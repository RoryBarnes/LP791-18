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

# Tweak
plt.rcParams.update({"font.size": 16, "legend.fontsize": 16})

# Run vplanet
output = vplanet.run(path / "vpl.in", units=False)

Time = output.b.Time * 1e-6
bwatlost = [10-x for x in output.b.SurfWaterMass]
dwatlost = [10-x for x in output.d.SurfWaterMass]
boxy = output.b.OxygenMass
doxy = output.d.OxygenMass

fig = plt.figure(figsize=(16,8))

wat = fig.add_subplot(1, 2, 1)
oxy = fig.add_subplot(1, 2, 2)

wat.plot(Time, bwatlost, color='magenta', label='Planet b')
wat.plot(Time, dwatlost, 'k--', label='Planet d')

oxy.plot(Time, boxy, color='magenta')
oxy.plot(Time, doxy, 'k--')

wat.set_xlabel('Time [days]')
oxy.set_xlabel('Time [days]')

wat.set_ylabel('Water Loss [TO]')
oxy.set_ylabel('Oxygen Produced [Bars]')

wat.set_xlim([0,1500])
oxy.set_xlim([0,1500])

plt.tight_layout()
wat.legend()
# plt.show()
plt.savefig('WaterLossSagynbayevaSabina.png', dpi=400)