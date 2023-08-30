#!/usr/bin/env python
import pathlib
import subprocess
import sys

import bigplanet as bp
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import vplot as vpl

import vplanet

lastname_firstname = ??
module = ?? # "distorb" or "eqtide"

# Path hacks
path = pathlib.Path(__file__).parents[0].absolute()
sys.path.insert(1, str(path.parents[0]))
from get_args import get_args

# Run vspace
if not (path / (lastname_firstname+f"_{module}")).exists():
    print("Running VSPACE...")
    subprocess.check_output(["vspace", f"vspace_{module}.in"], cwd=path)
else:
    print("VPSACE already run")

# Run multi-planet
if not (path / ("."+lastname_firstname+f"_{module}")).exists():
    print("Running MultiPlanet...")
    subprocess.check_output(["multiplanet", "-c", "1", "-bp", f"vspace_{module}.in"], cwd=path)
else:
    print("Multiplanet already run")

# Run bigplanet
if not (path / (lastname_firstname+f"_{module}.bpf")).exists():
    print("Building BigPlanet File")
    subprocess.check_output(["bigplanet", f"bpl_{module}.in"], cwd=path)
else:
    print("BigPlanet File already built")

print("Creating figure...")
data = bp.BPLFile(path / (lastname_firstname+f"_{module}.bpf"))

mpl.rcParams["figure.figsize"] = (6.5, 6.5)


time = bp.ExtractColumn(data, "b:Time:forward")
eccb = bp.ExtractColumn(data, "b:Eccentricity:forward")
semib = bp.ExtractColumn(data, "b:SemiMajorAxis:forward")

eccd = bp.ExtractColumn(data, "d:Eccentricity:forward")
semid = bp.ExtractColumn(data, "d:SemiMajorAxis:forward")

eccc = bp.ExtractColumn(data, "c:Eccentricity:forward")
semic = bp.ExtractColumn(data, "c:SemiMajorAxis:forward")

if module == "distorb":
  incb = bp.ExtractColumn(data, "b:Inc:forward")
  incd = bp.ExtractColumn(data, "d:Inc:forward")
  incc = bp.ExtractColumn(data, "c:Inc:forward")

fig, axes = plt.subplots(ncols=2,nrows=3,sharex=True)

for i in np.arange(len(eccb)):
    axes[0][0].plot(time[i], eccb[i])
    axes[1][0].plot(time[i], eccd[i])
    axes[2][0].plot(time[i], eccc[i])

    if module == "distorb":
        axes[0][1].plot(time[i], incb[i])
        axes[1][1].plot(time[i], incd[i])
        axes[2][1].plot(time[i], incc[i])
    else:
        axes[0][1].plot(time[i], semib[i])
        axes[1][1].plot(time[i], semid[i])
        axes[2][1].plot(time[i], semic[i])

axes[0][0].set_ylabel("Eccentricity (b)")
axes[1][0].set_ylabel("Eccentricity (d)")
axes[2][0].set_ylabel("Eccentricity (c)")

if module == "distorb":
    axes[0][1].set_ylabel("Inclination (b)")
    axes[1][1].set_ylabel("Inclination (d)")
    axes[2][1].set_ylabel("Inclination (c)")
else:
    axes[0][1].set_ylabel("Semi-major axis (b)")
    axes[1][1].set_ylabel("Semi-major axis (d)")
    axes[2][1].set_ylabel("Semi-major axis (c)")

# Save the figure
ext = get_args().ext
fig.savefig(path / (lastname_firstname+f"_{module}.{ext}"), dpi=300)
