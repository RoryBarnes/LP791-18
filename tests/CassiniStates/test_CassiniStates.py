import astropy.units as u
import pytest
from benchmark import Benchmark, benchmark


@benchmark(
    {
        "log.initial.system.Age": {"value": 0.000000, "unit": u.sec},
        "log.initial.system.Time": {"value": 0.000000, "unit": u.sec},
        "log.initial.system.TotAngMom": {
            "value": 9.638821e41,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.initial.system.TotEnergy": {"value": -2.276496e41, "unit": u.Joule},
        "log.initial.system.PotEnergy": {"value": -2.276504e41, "unit": u.Joule},
        "log.initial.system.KinEnergy": {"value": 1.103902e36, "unit": u.Joule},
        "log.initial.system.DeltaTime": {"value": 0.000000, "unit": u.sec},
        "log.initial.star.Mass": {"value": 1.988416e30, "unit": u.kg},
        "log.initial.star.Obliquity": {"value": 0.000000, "unit": u.rad},
        "log.initial.star.PrecA": {"value": 0.000000, "unit": u.rad},
        "log.initial.star.Xobl": {"value": 0.000000},
        "log.initial.star.Yobl": {"value": 0.000000},
        "log.initial.star.Zobl": {"value": 1.000000},
        "log.initial.star.Radius": {"value": 6.955074e08, "unit": u.m},
        "log.initial.star.RadGyra": {"value": 0.500000},
        "log.initial.star.RotAngMom": {
            "value": 7.286277e41,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.initial.star.RotKinEnergy": {"value": 1.103902e36, "unit": u.Joule},
        "log.initial.star.RotVel": {"value": 2107.446979, "unit": u.m / u.sec},
        "log.initial.star.BodyType": {"value": 0.000000},
        "log.initial.star.RotRate": {"value": 3.030086e-06, "unit": 1 / u.sec},
        "log.initial.star.RotPer": {"value": 24.000000, "unit": u.day},
        "log.initial.star.Density": {"value": 1410.955514, "unit": u.kg / u.m ** 3},
        "log.initial.star.SurfEnFluxTotal": {
            "value": 1.056036e-09,
            "unit": u.kg / u.sec ** 3,
        },
        "log.initial.star.TidalQ": {"value": 1.000000e06},
        "log.initial.star.ImK2": {"value": -2.990000e-07},
        "log.initial.star.K2": {"value": 0.299000},
        "log.initial.star.K2Man": {"value": 0.010000},
        "log.initial.star.Imk2Man": {"value": 0.000000},
        "log.initial.star.TidalQMantle": {"value": 100.000000},
        "log.initial.star.HEcc": {"value": 0.000000},
        "log.initial.star.HZLimitDryRunaway": {"value": -1.000000, "unit": u.m},
        "log.initial.star.HZLimRecVenus": {"value": -1.000000},
        "log.initial.star.HZLimRunaway": {"value": -1.000000},
        "log.initial.star.HZLimMoistGreenhouse": {"value": -1.000000},
        "log.initial.star.HZLimMaxGreenhouse": {"value": -1.000000},
        "log.initial.star.HZLimEarlyMars": {"value": -1.000000},
        "log.initial.star.Instellation": {
            "value": -1.000000,
            "unit": u.kg / u.sec ** 3,
        },
        "log.initial.star.KEcc": {"value": 0.000000},
        "log.initial.star.Eccentricity": {"value": -1.000000},
        "log.initial.star.OrbEnergy": {"value": 0.000000, "unit": u.Joule},
        "log.initial.star.MeanMotion": {"value": -1.000000, "unit": 1 / u.sec},
        "log.initial.star.OrbPeriod": {"value": -1.000000, "unit": u.sec},
        "log.initial.star.SemiMajorAxis": {"value": -1.000000, "unit": u.m},
        "log.initial.star.CriticalSemiMajorAxis": {"value": -1.000000, "unit": u.m},
        "log.initial.star.COPP": {"value": 0.000000},
        "log.initial.star.OrbAngMom": {
            "value": 0.000000,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.initial.star.LongP": {"value": 0.000000, "unit": u.rad},
        "log.initial.star.TotOrbEnergy": {"value": -2.334935e35, "unit": u.Joule},
        "log.initial.star.OrbPotEnergy": {"value": -1.000000, "unit": u.Joule},
        "log.initial.star.LostEnergy": {"value": 5.562685e-309, "unit": u.Joule},
        "log.initial.star.LockTime": {"value": -1.000000, "unit": u.sec},
        "log.initial.star.BodyDsemiDtEqtide": {"value": -1.000000},
        "log.initial.star.BodyDeccDt": {"value": -1.000000},
        "log.initial.star.DOblDtEqtide": {"value": 0.000000, "unit": u.rad / u.sec},
        "log.initial.star.DRotPerDtEqtide": {"value": -1.176748e-20},
        "log.initial.star.DRotRateDtEqtide": {
            "value": 1.719545e-32,
            "unit": 1 / u.sec ** 2,
        },
        "log.initial.star.EqRotRateDiscrete": {
            "value": 4.505089e-06,
            "unit": 1 / u.sec,
        },
        "log.initial.star.EqRotPerDiscrete": {"value": 1.394686e06, "unit": u.sec},
        "log.initial.star.EqRotRateCont": {"value": 4.612085e-06, "unit": 1 / u.sec},
        "log.initial.star.EqRotPerCont": {"value": 1.362331e06, "unit": u.sec},
        "log.initial.star.EqRotPer": {"value": 1.394686e06, "unit": u.sec},
        "log.initial.star.EqTidePower": {"value": 0.000000, "unit": 1 / u.sec},
        "log.initial.star.GammaRot": {"value": -1.000000, "unit": u.sec},
        "log.initial.star.GammaOrb": {"value": -1.000000, "unit": u.sec},
        "log.initial.star.OceanK2": {"value": 0.010000},
        "log.initial.star.EnvTidalQ": {"value": -1.000000},
        "log.initial.star.OceanTidalQ": {"value": -1.000000},
        "log.initial.star.TideLock": {"value": 0.000000},
        "log.initial.star.RotTimeEqtide": {"value": 1.762144e26, "unit": u.sec},
        "log.initial.star.EnvK2": {"value": 0.010000},
        "log.initial.star.OblTimeEqtide": {"value": -1.000000},
        "log.initial.star.PowerEqtide": {"value": 6.419365e09, "unit": u.W},
        "log.initial.star.SurfEnFluxEqtide": {
            "value": 1.056036e-09,
            "unit": u.kg / u.sec ** 3,
        },
        "log.initial.b.Mass": {"value": 5.972186e24, "unit": u.kg},
        "log.initial.b.Obliquity": {"value": 0.785398, "unit": u.rad},
        "log.initial.b.PrecA": {"value": 0.000000, "unit": u.rad},
        "log.initial.b.Xobl": {"value": 0.707107},
        "log.initial.b.Yobl": {"value": 0.000000},
        "log.initial.b.Zobl": {"value": 0.707107},
        "log.initial.b.Radius": {"value": 6.378100e06, "unit": u.m},
        "log.initial.b.RadGyra": {"value": 0.500000},
        "log.initial.b.RotAngMom": {
            "value": 4.416946e33,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.initial.b.RotKinEnergy": {"value": 1.606047e29, "unit": u.Joule},
        "log.initial.b.RotVel": {"value": 463.828521, "unit": u.m / u.sec},
        "log.initial.b.BodyType": {"value": 0.000000},
        "log.initial.b.RotRate": {"value": 7.272205e-05, "unit": 1 / u.sec},
        "log.initial.b.RotPer": {"value": 1.000000, "unit": u.day},
        "log.initial.b.Density": {"value": 5495.038549, "unit": u.kg / u.m ** 3},
        "log.initial.b.SurfEnFluxTotal": {
            "value": 39.817440,
            "unit": u.kg / u.sec ** 3,
        },
        "log.initial.b.TidalQ": {"value": 100.000000},
        "log.initial.b.ImK2": {"value": -0.003000},
        "log.initial.b.K2": {"value": 0.300000},
        "log.initial.b.K2Man": {"value": 0.010000},
        "log.initial.b.Imk2Man": {"value": 0.000000},
        "log.initial.b.TidalQMantle": {"value": 100.000000},
        "log.initial.b.HEcc": {"value": -0.049998},
        "log.initial.b.HZLimitDryRunaway": {"value": -1.000000, "unit": u.m},
        "log.initial.b.HZLimRecVenus": {"value": -1.000000},
        "log.initial.b.HZLimRunaway": {"value": -1.000000},
        "log.initial.b.HZLimMoistGreenhouse": {"value": -1.000000},
        "log.initial.b.HZLimMaxGreenhouse": {"value": -1.000000},
        "log.initial.b.HZLimEarlyMars": {"value": -1.000000},
        "log.initial.b.Instellation": {"value": -1.000000, "unit": u.kg / u.sec ** 3},
        "log.initial.b.KEcc": {"value": -0.000394},
        "log.initial.b.Eccentricity": {"value": 0.050000},
        "log.initial.b.OrbEnergy": {"value": -2.119237e34, "unit": u.Joule},
        "log.initial.b.MeanMotion": {"value": 4.505089e-06, "unit": 1 / u.sec},
        "log.initial.b.OrbPeriod": {"value": 1.394686e06, "unit": u.sec},
        "log.initial.b.SemiMajorAxis": {"value": 1.869973e10, "unit": u.m},
        "log.initial.b.CriticalSemiMajorAxis": {"value": -1.000000, "unit": u.m},
        "log.initial.b.COPP": {"value": -0.035354},
        "log.initial.b.OrbAngMom": {
            "value": 9.396425e39,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.initial.b.ArgP": {"value": 4.343614, "unit": u.rad},
        "log.initial.b.Inc": {"value": 0.008727, "unit": u.rad},
        "log.initial.b.LongA": {"value": 0.360890, "unit": u.rad},
        "log.initial.b.MeanLongitude": {"value": -1.578681, "unit": u.rad},
        "log.initial.b.LongP": {"value": 4.704504, "unit": u.rad},
        "log.initial.b.TotOrbEnergy": {"value": -2.334935e35, "unit": u.Joule},
        "log.initial.b.OrbPotEnergy": {"value": -4.238474e34, "unit": u.Joule},
        "log.initial.b.LostEnergy": {"value": 5.562685e-309, "unit": u.Joule},
        "log.initial.b.TidalRadius": {"value": 6.378100e06, "unit": u.m},
        "log.initial.b.DsemiDtEqtide": {"value": 1.202419e-09, "unit": u.m / u.sec},
        "log.initial.b.DeccDtEqtide": {"value": 7.399880e-21, "unit": 1 / u.sec},
        "log.initial.b.DMeanMotionDtEqtide": {
            "value": -4.345252e-25,
            "unit": 1 / u.sec ** 2,
        },
        "log.initial.b.DOrbPerDtEqtide": {"value": 1.345204e-13},
        "log.initial.b.EccTimeEqtide": {"value": 6.756867e18, "unit": u.sec},
        "log.initial.b.SemiTimeEqtide": {"value": 1.555176e19, "unit": u.sec},
        "log.initial.b.DHEccDtEqtide": {"value": -7.399650e-21, "unit": 1 / u.sec},
        "log.initial.b.DKEccDtEqtide": {"value": -5.834380e-23, "unit": 1 / u.sec},
        "log.initial.b.DXoblDtEqtide": {"value": 1.659179e-14, "unit": 1 / u.sec},
        "log.initial.b.DYoblDtEqtide": {"value": 0.000000, "unit": 1 / u.sec},
        "log.initial.b.DZoblDtEqtide": {"value": -1.659179e-14, "unit": 1 / u.sec},
        "log.initial.b.LockTime": {"value": -1.000000, "unit": u.sec},
        "log.initial.b.BodyDsemiDtEqtide": {"value": -1.000000},
        "log.initial.b.BodyDeccDt": {"value": -1.000000},
        "log.initial.b.DOblDtEqtide": {"value": 2.346433e-14, "unit": u.rad / u.sec},
        "log.initial.b.DRotPerDtEqtide": {"value": 5.841640e-09},
        "log.initial.b.DRotRateDtEqtide": {
            "value": -4.916852e-18,
            "unit": 1 / u.sec ** 2,
        },
        "log.initial.b.EqRotRateDiscrete": {"value": 4.505089e-06, "unit": 1 / u.sec},
        "log.initial.b.EqRotPerDiscrete": {"value": 1.394686e06, "unit": u.sec},
        "log.initial.b.EqRotRateCont": {"value": 4.612085e-06, "unit": 1 / u.sec},
        "log.initial.b.EqRotPerCont": {"value": 1.362331e06, "unit": u.sec},
        "log.initial.b.EqRotPer": {"value": 1.394686e06, "unit": u.sec},
        "log.initial.b.EqTidePower": {"value": 0.000000, "unit": 1 / u.sec},
        "log.initial.b.GammaRot": {"value": -1.000000, "unit": u.sec},
        "log.initial.b.GammaOrb": {"value": -1.000000, "unit": u.sec},
        "log.initial.b.OceanK2": {"value": 0.010000},
        "log.initial.b.EnvTidalQ": {"value": -1.000000},
        "log.initial.b.OceanTidalQ": {"value": -1.000000},
        "log.initial.b.TideLock": {"value": 0.000000},
        "log.initial.b.RotTimeEqtide": {"value": 1.479037e13, "unit": u.sec},
        "log.initial.b.EnvK2": {"value": 0.010000},
        "log.initial.b.OblTimeEqtide": {"value": -1.000000},
        "log.initial.b.PowerEqtide": {"value": 2.035475e16, "unit": u.W},
        "log.initial.b.SurfEnFluxEqtide": {"value": 39.817440, "unit": u.W / u.m ** 2},
        "log.initial.b.Sinc": {"value": 0.004363},
        "log.initial.b.Pinc": {"value": 0.001541},
        "log.initial.b.Qinc": {"value": 0.004082},
        "log.initial.b.DIncDtDistOrb": {"value": -9.038837e-15, "unit": u.rad / u.sec},
        "log.initial.b.DSincDtDistOrb": {"value": -4.519375e-15, "unit": 1 / u.sec},
        "log.initial.b.DLongADtDistOrb": {
            "value": -6.663476e-11,
            "unit": u.rad / u.sec,
        },
        "log.initial.b.DLongPDtDistOrb": {"value": 6.124653e-11, "unit": u.rad / u.sec},
        "log.initial.b.DHeccDtDistOrb": {"value": -4.476935e-12, "unit": 1 / u.sec},
        "log.initial.b.DKeccDtDistOrb": {"value": 3.027122e-12, "unit": 1 / u.sec},
        "log.initial.b.DPincDtDistOrb": {"value": -2.736148e-13, "unit": 1 / u.sec},
        "log.initial.b.DQincDtDistOrb": {"value": 9.843699e-14, "unit": 1 / u.sec},
        "log.initial.b.CassiniOne": {"value": 0.353129},
        "log.initial.b.CassiniTwo": {"value": 0.935575},
        "log.initial.b.DOblDtDistRot": {"value": 1.968719e-13, "unit": u.rad},
        "log.initial.b.DPrecADtDistRot": {"value": 9.753394e-10, "unit": u.rad / u.sec},
        "log.initial.b.DXoblDtDistRot": {"value": 1.392095e-13, "unit": 1 / u.sec},
        "log.initial.b.DYoblDtDistRot": {"value": 6.896691e-10, "unit": 1 / u.sec},
        "log.initial.b.DZoblDtDistRot": {"value": -1.392095e-13, "unit": 1 / u.sec},
        "log.initial.b.OblTimeDistRot": {"value": 1.595754e13, "unit": u.rad},
        "log.initial.b.PrecATimeDistRot": {"value": 6.442050e09, "unit": u.sec},
        "log.initial.b.XoblTimeDistRot": {"value": 7.183418e12, "unit": 1 / u.sec},
        "log.initial.b.YoblTimeDistRot": {"value": 1.449971e09, "unit": 1 / u.sec},
        "log.initial.b.ZoblTimeDistRot": {"value": 7.183418e12, "unit": 1 / u.sec},
        "log.initial.b.DynEllip": {"value": 0.003281},
        "log.initial.b.PrecFNat": {"value": 9.747897e-10, "unit": u.rad / u.sec},
        "log.initial.c.Mass": {"value": 1.074993e26, "unit": u.kg},
        "log.initial.c.Radius": {"value": 9.567150e06, "unit": u.m},
        "log.initial.c.RadGyra": {"value": 0.500000},
        "log.initial.c.RotKinEnergy": {"value": 6.504490e30, "unit": u.Joule},
        "log.initial.c.RotVel": {"value": 695.742781, "unit": u.m / u.sec},
        "log.initial.c.BodyType": {"value": 0.000000},
        "log.initial.c.Density": {"value": 2.930687e04, "unit": u.kg / u.m ** 3},
        "log.initial.c.HEcc": {"value": -0.005734},
        "log.initial.c.HZLimitDryRunaway": {"value": -1.000000, "unit": u.m},
        "log.initial.c.HZLimRecVenus": {"value": -1.000000},
        "log.initial.c.HZLimRunaway": {"value": -1.000000},
        "log.initial.c.HZLimMoistGreenhouse": {"value": -1.000000},
        "log.initial.c.HZLimMaxGreenhouse": {"value": -1.000000},
        "log.initial.c.HZLimEarlyMars": {"value": -1.000000},
        "log.initial.c.Instellation": {"value": -1.000000, "unit": u.kg / u.sec ** 3},
        "log.initial.c.KEcc": {"value": 0.099835},
        "log.initial.c.Eccentricity": {"value": 0.100000},
        "log.initial.c.OrbEnergy": {"value": -2.123011e35, "unit": u.Joule},
        "log.initial.c.MeanMotion": {"value": 1.870531e-06, "unit": 1 / u.sec},
        "log.initial.c.OrbPeriod": {"value": 3.359039e06, "unit": u.sec},
        "log.initial.c.SemiMajorAxis": {"value": 3.359968e10, "unit": u.m},
        "log.initial.c.OrbAngMom": {
            "value": 2.258578e41,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.initial.c.ArgP": {"value": 5.876750, "unit": u.rad},
        "log.initial.c.Inc": {"value": 1.745329e-05, "unit": u.rad},
        "log.initial.c.LongA": {"value": 0.349066, "unit": u.rad},
        "log.initial.c.MeanLongitude": {"value": -0.057370, "unit": u.rad},
        "log.initial.c.LongP": {"value": 6.225816, "unit": u.rad},
        "log.initial.c.TotOrbEnergy": {"value": -2.334935e35, "unit": u.Joule},
        "log.initial.c.OrbPotEnergy": {"value": -4.246023e35, "unit": u.Joule},
        "log.initial.c.Sinc": {"value": 8.726646e-06},
        "log.initial.c.Pinc": {"value": 2.984689e-06},
        "log.initial.c.Qinc": {"value": 8.200365e-06},
        "log.initial.c.DIncDtDistOrb": {"value": 1.686400e-16, "unit": u.rad / u.sec},
        "log.initial.c.DSincDtDistOrb": {"value": 8.432000e-17, "unit": 1 / u.sec},
        "log.initial.c.DLongADtDistOrb": {"value": 1.386236e-09, "unit": u.rad / u.sec},
        "log.initial.c.DLongPDtDistOrb": {"value": 2.729235e-12, "unit": u.rad / u.sec},
        "log.initial.c.DHeccDtDistOrb": {"value": 2.777433e-13, "unit": 1 / u.sec},
        "log.initial.c.DKeccDtDistOrb": {"value": -7.609099e-14, "unit": 1 / u.sec},
        "log.initial.c.DPincDtDistOrb": {"value": 1.139648e-14, "unit": 1 / u.sec},
        "log.initial.c.DQincDtDistOrb": {"value": -4.058248e-15, "unit": 1 / u.sec},
        "log.final.system.Age": {"value": 3.155760e09, "unit": u.sec},
        "log.final.system.Time": {"value": 3.155760e09, "unit": u.sec},
        "log.final.system.TotAngMom": {
            "value": 9.638821e41,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.final.system.TotEnergy": {"value": -2.276496e41, "unit": u.Joule},
        "log.final.system.PotEnergy": {"value": -2.276504e41, "unit": u.Joule},
        "log.final.system.KinEnergy": {"value": 1.103902e36, "unit": u.Joule},
        "log.final.system.DeltaTime": {"value": 1.139264e07, "unit": u.sec},
        "log.final.star.Mass": {"value": 1.988416e30, "unit": u.kg},
        "log.final.star.Obliquity": {"value": 0.000000, "unit": u.rad},
        "log.final.star.PrecA": {"value": 0.000000, "unit": u.rad},
        "log.final.star.Xobl": {"value": 0.000000},
        "log.final.star.Yobl": {"value": 0.000000},
        "log.final.star.Zobl": {"value": 1.000000},
        "log.final.star.Radius": {"value": 6.955074e08, "unit": u.m},
        "log.final.star.RadGyra": {"value": 0.500000},
        "log.final.star.RotAngMom": {
            "value": 7.286277e41,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.final.star.RotKinEnergy": {"value": 1.103902e36, "unit": u.Joule},
        "log.final.star.RotVel": {"value": 2107.446979, "unit": u.m / u.sec},
        "log.final.star.BodyType": {"value": 0.000000},
        "log.final.star.RotRate": {"value": 3.030086e-06, "unit": 1 / u.sec},
        "log.final.star.RotPer": {"value": 24.000000, "unit": u.day},
        "log.final.star.Density": {"value": 1410.955514, "unit": u.kg / u.m ** 3},
        "log.final.star.SurfEnFluxTotal": {
            "value": 1.100249e-09,
            "unit": u.kg / u.sec ** 3,
        },
        "log.final.star.TidalQ": {"value": 1.000000e06},
        "log.final.star.ImK2": {"value": -2.990000e-07},
        "log.final.star.K2": {"value": 0.299000},
        "log.final.star.K2Man": {"value": 0.010000},
        "log.final.star.Imk2Man": {"value": 0.000000},
        "log.final.star.TidalQMantle": {"value": 100.000000},
        "log.final.star.HEcc": {"value": 0.000000},
        "log.final.star.HZLimitDryRunaway": {"value": -1.000000, "unit": u.m},
        "log.final.star.HZLimRecVenus": {"value": -1.000000},
        "log.final.star.HZLimRunaway": {"value": -1.000000},
        "log.final.star.HZLimMoistGreenhouse": {"value": -1.000000},
        "log.final.star.HZLimMaxGreenhouse": {"value": -1.000000},
        "log.final.star.HZLimEarlyMars": {"value": -1.000000},
        "log.final.star.Instellation": {"value": -1.000000, "unit": u.kg / u.sec ** 3},
        "log.final.star.KEcc": {"value": 0.000000},
        "log.final.star.Eccentricity": {"value": -1.000000},
        "log.final.star.OrbEnergy": {"value": 0.000000, "unit": u.Joule},
        "log.final.star.MeanMotion": {"value": -1.000000, "unit": 1 / u.sec},
        "log.final.star.OrbPeriod": {"value": -1.000000, "unit": u.sec},
        "log.final.star.SemiMajorAxis": {"value": -1.000000, "unit": u.m},
        "log.final.star.CriticalSemiMajorAxis": {"value": -1.000000, "unit": u.m},
        "log.final.star.COPP": {"value": 0.000000},
        "log.final.star.OrbAngMom": {
            "value": 0.000000,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.final.star.LongP": {"value": 0.000000, "unit": u.rad},
        "log.final.star.TotOrbEnergy": {"value": -2.334935e35, "unit": u.Joule},
        "log.final.star.OrbPotEnergy": {"value": -1.000000, "unit": u.Joule},
        "log.final.star.LostEnergy": {"value": 2.066697e19, "unit": u.Joule},
        "log.final.star.LockTime": {"value": -1.000000, "unit": u.sec},
        "log.final.star.BodyDsemiDtEqtide": {"value": -1.000000},
        "log.final.star.BodyDeccDt": {"value": -1.000000},
        "log.final.star.DOblDtEqtide": {"value": 0.000000, "unit": u.rad / u.sec},
        "log.final.star.DRotPerDtEqtide": {"value": -1.189539e-20},
        "log.final.star.DRotRateDtEqtide": {
            "value": 1.738235e-32,
            "unit": 1 / u.sec ** 2,
        },
        "log.final.star.EqRotRateDiscrete": {"value": 4.505089e-06, "unit": 1 / u.sec},
        "log.final.star.EqRotPerDiscrete": {"value": 1.394686e06, "unit": u.sec},
        "log.final.star.EqRotRateCont": {"value": 4.679702e-06, "unit": 1 / u.sec},
        "log.final.star.EqRotPerCont": {"value": 1.342646e06, "unit": u.sec},
        "log.final.star.EqRotPer": {"value": 1.394686e06, "unit": u.sec},
        "log.final.star.EqTidePower": {"value": 0.000000, "unit": 1 / u.sec},
        "log.final.star.GammaRot": {"value": -1.000000, "unit": u.sec},
        "log.final.star.GammaOrb": {"value": -1.000000, "unit": u.sec},
        "log.final.star.OceanK2": {"value": 0.010000},
        "log.final.star.EnvTidalQ": {"value": -1.000000},
        "log.final.star.OceanTidalQ": {"value": -1.000000},
        "log.final.star.TideLock": {"value": 0.000000},
        "log.final.star.RotTimeEqtide": {"value": 1.743197e26, "unit": u.sec},
        "log.final.star.EnvK2": {"value": 0.010000},
        "log.final.star.OblTimeEqtide": {"value": -1.000000},
        "log.final.star.PowerEqtide": {"value": 6.688128e09, "unit": u.W},
        "log.final.star.SurfEnFluxEqtide": {
            "value": 1.100249e-09,
            "unit": u.kg / u.sec ** 3,
        },
        "log.final.b.Mass": {"value": 5.972186e24, "unit": u.kg},
        "log.final.b.Obliquity": {"value": 0.786730, "unit": u.rad},
        "log.final.b.PrecA": {"value": 3.075200, "unit": u.rad},
        "log.final.b.Xobl": {"value": -0.706488},
        "log.final.b.Yobl": {"value": 0.046974},
        "log.final.b.Zobl": {"value": 0.706164},
        "log.final.b.Radius": {"value": 6.378100e06, "unit": u.m},
        "log.final.b.RadGyra": {"value": 0.500000},
        "log.final.b.RotAngMom": {
            "value": 4.415998e33,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.final.b.RotKinEnergy": {"value": 1.605358e29, "unit": u.Joule},
        "log.final.b.RotVel": {"value": 463.729001, "unit": u.m / u.sec},
        "log.final.b.BodyType": {"value": 0.000000},
        "log.final.b.RotRate": {"value": 7.270645e-05, "unit": 1 / u.sec},
        "log.final.b.RotPer": {"value": 1.000215, "unit": u.day},
        "log.final.b.Density": {"value": 5495.038549, "unit": u.kg / u.m ** 3},
        "log.final.b.SurfEnFluxTotal": {"value": 40.250313, "unit": u.kg / u.sec ** 3},
        "log.final.b.TidalQ": {"value": 100.000000},
        "log.final.b.ImK2": {"value": -0.003000},
        "log.final.b.K2": {"value": 0.300000},
        "log.final.b.K2Man": {"value": 0.010000},
        "log.final.b.Imk2Man": {"value": 0.000000},
        "log.final.b.TidalQMantle": {"value": 100.000000},
        "log.final.b.HEcc": {"value": -0.062959},
        "log.final.b.HZLimitDryRunaway": {"value": -1.000000, "unit": u.m},
        "log.final.b.HZLimRecVenus": {"value": -1.000000},
        "log.final.b.HZLimRunaway": {"value": -1.000000},
        "log.final.b.HZLimMoistGreenhouse": {"value": -1.000000},
        "log.final.b.HZLimMaxGreenhouse": {"value": -1.000000},
        "log.final.b.HZLimEarlyMars": {"value": -1.000000},
        "log.final.b.Instellation": {"value": -1.000000, "unit": u.kg / u.sec ** 3},
        "log.final.b.KEcc": {"value": 0.010774},
        "log.final.b.Eccentricity": {"value": 0.063874},
        "log.final.b.OrbEnergy": {"value": -2.119237e34, "unit": u.Joule},
        "log.final.b.MeanMotion": {"value": 4.505089e-06, "unit": 1 / u.sec},
        "log.final.b.OrbPeriod": {"value": 1.394686e06, "unit": u.sec},
        "log.final.b.SemiMajorAxis": {"value": 1.869973e10, "unit": u.m},
        "log.final.b.CriticalSemiMajorAxis": {"value": -1.000000, "unit": u.m},
        "log.final.b.COPP": {"value": 0.044986},
        "log.final.b.OrbAngMom": {
            "value": 9.388981e39,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.final.b.ArgP": {"value": 4.733145, "unit": u.rad},
        "log.final.b.Inc": {"value": 0.008680, "unit": u.rad},
        "log.final.b.LongA": {"value": 0.148731, "unit": u.rad},
        "log.final.b.MeanLongitude": {"value": -1.401309, "unit": u.rad},
        "log.final.b.LongP": {"value": 4.881877, "unit": u.rad},
        "log.final.b.TotOrbEnergy": {"value": -2.334935e35, "unit": u.Joule},
        "log.final.b.OrbPotEnergy": {"value": -4.238474e34, "unit": u.Joule},
        "log.final.b.LostEnergy": {"value": 6.457124e25, "unit": u.Joule},
        "log.final.b.TidalRadius": {"value": 6.378100e06, "unit": u.m},
        "log.final.b.DsemiDtEqtide": {"value": 1.225892e-09, "unit": u.m / u.sec},
        "log.final.b.DeccDtEqtide": {"value": 9.453231e-21, "unit": 1 / u.sec},
        "log.final.b.DMeanMotionDtEqtide": {
            "value": -4.430078e-25,
            "unit": 1 / u.sec ** 2,
        },
        "log.final.b.DOrbPerDtEqtide": {"value": 1.371464e-13},
        "log.final.b.EccTimeEqtide": {"value": 6.756867e18, "unit": u.sec},
        "log.final.b.SemiTimeEqtide": {"value": 1.525398e19, "unit": u.sec},
        "log.final.b.DHEccDtEqtide": {"value": -9.317779e-21, "unit": 1 / u.sec},
        "log.final.b.DKEccDtEqtide": {"value": 1.594545e-21, "unit": 1 / u.sec},
        "log.final.b.DXoblDtEqtide": {"value": -1.655873e-14, "unit": 1 / u.sec},
        "log.final.b.DYoblDtEqtide": {"value": 1.100989e-15, "unit": 1 / u.sec},
        "log.final.b.DZoblDtEqtide": {"value": -1.663957e-14, "unit": 1 / u.sec},
        "log.final.b.LockTime": {"value": -1.000000, "unit": u.sec},
        "log.final.b.BodyDsemiDtEqtide": {"value": -1.000000},
        "log.final.b.BodyDeccDt": {"value": -1.000000},
        "log.final.b.DOblDtEqtide": {"value": 2.350061e-14, "unit": u.rad / u.sec},
        "log.final.b.DRotPerDtEqtide": {"value": 5.912122e-09},
        "log.final.b.DRotRateDtEqtide": {
            "value": -4.974041e-18,
            "unit": 1 / u.sec ** 2,
        },
        "log.final.b.EqRotRateDiscrete": {"value": 4.505089e-06, "unit": 1 / u.sec},
        "log.final.b.EqRotPerDiscrete": {"value": 1.394686e06, "unit": u.sec},
        "log.final.b.EqRotRateCont": {"value": 4.679702e-06, "unit": 1 / u.sec},
        "log.final.b.EqRotPerCont": {"value": 1.342646e06, "unit": u.sec},
        "log.final.b.EqRotPer": {"value": 1.394686e06, "unit": u.sec},
        "log.final.b.EqTidePower": {"value": 0.000000, "unit": 1 / u.sec},
        "log.final.b.GammaRot": {"value": -1.000000, "unit": u.sec},
        "log.final.b.GammaOrb": {"value": -1.000000, "unit": u.sec},
        "log.final.b.OceanK2": {"value": 0.010000},
        "log.final.b.EnvTidalQ": {"value": -1.000000},
        "log.final.b.OceanTidalQ": {"value": -1.000000},
        "log.final.b.TideLock": {"value": 0.000000},
        "log.final.b.RotTimeEqtide": {"value": 1.461718e13, "unit": u.sec},
        "log.final.b.EnvK2": {"value": 0.010000},
        "log.final.b.OblTimeEqtide": {"value": -1.000000},
        "log.final.b.PowerEqtide": {"value": 2.057604e16, "unit": u.W},
        "log.final.b.SurfEnFluxEqtide": {"value": 40.250313, "unit": u.W / u.m ** 2},
        "log.final.b.Sinc": {"value": 0.004340},
        "log.final.b.Pinc": {"value": 0.000643},
        "log.final.b.Qinc": {"value": 0.004292},
        "log.final.b.DIncDtDistOrb": {"value": -1.870539e-14, "unit": u.rad / u.sec},
        "log.final.b.DSincDtDistOrb": {"value": -9.352606e-15, "unit": 1 / u.sec},
        "log.final.b.DLongADtDistOrb": {"value": -6.794098e-11, "unit": u.rad / u.sec},
        "log.final.b.DLongPDtDistOrb": {"value": 5.038333e-11, "unit": u.rad / u.sec},
        "log.final.b.DHeccDtDistOrb": {"value": -3.716526e-12, "unit": 1 / u.sec},
        "log.final.b.DKeccDtDistOrb": {"value": 3.900985e-12, "unit": 1 / u.sec},
        "log.final.b.DPincDtDistOrb": {"value": -2.929948e-13, "unit": 1 / u.sec},
        "log.final.b.DQincDtDistOrb": {"value": 3.444461e-14, "unit": 1 / u.sec},
        "log.final.b.CassiniOne": {"value": 0.073055},
        "log.final.b.CassiniTwo": {"value": -0.997328},
        "log.final.b.DOblDtDistRot": {"value": -2.986025e-14, "unit": u.rad},
        "log.final.b.DPrecADtDistRot": {"value": 9.750131e-10, "unit": u.rad / u.sec},
        "log.final.b.DXoblDtDistRot": {"value": -4.577958e-11, "unit": 1 / u.sec},
        "log.final.b.DYoblDtDistRot": {"value": -6.888367e-10, "unit": 1 / u.sec},
        "log.final.b.DZoblDtDistRot": {"value": 2.114249e-14, "unit": 1 / u.sec},
        "log.final.b.OblTimeDistRot": {"value": 1.052099e14, "unit": u.rad},
        "log.final.b.PrecATimeDistRot": {"value": 6.444206e09, "unit": u.sec},
        "log.final.b.XoblTimeDistRot": {"value": 2.184380e10, "unit": 1 / u.sec},
        "log.final.b.YoblTimeDistRot": {"value": 1.451723e09, "unit": 1 / u.sec},
        "log.final.b.ZoblTimeDistRot": {"value": 4.729811e13, "unit": 1 / u.sec},
        "log.final.b.DynEllip": {"value": 0.003279},
        "log.final.b.PrecFNat": {"value": 9.755983e-10, "unit": u.rad / u.sec},
        "log.final.c.Mass": {"value": 1.074993e26, "unit": u.kg},
        "log.final.c.Radius": {"value": 9.567150e06, "unit": u.m},
        "log.final.c.RadGyra": {"value": 0.500000},
        "log.final.c.RotKinEnergy": {"value": 6.504490e30, "unit": u.Joule},
        "log.final.c.RotVel": {"value": 695.742781, "unit": u.m / u.sec},
        "log.final.c.BodyType": {"value": 0.000000},
        "log.final.c.Density": {"value": 2.930687e04, "unit": u.kg / u.m ** 3},
        "log.final.c.HEcc": {"value": -0.004891},
        "log.final.c.HZLimitDryRunaway": {"value": -1.000000, "unit": u.m},
        "log.final.c.HZLimRecVenus": {"value": -1.000000},
        "log.final.c.HZLimRunaway": {"value": -1.000000},
        "log.final.c.HZLimMoistGreenhouse": {"value": -1.000000},
        "log.final.c.HZLimMaxGreenhouse": {"value": -1.000000},
        "log.final.c.HZLimEarlyMars": {"value": -1.000000},
        "log.final.c.Instellation": {"value": -1.000000, "unit": u.kg / u.sec ** 3},
        "log.final.c.KEcc": {"value": 0.099553},
        "log.final.c.Eccentricity": {"value": 0.099673},
        "log.final.c.OrbEnergy": {"value": -2.123011e35, "unit": u.Joule},
        "log.final.c.MeanMotion": {"value": 1.870531e-06, "unit": 1 / u.sec},
        "log.final.c.OrbPeriod": {"value": 3.359039e06, "unit": u.sec},
        "log.final.c.SemiMajorAxis": {"value": 3.359968e10, "unit": u.m},
        "log.final.c.OrbAngMom": {
            "value": 2.258652e41,
            "unit": (u.kg * u.m ** 2) / u.sec,
        },
        "log.final.c.ArgP": {"value": 4.653590, "unit": u.rad},
        "log.final.c.Inc": {"value": 8.069275e-05, "unit": u.rad},
        "log.final.c.LongA": {"value": 1.580510, "unit": u.rad},
        "log.final.c.MeanLongitude": {"value": -0.049086, "unit": u.rad},
        "log.final.c.LongP": {"value": 6.234100, "unit": u.rad},
        "log.final.c.TotOrbEnergy": {"value": -2.334935e35, "unit": u.Joule},
        "log.final.c.OrbPotEnergy": {"value": -4.246023e35, "unit": u.Joule},
        "log.final.c.Sinc": {"value": 4.034637e-05},
        "log.final.c.Pinc": {"value": 4.034447e-05},
        "log.final.c.Qinc": {"value": -3.918894e-07},
        "log.final.c.DIncDtDistOrb": {"value": 2.439677e-14, "unit": u.rad / u.sec},
        "log.final.c.DSincDtDistOrb": {"value": 1.219839e-14, "unit": 1 / u.sec},
        "log.final.c.DLongADtDistOrb": {"value": 3.135675e-11, "unit": u.rad / u.sec},
        "log.final.c.DLongPDtDistOrb": {"value": 2.512992e-12, "unit": u.rad / u.sec},
        "log.final.c.DHeccDtDistOrb": {"value": 2.557887e-13, "unit": 1 / u.sec},
        "log.final.c.DKeccDtDistOrb": {"value": -1.019520e-13, "unit": 1 / u.sec},
        "log.final.c.DPincDtDistOrb": {"value": 1.218552e-14, "unit": 1 / u.sec},
        "log.final.c.DQincDtDistOrb": {"value": -1.383556e-15, "unit": 1 / u.sec},
    }
)
class TestCassiniStates(Benchmark):
    pass