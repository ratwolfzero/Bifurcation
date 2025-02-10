
import matplotlib.pyplot as plt
import numpy as np
from numba import njit

@njit
def logistic_map(r, x):
    """Logistic map function: x(n+1) = r * x(n) * (1 - x(n))"""
    return r * x * (1 - x)

@njit
def compute_bifurcation_data(r_min=2.5, r_max=4.0, r_steps=10000, iterations=10000, last=100):
    """
    Compute bifurcation data using Numba for performance optimization.
    
    - r_min, r_max: Range of r values
    - r_steps: Number of r values
    - iterations: Total iterations per r value
    - last: Number of last iterations to store for plotting
    """
    r_values = np.linspace(r_min, r_max, r_steps)
    bifurcation_points = []

    for r in r_values:
        x = 0.5  # Initial condition
        for _ in range(iterations - last):
            x = logistic_map(r, x)  # Iterate to stabilize
        
        for _ in range(last):
            x = logistic_map(r, x)
            bifurcation_points.append((r, x))

    return np.array(bifurcation_points)

def plot_bifurcation(bifurcation_data):
    """Plots the bifurcation diagram from precomputed data."""
    plt.figure(figsize=(10, 6))
    plt.plot(bifurcation_data[:, 0], bifurcation_data[:, 1], ',k', alpha=0.25, markersize=0.1)
    plt.xlim(2.5, 4.0)
    plt.ylim(0, 1)
    plt.xlabel("r (Growth Rate)")
    plt.ylabel("x (Population)")
    plt.title("Bifurcation Diagram of the Logistic Map")
    plt.show()

# Main execution
bifurcation_data = compute_bifurcation_data()
plot_bifurcation(bifurcation_data)

