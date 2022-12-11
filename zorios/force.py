# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_force.ipynb.

# %% auto 0
__all__ = ['Force', 'AttractiveGravity']

# %% ../nbs/02_force.ipynb 3
import pandas as pd
import numpy as np
import sympy as smp

from .core import *
from .object import BuildSphere
from . import constants

# %% ../nbs/02_force.ipynb 5
class Force:
    pass

# %% ../nbs/02_force.ipynb 13
class AttractiveGravity(Force):
    
    def magnitude(
        self,
        other_object
    ):
        pass