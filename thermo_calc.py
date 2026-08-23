class Chemical:
    def __init__(self, name, A, B, C):
        self.name = name
        self.A = A
        self.B = B
        self.C = C
        self.T_min = 1
        self.T_max = 100


    def vapor_pressure(self, T, T_unit="C"):
        T_unit = T_unit.upper()

        if T_unit == "K":
            T_calc = T - 273.15
        elif T_unit == "F":
            T_calc = (T - 32) * 5/9
        elif T_unit == "C":
            T_calc = T
        else:
            raise ValueError("Invalid Temperature Unit! Use 'C', 'F', or 'K'.")



        if T_calc < self.T_min or T_calc > self.T_max:
            raise ValueError(f"Temperature {T} is out of bounds for {self.name}!")
        else:
            P = 10 ** (self.A - (self.B / (self.C + T_calc)))
            return P



