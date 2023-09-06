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
#out = vplanet.run(path / "vpl.in")
out = vplanet.get_output(path)
time = out.star.Time / 1e3

fig = plt.figure(figsize=(6.5, 8))
plt.subplot(3, 2, 1)
plt.plot(time, out.b.Obliquity, color=vplot.colors.red)
plt.plot(time, out.d.Obliquity, color=vplot.colors.orange)
plt.plot(time, out.c.Obliquity, color=vplot.colors.pale_blue)
plt.ylabel(r"Obliquity ($^\circ$)")

plt.subplot(3, 2, 2)
plt.plot(time, out.b.SurfEnFluxTotal, color=vplot.colors.red)
plt.plot(time, out.d.SurfEnFluxTotal, color=vplot.colors.orange)
plt.plot(time, out.c.SurfEnFluxTotal, color=vplot.colors.pale_blue)
plt.ylabel(r"Surface Energy Flux (W/m$^2$)")

plt.subplot(3, 2, 3)
plt.plot(time, out.b.RotPer, color=vplot.colors.red)
plt.plot(time, out.d.RotPer, color=vplot.colors.orange)
plt.plot(time, out.c.RotPer, color=vplot.colors.pale_blue)
plt.ylabel("Rotation Period (days)")

plt.subplot(3, 2, 4)
plt.plot(time, out.b.DynEllip, color=vplot.colors.red, label="b")
plt.plot(time, out.d.DynEllip, color=vplot.colors.orange, label="d")
plt.plot(time, out.c.DynEllip, color=vplot.colors.pale_blue, label="c")
plt.ylabel("Dynamical Ellipticity")
plt.legend(loc="upper right", fontsize=12, ncol=1)

plt.subplot(3, 2, 5)
plt.plot(time, out.b.CassiniOne, color=vplot.colors.red)
plt.plot(time, out.d.CassiniOne, color=vplot.colors.orange)
plt.plot(time, out.c.CassiniOne, color=vplot.colors.pale_blue)
plt.xlabel("Time (kyr)")
plt.ylabel("$\sin{\Psi}$")

plt.subplot(3, 2, 6)
plt.plot(time, out.b.CassiniTwo, color=vplot.colors.red)
plt.plot(time, out.d.CassiniTwo, color=vplot.colors.orange)
plt.plot(time, out.c.CassiniTwo, color=vplot.colors.pale_blue)
plt.xlabel("Time (kyr)")
plt.ylabel("$\cos{\Psi}$")

# Save the figure
ext = get_args().ext
fig.tight_layout()
fig.savefig(path / f"RotationBarnesRory.{ext}")
