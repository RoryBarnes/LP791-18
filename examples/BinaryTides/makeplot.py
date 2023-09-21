"""
This script produces a reproduction of Figure 1 of Zahn & Bouchet (1989)
using a coupled EQTIDE and STELLAR VPLANET run.

David P. Fleming, University of Washington, 2018
"""
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
mpl.rcParams["font.size"] = 18.0

# Run vplanet
output = vplanet.run(path / "vpl.in", units=False)

# Load data
time = output.primary.Time

# Extract important quantities
# saOutputOrder	Time -TotEn -TotAngMom -Semim -Radius -RotPer Ecce -RotRate -MeanMotion -OrbPer -SurfEnFluxTotal
Omega = output.secondary.RotRate  # Rotation Rate
omega = output.secondary.MeanMotion  # Mean Motion
e = output.secondary.Eccentricity
period = 2.0 * np.pi / omega
om = Omega / omega

# Plot it!
fig, ax = plt.subplots()

# Twin the x-axis twice to make independent y-axes.
axes = [ax, ax.twinx(), ax.twinx()]

# Make some space on the right side for the extra y-axis.
fig.subplots_adjust(right=0.75)

# Move the last y-axis spine over to the right by 20% of the width of the axes
axes[-1].spines["right"].set_position(("axes", 1.2))

# To make the border of the right-most axis visible, we need to turn the frame
# on. This hides the other plots, however, so we need to turn its fill off.
axes[-1].set_frame_on(True)
axes[-1].patch.set_visible(False)

# And finally we get to plot things...
data = [e, period, om]
labels = [r"Eccentricity", r"Orbital Period [days]", r"$\Omega$/$n$"]
legend_labels = [r"Eccentricity", r"Orbital Period", r"$\Omega$/$n$"]
linestyle = ["-", "--", "-."]
colors = ["#C91111", "#642197", "#1321D8"]

# Plot each quantities, format axes
for i in range(0, len(axes)):
    axes[i].plot(time, data[i], lw=3, ls=linestyle[i], color=colors[i], label="")
    axes[i].set_ylabel(labels[i], color=colors[i])
    axes[i].tick_params(axis="y", colors=colors[i])
    axes[i].set_xlim(time[1], time[-1])
    axes[i].set_xscale("log")
    axes[i].grid(False)

for ii in range(len(axes)):
    ax.plot(
        [100], [100], color=colors[ii], ls=linestyle[ii], label=legend_labels[ii], lw=3
    )
ax.legend(loc="lower left")

# Additional formatting
axes[1].set_ylabel(labels[1], color=colors[1], labelpad=15)
axes[0].set_ylim(0.0, 0.35)
axes[0].set_xlabel("Time [yr]")
axes[0].tick_params(axis="x", pad=10)

# Add text to plot to mirror Zahn+1989 figure
plt.text(
    0.77,
    0.9,
    r"1 M$_{\odot}$ + 1 M$_{\odot}$",
    horizontalalignment="center",
    verticalalignment="center",
    transform=axes[0].transAxes,
)

# Save figure
fig.tight_layout()
ext = get_args().ext
fig.savefig(path / f"BinaryTides.{ext}", bbox_inches="tight", dpi=600)
