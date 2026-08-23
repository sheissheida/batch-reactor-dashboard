# Batch Reactor Kinetics Dashboard 🧪

hey. 

honestly this is just a personal practice project and nothing really special. i mainly built it to get the hang of python and learn how the **Reflex** web framework works behind the scenes (trying to avoid that copy-paste "vibe coding" thing). i also just wanted a safe place to keep my code.

## What it does
it's a simple interactive web dashboard that simulates the kinetics of a basic batch reactor (where Reactant A turns into Product B). 
* solves ordinary differential equations (ODEs) for mass balance in the background.
* includes a slider so you can play around with the reaction rate constant (k).
* instantly updates the concentration vs. time graph based on your input.

## The Tech Stack I Used
* **Reflex:** for building the UI and handling the state purely in python.
* **SciPy (`odeint`):** to solve the differential equations.
* **NumPy:** for data arrays and handling time intervals.

## How to run it locally
if you happen to stumble upon this and want to run it on your machine, it's pretty straightforward:

1. Clone this repository to your computer.
2. Install the required libraries:
   pip install reflex scipy numpy
3. Run the Reflex app:
   reflex run
4. Open `http://localhost:3000` in your browser to see the dashboard.
