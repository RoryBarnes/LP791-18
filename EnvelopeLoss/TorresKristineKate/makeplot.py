"""

Code to generate the atmosphere escape + ocean + thermal interior potential
tidal evolution histories for Proxima Centauri b, Figure 25 from
Barnes et al. 2016

@author: David P. Fleming
@email: dflemin3 (at) uw (dot) edu

Date: Oct. 21st, 2018

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

# Run vplanet
lp79118 = vplanet.run(path / "vpl.in", units=False)

# Time grid same for all simulations
time = lp79118.star.Time / 1e6

# Define color preferences
elim_color = vplot.colors.dark_blue
rrlim_color = vplot.colors.pale_blue
auto_color = vplot.colors.orange
bondi_color = vplot.colors.red

# Define linestyles
l12_ls = "-"
lc17_ls = ":"

# Define Labels
l12_label = "Lopez12"
lc17_label = "Lehmer17"
auto_label = "AtmEscAuto"

# Plot!
mpl.rcParams.update({"font.size": 8})
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(6.5, 7), sharex=True)
axes = axes.flatten()
# for ax in axes:
#    ax.set_xlim(0, 200)

### Top Left Plot: L_XUV/L_tot vs Time ###
axes[0].plot(time, lp79118.star.LXUVTot / lp79118.star.Luminosity, color="k")
axes[0].set_ylabel(r"L$_{XUV}$/L$_{tot}$")
axes[0].set_yscale('log')

### Top Right Plot: HZ Limits ###
fbk = {"lw": 0.0, "edgecolor": None}
axes[1].plot(time, lp79118.star.HZLimRunaway, color="g")
axes[1].plot(time, lp79118.star.HZLimMaxGreenhouse, color="g")
axes[1].fill_between(
    time,
    lp79118.star.HZLimRunaway,
    lp79118.star.HZLimMaxGreenhouse,
    color="g",
    **fbk
)
axes[1].set_ylabel("Semi-Major Axis (AU)")
axes[1].set_ylim(0, 0.3)
# Plot horiz line indicating best fit semi-major axis for LP791-18 d
axes[1].axhline(y=0.01991554415888, xmin=0.0, xmax=7.0e9, ls="--", color="black")
axes[1].fill_between(
    time,
    0.050500,
    0.096837,
    color="g",
    **fbk,
    alpha=0.2
)
# Annotate best fit
axes[1].annotate(
    "d's orbit",
    xy=(0.25, 0.07),
    xycoords="axes fraction",
    fontsize=10,
    horizontalalignment="right",
    verticalalignment="bottom",
)
# Annotate HZ
axes[1].annotate(
    "HZ",
    xy=(0.4, 0.2),
    xycoords="axes fraction",
    fontsize=15,
    horizontalalignment="left",
    verticalalignment="bottom",
    color="w",
)

### Middle Left: Envelope Mass vs Time ###
axes[2].plot(
    time,
    lp79118.L12ELim.EnvelopeMass,
    color=elim_color,
    linestyle=l12_ls,
    label="E-limited",
)
axes[2].plot(
    time,
    lp79118.L12RRLim.EnvelopeMass,
    color=rrlim_color,
    linestyle=l12_ls,
    label="RR-limited",
)
axes[2].plot(
    time,
    lp79118.L12Auto.EnvelopeMass,
    color=auto_color,
    linestyle=l12_ls,
    label="AtmEscAuto",
)
axes[2].plot(
    time,
    lp79118.L12Bondi.EnvelopeMass,
    color=bondi_color,
    linestyle=l12_ls,
    label="Bondi-Limited",
)
axes[2].plot(
    time,
    lp79118.LC17ELim.EnvelopeMass,
    color=elim_color,
    linestyle=lc17_ls,
    label="",
)
axes[2].plot(
    time,
    lp79118.LC17RRLim.EnvelopeMass,
    color=rrlim_color,
    linestyle=lc17_ls,
    label="",
)
axes[2].plot(
    time,
    lp79118.LC17Auto.EnvelopeMass,
    color=auto_color,
    linestyle=lc17_ls,
    label="",
)
axes[2].plot(
    time,
    lp79118.LC17Bondi.EnvelopeMass,
    color=bondi_color,
    linestyle=lc17_ls,
    label="",
)
axes[2].set_ylabel(r"Envelope Mass (M$_\oplus$)")
axes[2].legend(loc="upper right", title="Escape Model")
# leg.get_frame().set_alpha(0.0)

### Middle Right: Planet radius vs Time ###
axes[3].plot(
    time,
    lp79118.L12ELim.PlanetRadius,
    color="k",
    linestyle=l12_ls,
    label="Lopez12",
)
axes[3].plot(
    time,
    lp79118.L12ELim.PlanetRadius,
    color=elim_color,
    linestyle=l12_ls,
    label="",
)
axes[3].plot(
    time,
    lp79118.L12RRLim.PlanetRadius,
    color=rrlim_color,
    linestyle=l12_ls,
    label="",
)
axes[3].plot(
    time,
    lp79118.L12Auto.PlanetRadius,
    color=auto_color,
    linestyle=l12_ls,
    label="",
)
axes[3].plot(
    time,
    lp79118.L12Bondi.PlanetRadius,
    color=bondi_color,
    linestyle=l12_ls,
    label="",
)
axes[3].plot(
    time,
    lp79118.LC17ELim.PlanetRadius,
    color="k",
    linestyle=lc17_ls,
    label="Lehmer17",
)
axes[3].plot(
    time,
    lp79118.LC17ELim.PlanetRadius,
    color=elim_color,
    linestyle=lc17_ls,
    label="",
)
axes[3].plot(
    time,
    lp79118.LC17RRLim.PlanetRadius,
    color=rrlim_color,
    linestyle=lc17_ls,
    label="",
)
axes[3].plot(
    time,
    lp79118.LC17Auto.PlanetRadius,
    color=auto_color,
    linestyle=lc17_ls,
    label="",
)
axes[3].plot(
    time,
    lp79118.LC17Bondi.PlanetRadius,
    color=bondi_color,
    linestyle=lc17_ls,
    label="",
)
axes[3].set_ylabel(r"Radius (R$_\oplus$)")
axes[3].legend(loc="upper right", title="Radius Model")
axes[3].set_ylim(0, 9)

### Bottom left: Water Mass vs Time ###
axes[4].plot(time, lp79118.L12ELim.SurfWaterMass, color=elim_color, linestyle=l12_ls)
axes[4].plot(time, lp79118.L12RRLim.SurfWaterMass, color=rrlim_color, linestyle=l12_ls)
axes[4].plot(time, lp79118.L12Auto.SurfWaterMass, color=auto_color, linestyle=l12_ls)
axes[4].plot(time, lp79118.L12Bondi.SurfWaterMass, color=bondi_color, linestyle=l12_ls)
axes[4].plot(time, lp79118.LC17ELim.SurfWaterMass, color=elim_color, linestyle=lc17_ls)
axes[4].plot(time, lp79118.LC17RRLim.SurfWaterMass, color=rrlim_color, linestyle=lc17_ls)
axes[4].plot(time, lp79118.LC17Auto.SurfWaterMass, color=auto_color, linestyle=lc17_ls)
axes[4].plot(time, lp79118.LC17Bondi.SurfWaterMass, color=bondi_color, linestyle=lc17_ls)
axes[4].set_ylabel("Water Mass (TO)")
axes[4].set_xlabel("Time (Myr)")
# axes[4].set_ylim(-0.0001,0.001)

### Botton Right: Oxygen Mass vs Time ###
axes[5].plot(time, lp79118.L12ELim.OxygenMass, color=elim_color, linestyle=l12_ls)
axes[5].plot(time, lp79118.L12RRLim.OxygenMass, color=rrlim_color, linestyle=l12_ls)
axes[5].plot(time, lp79118.L12Auto.OxygenMass, color=auto_color, linestyle=l12_ls)
axes[5].plot(time, lp79118.L12Bondi.OxygenMass, color=bondi_color, linestyle=l12_ls)
axes[5].plot(time, lp79118.LC17ELim.OxygenMass, color=elim_color, linestyle=lc17_ls)
axes[5].plot(time, lp79118.LC17RRLim.OxygenMass, color=rrlim_color, linestyle=lc17_ls)
axes[5].plot(time, lp79118.LC17Auto.OxygenMass, color=auto_color, linestyle=lc17_ls)
axes[5].plot(time, lp79118.LC17Bondi.OxygenMass, color=bondi_color, linestyle=lc17_ls)
axes[5].set_ylabel("Oxygen Pressure (bars)")
axes[5].set_xlabel("Time (Myr)")

# Save the figure
ext = get_args().ext
fig.savefig(path / f"LP791-18d.{ext}", bbox_inches="tight", dpi=600)
