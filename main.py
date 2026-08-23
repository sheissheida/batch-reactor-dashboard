from thermo_calc import Chemical
from reactor_kinetics import BatchReactor
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def run_reactor():
    print("\n--- Running Batch Reactor Simulation ---")

    reactor = BatchReactor(0.1, [1.0, 0.0])

    t = np.linspace(0, 50, 100)

    solution = odeint(reactor.reaction_equations, reactor.C0, t)

    Ca_out = solution[:, 0]
    Cb_out = solution[:, 1]

    plt.plot(t, Ca_out, label='Reactant A', color='blue', linewidth=2)
    plt.plot(t, Cb_out, label='Product B', color='green', linewidth=2)

    plt.xlabel('Time (minutes)')
    plt.ylabel('Concentration (mol/L)')
    plt.title('Batch Reactor Kinetics: A -> B')
    plt.legend()
    plt.grid(True)

    plt.show()



if __name__ == "__main__":
    run_reactor()