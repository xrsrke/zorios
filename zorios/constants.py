# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_constants.ipynb.

# %% auto 0
__all__ = ['GRAVITATIONAL_CONSTANT', 'EARTH_MASS', 'EARTH_RADIUS', 'EARTH_GRAVITY', 'MARS_MASS', 'MARS_RADIUS', 'MARS_GRAVITY',
           'MOON_MASS', 'MOON_RADIUS', 'MOON_GRAVITY']

# %% ../nbs/00_constants.ipynb 4
from fastcore.test import test_eq
from .core import *

# %% ../nbs/00_constants.ipynb 6
GRAVITATIONAL_CONSTANT = Q(6.6743e-11, '(m^3)/(kg * s^2)')

# %% ../nbs/00_constants.ipynb 9
EARTH_MASS = Q(5.9736e24, 'kilogram').to(Unit.MASS)
EARTH_RADIUS = Q(6371, 'kilometer').to(Unit.LENGTH)
EARTH_GRAVITY = Q(9.807, 'meter/(second^2)').to(Unit.ACCELERATION)

# %% ../nbs/00_constants.ipynb 11
MARS_MASS = Q(6.39e23, 'kilogram').to(Unit.MASS)
MARS_RADIUS = Q(3389.5, 'kilometer').to(Unit.LENGTH)
MARS_GRAVITY = Q(3.721, 'meter/(second^2)').to(Unit.ACCELERATION)

# %% ../nbs/00_constants.ipynb 13
MOON_MASS = Q(7.34767309e22, 'kilogram').to(Unit.MASS)
MOON_RADIUS = Q(1737.4, 'kilometer').to(Unit.LENGTH)
MOON_GRAVITY = Q(1.62, 'meter/(second^2)').to(Unit.ACCELERATION)
