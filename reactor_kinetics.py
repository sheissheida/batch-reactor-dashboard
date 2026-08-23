import numpy as np
from scipy.integrate import odeint


class BatchReactor:
    def __init__(self, k, C0):
        self.k = k
        self.C0 = C0


    def reaction_equations(self, concentrations, t):
        Ca = concentrations[0]
        Cb = concentrations[1]

        dCa_dt = -self.k * Ca
        dCb_dt = self.k * Ca

        return [dCa_dt, dCb_dt]






