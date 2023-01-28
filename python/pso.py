# pso with pyswarms library

import pyswarms as ps
import matplotlib.pyplot as plt
from pyswarms.utils.functions import single_obj as fonksiyon
from pyswarms.utils.plotters import plot_cost_history, plot_contour, plot_surface

# Define the parameters for the PSO algorithm
parameters = {"c1":0.5, "c2":0.3, "w":0.9}

# Create an instance of the GlobalBestPSO optimizer
optimizer = ps.single.GlobalBestPSO(n_particles=20, dimensions=3, options=parameters)

# Optimize the sphere function using the optimizer
best_cost, best_pos = optimizer.optimize(fonksiyon.sphere, iters = 1000)

# Plot the cost history over the course of the optimization
plot_cost_history(optimizer.cost_history)
plt.show()