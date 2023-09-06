#!/usr/bin/env python
import pathlib
import subprocess
import sys

import bigplanet as bp
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import vplot as vpl

import vplanet

# Path hacks
path = pathlib.Path(__file__).parents[0].absolute()
sys.path.insert(1, str(path.parents[0]))

# Run vspace
if not (path / "WaterLossSilvaLaura").exists():
    print("Running VSPACE...")
    subprocess.check_output(["vspace", "vspace.in"], cwd=path)
else:
    print("VPSACE already run")

# Run multi-planet
if not (path / ".WaterLossSilvaLaura").exists():
    print("Running MultiPlanet...")
    subprocess.check_output(["multiplanet", "vspace.in"], cwd=path)
else:
    print("Multiplanet already run")

# Run bigplanet
if not (path / "WaterLossSilvaLaura.bpf").exists():
    print("Building BigPlanet File")
    subprocess.check_output(["bigplanet", "bpl.in"], cwd=path)
else:
    print("BigPlanet File already built")

print("Creating figure...")
data = bp.BPLFile(path / "WaterLossSilvaLaura.bpf")

bwatinitial = bp.ExtractColumn(data, 'b:SurfWaterMass:initial')
dwatinitial = bp.ExtractColumn(data, 'd:SurfWaterMass:initial')

bwatfinal = bp.ExtractColumn(data, 'b:SurfWaterMass:final')
dwatfinal = bp.ExtractColumn(data, 'd:SurfWaterMass:final')

bwatlost = [bwatinitial[x]-bwatfinal[x] for x in range(len(bwatinitial))]
dwatlost = [dwatinitial[x]-dwatfinal[x] for x in range(len(dwatinitial))]

boxyfinal = bp.ExtractColumn(data, 'b:OxygenMass:final')
doxyfinal = bp.ExtractColumn(data, 'd:OxygenMass:final')

fig = plt.figure(figsize=(8,8))

watb = fig.add_subplot(2, 2, 1)
oxyb = fig.add_subplot(2, 2, 2)
watd = fig.add_subplot(2, 2, 3)
oxyd = fig.add_subplot(2, 2, 4)

#watbhist = watb.hist2d(bwatinitial, bwatlost)
#oxybhist = oxyb.hist2d(bwatinitial, boxyfinal)
#watdhist = watd.hist2d(dwatinitial, dwatlost)
#oxydhist = oxyd.hist2d(dwatinitial, doxyfinal)
#fig.colorbar(watbhist[3])
#fig.colorbar(oxybhist[3])
#fig.colorbar(watdhist[3])
#fig.colorbar(oxydhist[3])

watb.hist2d(bwatinitial, bwatlost)
oxyb.hist2d(bwatinitial, boxyfinal)
watd.hist2d(dwatinitial, dwatlost)
oxyd.hist2d(dwatinitial, doxyfinal)

watb.set_xlabel('Initial Water [TO]')
oxyb.set_xlabel('Initial Water [TO]')
watd.set_xlabel('Initial Water [TO]')
oxyd.set_xlabel('Initial Water [TO]')

watb.set_ylabel('Water Lost [TO]')
watd.set_ylabel('Water Lost [TO]')

oxyb.set_ylabel('Oxygen Produced [bars]')
oxyd.set_ylabel('Oxygen Produced [bars]')

plt.tight_layout()
plt.show()


#mpl.rcParams["figure.figsize"] = (6.5, 6.5)
#fig = plt.figure()
#RIC = bp.ExtractColumn(data, "earth:RIC:final")
#RIC_units = bp.ExtractUnits(data, "earth:RIC:final")

