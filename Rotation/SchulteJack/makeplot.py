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
out = vplanet.get_output(path)
print(out)
time = out.LP791_18star.Time / 1e3

fig = plt.figure(figsize=(6.5, 8))
plt.subplot(3, 2, 1)
plt.plot(time, out.LP791_18b.Obliquity, color="k", label="b")
plt.plot(time, out.LP791_18c.Obliquity, color=vplot.colors.red, label="c")
plt.plot(time, out.LP791_18d.Obliquity, color='#009B77', label="d")
plt.ylabel(r"Obliquity ($^\circ$)")
plt.legend(loc="upper right", fontsize=12, ncol=1)

plt.subplot(3, 2, 2)
plt.plot(time, out.LP791_18b.Eccentricity, color="k", label="b")
plt.plot(time, out.LP791_18c.Eccentricity, color=vplot.colors.red, label="c")
plt.plot(time, out.LP791_18d.Eccentricity, color='#009B77', label="d")
plt.ylabel("Eccentricity")
plt.legend(loc="upper right", fontsize=12, ncol=1)

plt.subplot(3, 2, 3)
plt.plot(time, out.LP791_18b.RotPer, color="k", label="b")
plt.plot(time, out.LP791_18c.RotPer, color=vplot.colors.red, label="c")
plt.plot(time, out.LP791_18d.RotPer, color='#009B77', label="d")
plt.ylabel("Rotation Period (days)")
plt.legend(loc="upper right", fontsize=12, ncol=1)

plt.subplot(3, 2, 4)
plt.plot(time, out.LP791_18b.DynEllip, color="k", label="b")
plt.plot(time, out.LP791_18c.DynEllip, color=vplot.colors.red, label="c")
plt.plot(time, out.LP791_18d.DynEllip, color='#009B77', label="d")
plt.ylabel("Dynamical Ellipticity")
plt.legend(loc="upper right", fontsize=12, ncol=1)

plt.subplot(3, 2, 5)
plt.plot(time, out.LP791_18b.CassiniOne, color="k", label="b")
plt.plot(time, out.LP791_18c.CassiniOne, color=vplot.colors.red, label="c")
plt.plot(time, out.LP791_18d.CassiniOne, color='#009B77', label="d")
plt.xlabel("Time (kyr)")
plt.ylabel("$\sin{\Psi}$")
plt.legend(loc="upper right", fontsize=12, ncol=1)

plt.subplot(3, 2, 6)
plt.plot(time, out.LP791_18b.CassiniTwo, color="k", label="b")
plt.plot(time, out.LP791_18c.CassiniTwo, color=vplot.colors.red, label="c")
plt.plot(time, out.LP791_18d.CassiniTwo, color='#009B77', label="d")
plt.xlabel("Time (kyr)")
plt.ylabel("$\cos{\Psi}$")
plt.legend(loc="upper right", fontsize=12, ncol=1)

# Save the figure
ext = get_args().ext
fig.tight_layout()
fig.savefig(path / f"CassiniMulti.{ext}")
