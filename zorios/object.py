# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_object.ipynb.

# %% auto 0
__all__ = ['Shape', 'Shape3D', 'Point', 'Square', 'Sphere', 'Object', 'Particle', 'RigidBody', 'BuildObject', 'BuildParticle',
           'BuildRigidBody', 'BuildSphere', 'BuildPlanet', 'PlanetFactory']

# %% ../nbs/03_object.ipynb 4
from abc import ABC, abstractmethod
from dataclasses import dataclass

from fastcore.test import test_eq

from . import constants

# %% ../nbs/03_object.ipynb 8
class Shape(ABC):
    # @abstractmethod
    # def radius(self):
    #     pass
    pass

# %% ../nbs/03_object.ipynb 9
class Shape3D(Shape):
    # @abstractmethod
    # def volume(self):
    #     pass
    pass

# %% ../nbs/03_object.ipynb 10
class Point(Shape):
    pass

# %% ../nbs/03_object.ipynb 11
class Square(Shape):
    def radius(self):
        # in the square, the radius called diangal
        pass

# %% ../nbs/03_object.ipynb 12
class Sphere(Shape3D):
    
    def __init__(
        self,
        radius # the radius of the sphere
    ):
        self.radius = radius

# %% ../nbs/03_object.ipynb 15
class Object:
    def __init__(self):
        self.mass = None
        self.shape: Shape = None

# %% ../nbs/03_object.ipynb 16
class Particle(Object):
    def __init__(self):
        pass

# %% ../nbs/03_object.ipynb 17
class RigidBody(Object):
    pass

# %% ../nbs/03_object.ipynb 19
class BuildObject(ABC):
    
    @abstractmethod
    def setMass(self):
        pass
    
    @abstractmethod
    def build(self):
        pass

# %% ../nbs/03_object.ipynb 20
class BuildParticle(BuildObject, Particle):
    
    def __init__(self, particle=Particle()):
        self.particle = particle
        self.particle.shape = Point()
    
    def setMass(self, mass):
        self.particle.mass = mass
        return self
    
    def build(self):
        return self.particle

# %% ../nbs/03_object.ipynb 21
class BuildRigidBody(BuildObject, RigidBody):
    @abstractmethod
    def setShape(self):
        pass

# %% ../nbs/03_object.ipynb 23
class BuildSphere(BuildRigidBody):
    def __init__(
        self,
        #body=Object(),
        radius # the radius of the sphere
    ):
        self.shape = Sphere(radius=radius)
    
    def setMass(self, mass):
        return self
    
    def build(self):
        return self

# %% ../nbs/03_object.ipynb 26
class BuildPlanet(BuildRigidBody):
    def __init__(self, object=Object()):
        self.object = object
    
    def setMass(self, mass):
        self.object.mass = mass
        return self
    
    def setShape(self, shape):
        self.object.shape = shape
        return self
    
    def build(self):
        return self.object

# %% ../nbs/03_object.ipynb 27
class PlanetFactory:
    
    @staticmethod
    def new_earth():
        shape = Sphere(radius=constants.EARTH_RADIUS)
        earth = BuildPlanet().setMass(constants.EARTH_MASS).setShape(shape).build()
        return earth
    
    @staticmethod
    def new_mars():
        shape = Sphere(radius=constants.MARS_RADIUS)
        mars = BuildPlanet().setMass(constants.MARS_MASS).setShape(shape).build()
        return mars
