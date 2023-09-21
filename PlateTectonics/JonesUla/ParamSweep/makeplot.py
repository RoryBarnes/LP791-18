import numpy as np
import matplotlib.pyplot as plt

import bigplanet as bp


plt.rcParams['font.size'] = '8'
plt.rcParams['axes.labelsize'] = '8'
plt.rcParams['xtick.labelsize'] = '6'
plt.rcParams['ytick.labelsize'] = '6'


data = bp.BPLFile("JonesUla.bpf")


MagMom = np.array(bp.ExtractColumn(data, 'tidalearth:MagMom:forward'))
HflowMeltMan = np.array(bp.ExtractColumn(data, 'tidalearth:HflowMeltMan:forward'))

dViscRef = np.array(bp.ExtractColumn(data, 'tidalearth:dViscRef:option'))
dElecCondCore = np.array(bp.ExtractColumn(data, 'tidalearth:dElecCondCore:option'))
dTMan = np.array(bp.ExtractColumn(data, 'tidalearth:dTMan:option'))
dEruptEff = np.array(bp.ExtractColumn(data, 'tidalearth:dEruptEff:option'))

Time = np.linspace(0, 10, len(MagMom[0]))


# Define a variable dict to associate strings with the array in that string
variable_dict = {"MagMom": MagMom, "HflowMeltMan": HflowMeltMan, "dViscRef": dViscRef, 
				"dElecCondCore": dElecCondCore, "dTMan": dTMan, "dEruptEff": dEruptEff}


def GetValueAtTime(forwardArray, timeIndex):
	valueAtTime = np.zeros(len(forwardArray))

	for i in range(len(forwardArray)):
		valueAtTime[i] = forwardArray[i][timeIndex]

	return valueAtTime


def MakeTimePlots(xAxisVar, yAxisVar, cAxisVar):
	fig, ax = plt.subplots(2,2)

	xAxisVarVal = variable_dict[xAxisVar]
	yAxisVarVal = variable_dict[yAxisVar]
	cAxisVarVal = variable_dict[cAxisVar]

	



	min_cAxisVar = np.min([GetValueAtTime(cAxisVarVal, 4000), GetValueAtTime(cAxisVarVal, 6000), GetValueAtTime(cAxisVarVal, 8000), GetValueAtTime(cAxisVarVal, 10000)])
	max_cAxisVar = np.max([GetValueAtTime(cAxisVarVal, 4000), GetValueAtTime(cAxisVarVal, 6000), GetValueAtTime(cAxisVarVal, 8000), GetValueAtTime(cAxisVarVal, 10000)])


	fig, ax = plt.subplots(2,2)

	ax[0,0].set_title("4 Gyrs", fontsize = 6)
	ax[0,1].set_title("6 Gyrs", fontsize = 6)
	ax[1,0].set_title("8 Gyrs", fontsize = 6)
	ax[1,1].set_title("10 Gyrs", fontsize = 6)

	ax[0,0].set_ylabel(yAxisVar)
	ax[1,0].set_ylabel(yAxisVar)
	ax[1,0].set_xlabel(xAxisVar)
	ax[1,1].set_xlabel(xAxisVar)

	im = ax[0,0].scatter(xAxisVarVal, yAxisVarVal, c = GetValueAtTime(cAxisVarVal, 4000), vmin = min_cAxisVar, vmax = max_cAxisVar)
	ax[0,1].scatter(xAxisVarVal, yAxisVarVal, c = GetValueAtTime(cAxisVarVal, 6000), vmin = min_cAxisVar, vmax = max_cAxisVar)
	ax[1,0].scatter(xAxisVarVal, yAxisVarVal, c = GetValueAtTime(cAxisVarVal, 8000), vmin = min_cAxisVar, vmax = max_cAxisVar)
	ax[1,1].scatter(xAxisVarVal, yAxisVarVal, c = GetValueAtTime(cAxisVarVal, 10000), vmin = min_cAxisVar, vmax = max_cAxisVar)


	if xAxisVar == 'dViscRef':
		ax[0,0].set_xscale('log')
		ax[0,1].set_xscale('log')
		ax[1,0].set_xscale('log')
		ax[1,1].set_xscale('log')
		#xAxisVarVal = np.log10(xAxisVarVal)

	if yAxisVar == 'dViscRef':
		ax[0,0].set_yscale('log')
		ax[0,1].set_yscale('log')
		ax[1,0].set_yscale('log')
		ax[1,1].set_yscale('log')
		#yAxisVarVal = np.log10(yAxisVarVal)

	fig.colorbar(im, ax=ax.ravel().tolist())



	plt.savefig(xAxisVar + yAxisVar + cAxisVar + "PlateTectonics.png", dpi = 400)
	plt.close()



MakeTimePlots("dViscRef", "dElecCondCore", "MagMom")
MakeTimePlots("dViscRef", "dTMan", "MagMom")
MakeTimePlots("dViscRef", "dEruptEff", "MagMom")
MakeTimePlots("dElecCondCore", "dTMan", "MagMom")
MakeTimePlots("dElecCondCore", "dEruptEff", "MagMom")
MakeTimePlots("dTMan", "dEruptEff", "MagMom")

MakeTimePlots("dViscRef", "dElecCondCore", "HflowMeltMan")
MakeTimePlots("dViscRef", "dTMan", "HflowMeltMan")
MakeTimePlots("dViscRef", "dEruptEff", "HflowMeltMan")
MakeTimePlots("dElecCondCore", "dTMan", "HflowMeltMan")
MakeTimePlots("dElecCondCore", "dEruptEff", "HflowMeltMan")
MakeTimePlots("dTMan", "dEruptEff", "HflowMeltMan")











