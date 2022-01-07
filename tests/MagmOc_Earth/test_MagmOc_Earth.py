from benchmark import Benchmark, benchmark 
import astropy.units as u 
import pytest 
 
@benchmark( 
   { 
       "log.initial.system.Age": {"value": 1.577880e+13, "unit": u.sec}, 
       "log.initial.system.Time": {"value": 0.000000, "unit": u.sec}, 
       "log.initial.system.TotAngMom": {"value": 8.296053e+43, "unit": (u.kg * u.m ** 2) / u.sec}, 
       "log.initial.system.TotEnergy": {"value": -9.104482e+40, "unit": u.Joule}, 
       "log.initial.system.PotEnergy": {"value": -9.406038e+40, "unit": u.Joule}, 
       "log.initial.system.KinEnergy": {"value": 3.015563e+39, "unit": u.Joule}, 
       "log.initial.system.DeltaTime": {"value": 0.000000, "unit": u.sec}, 
       "log.initial.Sun.Mass": {"value": 1.988416e+30, "unit": u.kg}, 
       "log.initial.Sun.Radius": {"value": 263.919878, "unit": u.Rearth}, 
       "log.initial.Sun.RadGyra": {"value": 0.449900}, 
       "log.initial.Sun.RotAngMom": {"value": 8.293392e+43, "unit": (u.kg * u.m ** 2) / u.sec}, 
       "log.initial.Sun.RotVel": {"value": 1.224136e+05, "unit": u.m / u.sec}, 
       "log.initial.Sun.BodyType": {"value": 0.000000}, 
       "log.initial.Sun.RotRate": {"value": 7.272205e-05, "unit": 1 / u.sec}, 
       "log.initial.Sun.RotPer": {"value": 8.640000e+04, "unit": u.sec}, 
       "log.initial.Sun.Density": {"value": 99.524124, "unit": u.kg / u.m ** 3}, 
       "log.initial.Sun.HZLimitDryRunaway": {"value": 1.887931e+11, "unit": u.m}, 
       "log.initial.Sun.HZLimRecVenus": {"value": 1.640992e+11, "unit": u.m}, 
       "log.initial.Sun.HZLimRunaway": {"value": 2.178515e+11, "unit": u.m}, 
       "log.initial.Sun.HZLimMoistGreenhouse": {"value": 2.171294e+11, "unit": u.m}, 
       "log.initial.Sun.HZLimMaxGreenhouse": {"value": 3.929566e+11, "unit": u.m}, 
       "log.initial.Sun.HZLimEarlyMars": {"value": 4.286401e+11, "unit": u.m}, 
       "log.initial.Sun.Instellation": {"value": -1.000000, "unit": u.kg / u.sec ** 3}, 
       "log.initial.Sun.CriticalSemiMajorAxis": {"value": -1.000000, "unit": u.m}, 
       "log.initial.Sun.LXUVTot": {"value": 7.435159e+23, "unit": u.kg / u.sec ** 3}, 
       "log.initial.Sun.LostEnergy": {"value": 5.562685e-309, "unit": u.Joule}, 
       "log.initial.Sun.LostAngMom": {"value": 5.562685e-309, "unit": (u.kg * u.m ** 2) / u.sec}, 
       "log.initial.Sun.Luminosity": {"value": 1.933219, "unit": u.LSUN}, 
       "log.initial.Sun.LXUVStellar": {"value": 0.001933, "unit": u.LSUN}, 
       "log.initial.Sun.Temperature": {"value": 4377.256537, "unit": u.K}, 
       "log.initial.Sun.LXUVFrac": {"value": 0.001000}, 
       "log.initial.Sun.RossbyNumber": {"value": 0.029996}, 
       "log.initial.Sun.DRotPerDtStellar": {"value": 9.510363e-10}, 
       "log.initial.Earth.Mass": {"value": 5.972186e+24, "unit": u.kg}, 
       "log.initial.Earth.Radius": {"value": 6.378100e+06, "unit": u.m}, 
       "log.initial.Earth.RadGyra": {"value": 0.500000}, 
       "log.initial.Earth.BodyType": {"value": 0.000000}, 
       "log.initial.Earth.Density": {"value": 5495.038549, "unit": u.kg / u.m ** 3}, 
       "log.initial.Earth.HZLimitDryRunaway": {"value": 1.888204e+11, "unit": u.m}, 
       "log.initial.Earth.HZLimRecVenus": {"value": 1.640992e+11, "unit": u.m}, 
       "log.initial.Earth.HZLimRunaway": {"value": 2.178515e+11, "unit": u.m}, 
       "log.initial.Earth.HZLimMoistGreenhouse": {"value": 2.171294e+11, "unit": u.m}, 
       "log.initial.Earth.HZLimMaxGreenhouse": {"value": 3.929566e+11, "unit": u.m}, 
       "log.initial.Earth.HZLimEarlyMars": {"value": 4.286401e+11, "unit": u.m}, 
       "log.initial.Earth.Instellation": {"value": 2644.188161, "unit": u.kg / u.sec ** 3}, 
       "log.initial.Earth.MeanMotion": {"value": 1.990987e-07, "unit": 1 / u.sec}, 
       "log.initial.Earth.OrbPeriod": {"value": 3.155815e+07, "unit": u.sec}, 
       "log.initial.Earth.SemiMajorAxis": {"value": 1.495979e+11, "unit": u.m}, 
       "log.initial.Earth.LXUVTot": {"value": -1.000000, "unit": u.kg / u.sec ** 3}, 
       "log.initial.Earth.SurfWaterMass": {"value": 6.950000e+21, "unit": u.kg}, 
       "log.initial.Earth.EnvelopeMass": {"value": 0.000000, "unit": u.kg}, 
       "log.initial.Earth.OxygenMass": {"value": 0.000000, "unit": u.kg}, 
       "log.initial.Earth.RGLimit": {"value": 2.116533e+11, "unit": u.m}, 
       "log.initial.Earth.XO": {"value": 0.333333}, 
       "log.initial.Earth.EtaO": {"value": 0.612158}, 
       "log.initial.Earth.PlanetRadius": {"value": 6.378100e+06, "unit": u.m}, 
       "log.initial.Earth.OxygenMantleMass": {"value": 0.000000, "unit": u.kg}, 
       "log.initial.Earth.RadXUV": {"value": -1.000000, "unit": u.m}, 
       "log.initial.Earth.RadSolid": {"value": -1.000000, "unit": u.m}, 
       "log.initial.Earth.PresXUV": {"value": 5.000000}, 
       "log.initial.Earth.ScaleHeight": {"value": -1.000000, "unit": u.m}, 
       "log.initial.Earth.ThermTemp": {"value": 195.374154, "unit": u.K}, 
       "log.initial.Earth.AtmGasConst": {"value": 4124.000000}, 
       "log.initial.Earth.PresSurf": {"value": -1.000000, "unit": u.Pa}, 
       "log.initial.Earth.DEnvMassDt": {"value": 0.000000, "unit": u.kg / u.sec}, 
       "log.initial.Earth.FXUV": {"value": 2.644188, "unit": u.W / u.m ** 2}, 
       "log.initial.Earth.AtmXAbsEffH2O": {"value": 0.300000}, 
       "log.initial.Earth.RocheRadius": {"value": 1.496558e+09, "unit": u.m}, 
       "log.initial.Earth.BondiRadius": {"value": 1.014863e+07, "unit": u.m}, 
       "log.initial.Earth.HEscapeRegime": {"value": 8.000000}, 
       "log.initial.Earth.RRCriticalFlux": {"value": 53.023382, "unit": u.W / u.m ** 2}, 
       "log.initial.Earth.KTide": {"value": 0.993607}, 
       "log.initial.Earth.RGDuration": {"value": 0.00000e+00, "unit": u.yr}, 
       "log.initial.Earth.WaterMassMOAtm": {"value": 5.000000, "unit": u.TO}, 
       "log.initial.Earth.PotTemp": {"value": 4000.000000, "unit": u.K}, 
       "log.initial.Earth.SurfTemp": {"value": 4000.000000, "unit": u.K}, 
       "log.initial.Earth.WaterMassSol": {"value": 0.000000, "unit": u.TO}, 
       "log.initial.Earth.SolidRadius": {"value": 0.533074, "unit": u.Rearth}, 
       "log.initial.Earth.OxygenMassMOAtm": {"value": 0.000000, "unit": u.kg}, 
       "log.initial.Earth.OxygenMassSol": {"value": 0.000000, "unit": u.kg}, 
       "log.initial.Earth.PressWaterAtm": {"value": 2.468645e+06}, 
       "log.initial.Earth.PressOxygenAtm": {"value": 0.000000}, 
       "log.initial.Earth.HydrogenMassSpace": {"value": 0.000000, "unit": u.kg}, 
       "log.initial.Earth.OxygenMassSpace": {"value": 0.000000, "unit": u.kg}, 
       "log.initial.Earth.FracFe2O3Man": {"value": 0.000000}, 
       "log.initial.Earth.NetFluxAtmo": {"value": 1.340582e+05}, 
       "log.initial.Earth.WaterFracMelt": {"value": 0.001849}, 
       "log.initial.Earth.RadioPower": {"value": 9.823813e+13, "unit": u.W}, 
       "log.initial.Earth.TidalPower": {"value": 0.000000, "unit": u.W}, 
       "log.initial.Earth.HZInnerEdge": {"value": 2.116533e+11, "unit": u.m}, 
       "log.initial.Earth.MeltFraction": {"value": 1.000000}, 
       "log.initial.Earth.CO2MassMOAtm": {"value": 0.000000, "unit": u.kg}, 
       "log.initial.Earth.CO2MassSol": {"value": 0.000000, "unit": u.kg}, 
       "log.initial.Earth.PressCO2Atm": {"value": 0.000000}, 
       "log.initial.Earth.CO2FracMelt": {"value": 0.000000}, 
       "log.final.system.Age": {"value": 1.893456e+13, "unit": u.sec}, 
       "log.final.system.Time": {"value": 3.155760e+12, "unit": u.sec}, 
       "log.final.system.TotAngMom": {"value": 8.296053e+43, "unit": (u.kg * u.m ** 2) / u.sec}, 
       "log.final.system.TotEnergy": {"value": -9.104482e+40, "unit": u.Joule}, 
       "log.final.system.PotEnergy": {"value": -9.406038e+40, "unit": u.Joule}, 
       "log.final.system.KinEnergy": {"value": 2.813173e+39, "unit": u.Joule}, 
       "log.final.system.DeltaTime": {"value": 3.019866e+06, "unit": u.sec}, 
       "log.final.Sun.Mass": {"value": 1.988416e+30, "unit": u.kg}, 
       "log.final.Sun.Radius": {"value": 263.919878, "unit": u.Rearth}, 
       "log.final.Sun.RadGyra": {"value": 0.449900}, 
       "log.final.Sun.RotAngMom": {"value": 8.010254e+43, "unit": (u.kg * u.m ** 2) / u.sec}, 
       "log.final.Sun.RotVel": {"value": 1.182343e+05, "unit": u.m / u.sec}, 
       "log.final.Sun.BodyType": {"value": 0.000000}, 
       "log.final.Sun.RotRate": {"value": 7.023931e-05, "unit": 1 / u.sec}, 
       "log.final.Sun.RotPer": {"value": 8.945398e+04, "unit": u.sec}, 
       "log.final.Sun.Density": {"value": 99.524124, "unit": u.kg / u.m ** 3}, 
       "log.final.Sun.HZLimitDryRunaway": {"value": 1.887931e+11, "unit": u.m}, 
       "log.final.Sun.HZLimRecVenus": {"value": 1.640992e+11, "unit": u.m}, 
       "log.final.Sun.HZLimRunaway": {"value": 2.178515e+11, "unit": u.m}, 
       "log.final.Sun.HZLimMoistGreenhouse": {"value": 2.171294e+11, "unit": u.m}, 
       "log.final.Sun.HZLimMaxGreenhouse": {"value": 3.929566e+11, "unit": u.m}, 
       "log.final.Sun.HZLimEarlyMars": {"value": 4.286401e+11, "unit": u.m}, 
       "log.final.Sun.Instellation": {"value": -1.000000, "unit": u.kg / u.sec ** 3}, 
       "log.final.Sun.CriticalSemiMajorAxis": {"value": -1.000000, "unit": u.m}, 
       "log.final.Sun.LXUVTot": {"value": 7.435159e+23, "unit": u.kg / u.sec ** 3}, 
       "log.final.Sun.LostEnergy": {"value": 2.023891e+38, "unit": u.Joule}, 
       "log.final.Sun.LostAngMom": {"value": 2.831382e+42, "unit": (u.kg * u.m ** 2) / u.sec}, 
       "log.final.Sun.Luminosity": {"value": 1.933219, "unit": u.LSUN}, 
       "log.final.Sun.LXUVStellar": {"value": 0.001933, "unit": u.LSUN}, 
       "log.final.Sun.Temperature": {"value": 4377.256537, "unit": u.K}, 
       "log.final.Sun.LXUVFrac": {"value": 0.001000}, 
       "log.final.Sun.RossbyNumber": {"value": 0.031056}, 
       "log.final.Sun.DRotPerDtStellar": {"value": 9.846526e-10}, 
       "log.final.Earth.Mass": {"value": 5.972186e+24, "unit": u.kg}, 
       "log.final.Earth.Radius": {"value": 6.378100e+06, "unit": u.m}, 
       "log.final.Earth.RadGyra": {"value": 0.500000}, 
       "log.final.Earth.BodyType": {"value": 0.000000}, 
       "log.final.Earth.Density": {"value": 5495.038549, "unit": u.kg / u.m ** 3}, 
       "log.final.Earth.HZLimitDryRunaway": {"value": 1.888204e+11, "unit": u.m}, 
       "log.final.Earth.HZLimRecVenus": {"value": 1.640992e+11, "unit": u.m}, 
       "log.final.Earth.HZLimRunaway": {"value": 2.178515e+11, "unit": u.m}, 
       "log.final.Earth.HZLimMoistGreenhouse": {"value": 2.171294e+11, "unit": u.m}, 
       "log.final.Earth.HZLimMaxGreenhouse": {"value": 3.929566e+11, "unit": u.m}, 
       "log.final.Earth.HZLimEarlyMars": {"value": 4.286401e+11, "unit": u.m}, 
       "log.final.Earth.Instellation": {"value": 2644.188161, "unit": u.kg / u.sec ** 3}, 
       "log.final.Earth.MeanMotion": {"value": 1.990987e-07, "unit": 1 / u.sec}, 
       "log.final.Earth.OrbPeriod": {"value": 3.155815e+07, "unit": u.sec}, 
       "log.final.Earth.SemiMajorAxis": {"value": 1.495979e+11, "unit": u.m}, 
       "log.final.Earth.LXUVTot": {"value": -1.000000, "unit": u.kg / u.sec ** 3}, 
       "log.final.Earth.SurfWaterMass": {"value": 6.950000e+21, "unit": u.kg}, 
       "log.final.Earth.EnvelopeMass": {"value": 0.000000, "unit": u.kg}, 
       "log.final.Earth.OxygenMass": {"value": 0.000000, "unit": u.kg}, 
       "log.final.Earth.RGLimit": {"value": 2.116533e+11, "unit": u.m}, 
       "log.final.Earth.XO": {"value": 0.333333}, 
       "log.final.Earth.EtaO": {"value": 0.612158}, 
       "log.final.Earth.PlanetRadius": {"value": 6.378100e+06, "unit": u.m}, 
       "log.final.Earth.OxygenMantleMass": {"value": 0.000000, "unit": u.kg}, 
       "log.final.Earth.RadXUV": {"value": -1.000000, "unit": u.m}, 
       "log.final.Earth.RadSolid": {"value": -1.000000, "unit": u.m}, 
       "log.final.Earth.PresXUV": {"value": 5.000000}, 
       "log.final.Earth.ScaleHeight": {"value": -1.000000, "unit": u.m}, 
       "log.final.Earth.ThermTemp": {"value": 195.374154, "unit": u.K}, 
       "log.final.Earth.AtmGasConst": {"value": 4124.000000}, 
       "log.final.Earth.PresSurf": {"value": -1.000000, "unit": u.Pa}, 
       "log.final.Earth.DEnvMassDt": {"value": 0.000000, "unit": u.kg / u.sec}, 
       "log.final.Earth.FXUV": {"value": 2.644188, "unit": u.W / u.m ** 2}, 
       "log.final.Earth.AtmXAbsEffH2O": {"value": 0.300000}, 
       "log.final.Earth.RocheRadius": {"value": 1.496558e+09, "unit": u.m}, 
       "log.final.Earth.BondiRadius": {"value": 1.014863e+07, "unit": u.m}, 
       "log.final.Earth.HEscapeRegime": {"value": 8.000000}, 
       "log.final.Earth.RRCriticalFlux": {"value": 53.023382, "unit": u.W / u.m ** 2}, 
       "log.final.Earth.KTide": {"value": 0.993607}, 
       "log.final.Earth.RGDuration": {"value": 0.00000e+00, "unit": u.yr}, 
       "log.final.Earth.WaterMassMOAtm": {"value": 4.892788, "unit": u.TO}, 
       "log.final.Earth.PotTemp": {"value": 2173.620200, "unit": u.K}, 
       "log.final.Earth.SurfTemp": {"value": 4000.000000, "unit": u.K}, 
       "log.final.Earth.WaterMassSol": {"value": 0.101555, "unit": u.TO}, 
       "log.final.Earth.SolidRadius": {"value": 0.919480, "unit": u.Rearth}, 
       "log.final.Earth.OxygenMassMOAtm": {"value": 1.836758e+18, "unit": u.kg}, 
       "log.final.Earth.OxygenMassSol": {"value": 8.739505e+17, "unit": u.kg}, 
       "log.final.Earth.PressWaterAtm": {"value": 3.567104e+07}, 
       "log.final.Earth.PressOxygenAtm": {"value": 0.000000}, 
       "log.final.Earth.HydrogenMassSpace": {"value": 8.798414e+17, "unit": u.kg}, 
       "log.final.Earth.OxygenMassSpace": {"value": 4.272139e+18, "unit": u.kg}, 
       "log.final.Earth.FracFe2O3Man": {"value": 1.894182e-05}, 
       "log.final.Earth.NetFluxAtmo": {"value": 815.884123}, 
       "log.final.Earth.WaterFracMelt": {"value": 0.013344}, 
       "log.final.Earth.RadioPower": {"value": 9.823253e+13, "unit": u.W}, 
       "log.final.Earth.TidalPower": {"value": 0.000000, "unit": u.W}, 
       "log.final.Earth.HZInnerEdge": {"value": 2.116533e+11, "unit": u.m}, 
       "log.final.Earth.MeltFraction": {"value": 0.376273}, 
       "log.final.Earth.CO2MassMOAtm": {"value": 1.753694e-296, "unit": u.kg}, 
       "log.final.Earth.CO2MassSol": {"value": 1.753694e-296, "unit": u.kg}, 
       "log.final.Earth.PressCO2Atm": {"value": 0.000000}, 
       "log.final.Earth.CO2FracMelt": {"value": 0.000000}, 
   } 
)
class TestMagmOc_Earth(Benchmark): 
   pass 
