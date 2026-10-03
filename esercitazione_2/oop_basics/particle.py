import math

# Everything is carried on in natural units (c = 1).
# The time-like component of 4-vectors is the last one, since it's the convention used by ROOT.

class particle:
    def __init__(self, px, py, pz, m):
        self.px = px
        self.py = py
        self.pz = pz
        self.m  = m
        self.p  = math.sqrt(px**2 + py**2 + pz**2)
        self.E  = math.sqrt(m**2 + self.p**2)
        self.p4 = (px, py, pz, self.E)
        
        self.gamma = self.E / m
        self.beta  = self.p / (self.gamma * m)

    def particle_info(self):
        return f"\nCharacteristics of the particle:\n px = {self.px}\n py = {self.py}\n pz = {self.pz}\n m  = {self.m}\n \nMomentum-Energy 4-vector:\n p4 = {self.p4}\n \nCinematic variables:\n Gamma = {self.gamma}\n Beta  = {self.beta}"