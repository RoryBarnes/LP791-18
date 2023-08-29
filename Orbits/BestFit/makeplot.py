
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

# Typical plot parameters that make for pretty plot
mpl.rcParams["figure.figsize"] = (10, 8)
mpl.rcParams["font.size"] = 16.0

# Run vplanet
output = vplanet.run(path / "vpl.in", units=False)

# Extract data
time = output.b.Time / 1.0e6  # Scale to Myr
ecc1 = output.b.Eccentricity
ecc2 = output.d.Eccentricity
ecc3 = output.c.Eccentricity
varpi1 = output.b.LongP
varpi2 = output.d.LongP
varpi3 = output.c.LongP
a1 = output.b.SemiMajorAxis
a2 = output.d.SemiMajorAxis
a3 = output.c.SemiMajorAxis
P1 = output.b.RotPer
P2 = output.d.RotPer
P3 = output.c.RotPer
i1 = output.b.Inc
i2 = output.d.Inc
i3 = output.c.Inc

# Plot
fig, axes = plt.subplots(nrows=3, ncols=2, sharex=True)
color = "k"

## Upper left: a1 ##
axes[0, 0].plot(time, a1, color="C3", zorder=-1, label="LP791-18b")

# Format
axes[0, 0].set_xlim(time.min(), time.max())
axes[0, 0].legend(loc="best")
axes[0, 0].set_ylim(0.0098, 0.00981)
axes[0, 0].set_ylabel("Semi-major Axis [AU]")

## Upper right: eccentricities ##
axes[0, 1].plot(time, ecc1, color="C3", zorder=-1)
axes[0, 1].plot(time, ecc2, color="C0", zorder=-1)
axes[0, 1].plot(time, ecc3, color="C1", zorder=-1)

# Format
axes[0, 1].set_xlim(time.min(), time.max())
# axes[0, 1].set_ylim(0.0, 0.2)
axes[0, 1].set_ylabel("Eccentricity")

## Middle left: a2 ##
axes[1, 0].plot(time, a2, color="C0", zorder=-1, label="LP791-18d")

# Format
axes[1, 0].set_xlim(time.min(), time.max())
axes[1, 0].legend(loc="best")
axes[1, 0].set_ylim(0.0196, 0.0204)
axes[1, 0].set_ylabel("Semi-major Axis [AU]")

## Middle right: diff between longitude of periapses ##
# varpiDiff = np.fabs(np.fmod(varpi1 - varpi2, 360.0))
# varpiDiff2 = np.fabs(np.fmod(varpi2 - varpi3, 360.0))
# axes[1, 1].scatter(time, varpiDiff, color="C3", s=10, zorder=-1)
# axes[1, 1].scatter(time, varpiDiff2, color="C1", s=10, zorder=-1)
#
# # Format
# axes[1, 1].set_xlim(time.min(), time.max())
# # axes[1, 1].set_ylim(0, 360)
# axes[1, 1].set_xlabel("Time [Myr]")
# axes[1, 1].set_ylabel(r"$\Delta \varpi$ [$^{\circ}$]")

axes[1, 1].plot(time, i1, color="C3", zorder=-1)
axes[1, 1].plot(time, i2, color="C0", zorder=-1)
axes[1, 1].plot(time, i3, color="C1", zorder=-1)

# Format
axes[1, 1].set_xlim(time.min(), time.max())
# axes[0, 1].set_ylim(0.0, 0.2)
axes[1, 1].set_ylabel("Inclination (deg)")

## Lower left: a3 ##
axes[2, 0].plot(time, a3, color="C1", zorder=-1, label="LP791-18c")

# Format
axes[2, 0].set_xlim(time.min(), time.max())
axes[2, 0].legend(loc="best")
axes[2, 0].set_ylim(0.0293, 0.03)
axes[2, 0].set_xlabel("Time [Myr]")
axes[2, 0].set_ylabel("Semi-major Axis [AU]")

## Lower right: rotation periods ##
axes[2, 1].plot(time, P1, color="C3", zorder=-1)
axes[2, 1].plot(time, P2, color="C0", zorder=-1)
axes[2, 1].plot(time, P3, color="C1", zorder=-1)

# Format
axes[2, 1].set_xlim(time.min(), time.max())
# axes[2, 1].set_ylim(0, 5)
axes[2, 1].set_xlabel("Time [Myr]")
axes[2, 1].set_ylabel(r"Rotation period (days)")

# Final formating
#fig.tight_layout()
for ax in axes.flatten():
    # Rasterize
    ax.set_rasterization_zorder(0)

    # Set tick locations
    #ax.set_xticklabels(["0", "2", "4", "6", "8", "10"])
    # ax.set_xticks([0, 2, 4, 6, 8, 10])

# Show late-term ecc damping
# inset1 = fig.add_axes([0.74, 0.735, 0.2, 0.2])
# inset1.plot(time, ecc1, color="C3", zorder=20)
# inset1.plot(time, ecc2, color="C0", zorder=20)
#
# inset1.set_xlabel("Time [Myr]", fontsize=12)
# inset1.set_ylabel("Eccentricity", fontsize=12)
# inset1.set_xlim(8, 10)
# inset1.set_xticks([8, 9, 10])
# inset1.set_xticklabels(["8", "9", "10"], fontsize=12)
# inset1.set_yticks([1.0e-4, 1.0e-3, 1.0e-2])
# inset1.set_yticklabels(["$10^{-4}$", "$10^{-3}$", "$10^{-2}$"], fontsize=12)
# inset1.set_yscale("log")

# Show early apsidal locking
# inset2 = fig.add_axes([0.74, 0.235, 0.2, 0.2])
# inset2.scatter(time, varpiDiff, color="C3", s=10, zorder=20)
#
# inset2.set_xlim(0.1, 3)
# inset2.set_ylim(0, 360)
# inset2.set_xscale("log")
# inset2.set_yticks([0, 180, 360])
# inset2.set_yticklabels(["0", "180", "360"], fontsize=12)
# inset2.set_ylabel(r"$\Delta \varpi$ [$^{\circ}$]", fontsize=12)
# inset2.set_xticks([0.1, 0.25, 0.5, 1, 2, 3])
# inset2.set_xticklabels(["0.1", "0.25", "0.5", "1", "2", "3"], fontsize=12)
# inset2.set_xlabel("Time [Myr]", fontsize=12)

# Save the figure
#ext = get_args().ext
ext = "pdf"
#fig.savefig(path / f"ApseLock.{ext}", bbox_inches="tight", dpi=600)
fig.savefig(path / f"LP791-18_secular_bestfit.{ext}", dpi=600)
