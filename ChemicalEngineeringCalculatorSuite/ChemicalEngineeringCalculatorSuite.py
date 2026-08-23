import reflex as rx
import numpy as np
from scipy.integrate import odeint


def batch_reactor_logic(concentrations, t, k):
    Ca = concentrations[0]
    Cb = concentrations[1]
    return [-k * Ca, k * Ca]




class ReactorState(rx.State):
    k: float = 0.1
    reactor_data: list[dict] = []

    def change_k(self, new_value: list[float]):
        self.k = new_value[0]

    def update_chart(self):
        t = np.linspace(0, 50, 50)

        solution = odeint(batch_reactor_logic, [1.0, 0.0], t, args=(self.k,))

        new_data = []
        for i in range(len(t)):
            new_data.append({
                "time": float(t[i]),
                "A": float(solution[i, 0]),
                "B": float(solution[i, 1])
            })
        self.reactor_data = new_data









def index():
    return rx.vstack(
        rx.heading("Batch Reactor Dashboard"),
        rx.text("Reaction Rate Constant (k): ", ReactorState.k),

        rx.slider(
            value=[ReactorState.k],
            on_change=ReactorState.change_k,
            on_value_commit=ReactorState.update_chart,
            min=0.01,
            max=0.5,
            step=0.01
        ),

        rx.recharts.line_chart(
            rx.recharts.line(
                data_key="A",
                stroke="#3182ce",
                name="Reactant A",
            ),
            rx.recharts.line(
                data_key="B",
                stroke="#38a169",
                name="Product B",
            ),
            rx.recharts.x_axis(data_key="time"),
            rx.recharts.y_axis(),
            rx.recharts.graphing_tooltip(),
            data=ReactorState.reactor_data,
            width="100%",
            height=400,
        ),

        padding="2em",
        align_items="center"
    )



app = rx.App()
app.add_page(index, on_load=ReactorState.update_chart)
    