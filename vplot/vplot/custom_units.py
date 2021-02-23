# -*- coding: utf-8 -*-
import astropy.units as u

# Aliases
custom_units = [
    u.def_unit("sec", u.second),  # Alias for second
    u.def_unit("years", u.year),  # Alias for year
    u.def_unit("days",u.day),
    u.def_unit("bars", u.bar),  # Alias for bar
    u.def_unit("Degrees",u.degree), #Alias for Degrees
    u.def_unit("LSUN",u.Lsun), #Alias for L_sun
    u.def_unit("ergs",u.erg), #Alias for erg
    u.def_unit("TO", 1.39e21 * u.kg),  # Terrestrial ocean
    u.def_unit("F/F_Earth", u.Unit("")),  # TODO: Unit in Binary
]

# Register the units
u.add_enabled_units(custom_units)
