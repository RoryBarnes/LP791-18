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

Time = 1e-9*output.b.Time
bwatlost = [10-x for x in output.b.SurfWaterMass]
dwatlost = [10-x for x in output.d.SurfWaterMass]
boxy = output.b.OxygenMass
doxy = output.d.OxygenMass

fig = plt.figure(figsize=(16,8))

wat = fig.add_subplot(1, 2, 1)
oxy = fig.add_subplot(1, 2, 2)

wat.plot(Time, bwatlost, color='xkcd:blue', label='planet b')
wat.plot(Time, dwatlost, color='xkcd:red', label='planet d')

oxy.plot(Time, boxy, color='xkcd:blue')
oxy.plot(Time, doxy, color='xkcd:red')

wat.set_xlabel('Time (Gy)')
wat.set_ylabel('Water Loss (Earth Oceans)')
wat.set_xlim(0,2)

oxy.set_xlabel('Time (Gy)')
oxy.set_ylabel('Oxygen (bars)')
oxy.set_xlim(0,2)

wat.legend()

plt.tight_layout()
plt.savefig('WaterLossJacobsonSeth.png', dpi=400)