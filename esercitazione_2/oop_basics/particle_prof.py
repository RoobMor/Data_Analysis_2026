import math

class particle:
    # esempio di attributo di classe
    c = 299792458 # m/s
    
    # inizializzazione della particella (metodo d'istanza)
    def __init__(self, px, py, pz, m):
        # i seguenti sono tutti attributi d'istanza
        self.px = px
        self.py = py
        self.pz = pz
        self.m  = m
        self.e  = math.sqrt(m**2 + (px**2 + py**2 + pz*2))
        self.p4 = (self.px, self.py, self.pz, self.e)

    # metodo d'istanza annidato in un metodo statico (self non serve a nulla...)
    # è un esempio di costruzione di un oggetto di classe particle, passando solo un 4-vettore
    # PROBLEMA: gli argomenti di particle sono diversi da quelli riportati sotto!
    def particle_p4(self, lorentz_p4):
        return particle(px=lorentz_p4.px, py=lorentz_p4.py, pz=lorentz_p4.pz, e=lorentz_p4.E)

    # metodo d'istanza
    # ridefinisce il quadri-momento della particella
    # è l'analogo di quanto fatto con particle_p4(...), ma in modo esplicito
    # ATTENZIONE: m potrebbe non rispettare la mass-shell (tra l'altro non viene definita...)
    def init(self, lorentz_p4):
        self.px = lorentz_p4.px
        self.py = lorentz_p4.py
        self.pz = lorentz_p4.pz
        self.e  = lorentz_p4.E
        self.p4 = (self.e, self.px, self.py, self.pz)

    # stampa info generali sulla particella
    def particle_info(self):
        return f"\nCharacteristics of the particle:\n px = {self.px}\n py = {self.py}\n pz = {self.pz}\n m  = {self.m}\n \nEnergy-Momentum 4-vector:\n E = {self.e}\n p4 = {self.p4}"


measure_unit = "GeV"
x = particle(2, 4, 0.3, 10)

print("Assuming natural units (c = 1)")
print("In units of " + measure_unit + ":\n")
print(x.e)
print(x.p4)
print(x.particle_info())