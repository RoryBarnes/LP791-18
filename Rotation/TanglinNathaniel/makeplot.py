import pathlib
import sys

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import vplot

import vplanet

# Path hacks
path = pathlib.Path(__file__).parents[0].absolute()
sys.path.insert(1, str(path.parents[0]))
from get_args import get_args

# Run vplanet
out = vplanet.get_output(path) #vplanet.run(path / "vpl.in")
time = out.TGstar.Time / 1e3

fig = plt.figure(figsize=(8, 8))
plt.subplot(2, 2, 3)
plt.plot(time, out.TGb.Obliquity, color="k")
plt.plot(time, out.TGd.Obliquity, color=vplot.colors.pale_blue)
plt.plot(time, out.TGc.Obliquity, color=vplot.colors.red)
plt.ylabel(r"Obliquity ($^\circ$)")

plt.subplot(2, 2, 1)
plt.plot(time, out.TGb.RotPer, color="k")
plt.plot(time, out.TGd.RotPer, color=vplot.colors.pale_blue)
plt.plot(time, out.TGc.RotPer, color=vplot.colors.red)
plt.ylabel("Rotation Period (days)")

plt.subplot(2, 2, 2)
plt.plot(time, out.TGb.CassiniOne, color="k")
plt.plot(time, out.TGd.CassiniOne, color=vplot.colors.pale_blue)
plt.plot(time, out.TGc.CassiniOne, color=vplot.colors.red)
plt.xlabel("Time (kyr)")
plt.ylabel("$\sin{\Psi}$")

plt.subplot(2, 2, 4)
plt.plot(time, out.TGb.CassiniTwo, color="k")
plt.plot(time, out.TGd.CassiniTwo, color=vplot.colors.pale_blue)
plt.plot(time, out.TGc.CassiniTwo, color=vplot.colors.red)
plt.xlabel("Time (kyr)")
plt.ylabel("$\cos{\Psi}$")

# Save the figure
ext = get_args().ext
fig.tight_layout()
fig.savefig(path / f"CassiniMulti.{ext}")
