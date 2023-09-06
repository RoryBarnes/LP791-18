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
# from get_args import get_args

# Run vplanet
# out = vplanet.run(path / "vpl.in")
out = vplanet.get_output(path)
time = out.TGstar.Time / 1e3

fig = plt.figure(figsize=(6.5, 8))
plt.subplot(3, 2, 1)
plt.plot(time, out.TGb.Obliquity, color="k")
plt.plot(time, out.TGd.Obliquity, color="C0")
plt.plot(time, out.TGc.Obliquity, color=vplot.colors.red)
plt.xlabel("Time (kyr)")
plt.ylabel(r"Obliquity ($^\circ$)")

plt.subplot(3, 2, 2)
plt.plot(time, out.TGb.Eccentricity, color="k")
plt.plot(time, out.TGd.Eccentricity, color="C0")
plt.plot(time, out.TGc.Eccentricity, color=vplot.colors.red)
plt.xlabel("Time (kyr)")
plt.ylabel("Eccentricity")

plt.subplot(3, 2, 3)
plt.plot(time, out.TGb.RotPer, color="k")
plt.plot(time, out.TGd.RotPer, color="C0")
plt.plot(time, out.TGc.RotPer, color=vplot.colors.red)
plt.xlabel("Time (kyr)")
plt.ylabel("Rotation Period (days)")

plt.subplot(3, 2, 4)
plt.plot(time, out.TGb.DynEllip, color="k")
plt.plot(time, out.TGd.DynEllip, color="C0")
plt.plot(time, out.TGc.DynEllip, color=vplot.colors.red)
plt.ylabel("Dynamical Ellipticity")
plt.xlabel("Time (kyr)")
#plt.legend(loc="upper right", fontsize=12, ncol=1)


plt.subplot(3, 2, 5)
plt.plot(time, out.TGb.CassiniOne, color="k")
plt.plot(time, out.TGd.CassiniOne, color="C0")
plt.plot(time, out.TGc.CassiniOne, color=vplot.colors.red)
plt.xlabel("Time (kyr)")
plt.ylabel("$\sin{\Psi}$")

plt.subplot(3, 2, 6)
plt.plot(time, out.TGb.CassiniTwo, color="k")
plt.plot(time, out.TGd.CassiniTwo, color="C0")
plt.plot(time, out.TGc.CassiniTwo, color=vplot.colors.red)
plt.xlabel("Time (kyr)")
plt.ylabel("$\cos{\Psi}$")

# Save the figure
# ext = get_args().ext
fig.tight_layout()
fig.savefig("CassiniMulti.pdf")
