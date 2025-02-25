import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Data with altered content
years = np.arange(2010, 2023)
green_space_area = np.array([110, 130, 145, 160, 170, 185, 200, 215, 225, 235, 250, 265, 280])
health_index = np.array([60, 64, 67, 70, 72, 74, 76, 78, 80, 81, 83, 85, 87])

# Spline interpolation
x_smooth = np.linspace(green_space_area.min(), green_space_area.max(), 300)
spl = make_interp_spline(green_space_area, health_index, k=3)
y_smooth = spl(x_smooth)

# Plot
plt.figure(figsize=(12, 8))
plt.scatter(green_space_area, health_index, color='purple', edgecolor='black', s=100, label='Data')
plt.plot(x_smooth, y_smooth, color='orange', linestyle='-', linewidth=2, label='Fit')

# Title and labels
plt.title("Green Space vs Health (2010-2022)", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Green Space (ha)", fontsize=14, labelpad=10)
plt.ylabel("Health Index", fontsize=14, labelpad=10)

# Annotations
important_years = {
    "2015: Major Renovation": (135, 66),
    "2018: Rooftop Initiative": (230, 78),
    "2020: Garden Expansion": (240, 80)
}

for label, (x, y) in important_years.items():
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, bbox=dict(facecolor='white', alpha=0.5))

# Legend and grid
plt.legend(loc='lower right', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Display
plt.show()