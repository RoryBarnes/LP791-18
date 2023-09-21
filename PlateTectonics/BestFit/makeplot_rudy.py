import pathlib
import sys

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import vplot

import vplanet


plt.rcParams['font.size'] = '10'
plt.rcParams['axes.labelsize'] = '10'
plt.rcParams['xtick.labelsize'] = '10'
plt.rcParams['ytick.labelsize'] = '10'
plt.rcParams['legend.fontsize'] = '5'
plt.rcParams['patch.linewidth'] = '0'

out = vplanet.get_output(units = False)


fig, ax = plt.subplots(3,1)

ax[0].plot(out.tidalearth.Time, out.tidalearth.TUMan, c = 'k')

ax[1].plot(out.tidalearth.Time, out.tidalearth.MagMom, c = 'k')


ax[2].plot(out.tidalearth.Time, out.tidalearth.HflowUMan, c = vplot.colors.dark_blue, label = "Convection")
ax[2].plot(out.tidalearth.Time, out.tidalearth.RadPowerMan, c = vplot.colors.red, label = "Radioactivity")
ax[2].plot(out.tidalearth.Time, out.tidalearth.HflowMeltMan, c = vplot.colors.purple, label = "Melting")
ax[2].plot(out.tidalearth.Time, out.tidalearth.HflowCMB, c = 'k', label = "From Core")
ax[2].plot(out.tidalearth.Time, out.tidalearth.PowerEqtide, c = vplot.colors.orange, label = "Tides")



ax[0].set_ylabel("Upper Mantle Temp.\n[K]")
ax[1].set_ylabel("Magnetic Moment\n[Rel. to Earth]")
ax[2].set_ylabel("Heating/Cooling Rates\n[TW]")
ax[2].set_xlabel("Time [Gyrs]")

ax[2].set_ylim([0,275])
ax[2].legend(loc = 'best', ncol = 2, frameon = False)

plt.savefig("LP791-18dThermInt.png", dpi = 300)












