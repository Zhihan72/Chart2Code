import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Data
years = np.arange(2010, 2023)
green_space_area = np.array([120, 135, 150, 165, 175, 190, 205, 220, 230, 240, 255, 270, 285])
health_index = np.array([65, 66, 68, 69, 71, 73, 75, 77, 78, 80, 82, 84, 86])

# Spline interpolation
x_smooth = np.linspace(green_space_area.min(), green_space_area.max(), 300)
spl = make_interp_spline(green_space_area, health_index, k=3)
y_smooth = spl(x_smooth)

# Plot
plt.figure(figsize=(12, 8))
plt.scatter(green_space_area, health_index, color='purple', edgecolor='black', s=100, label='Data Points')
plt.plot(x_smooth, y_smooth, color='orange', linestyle='-', linewidth=2, label='Smooth Fit')

# Title and labels
plt.title("Impact of Urban Green Spaces on Community Health\n(2010-2022)", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Urban Green Space Area (hectares)", fontsize=14, labelpad=10)
plt.ylabel("Community Health Index (out of 100)", fontsize=14, labelpad=10)

# Annotations
important_years = {
    "2015: Major Park Renovation": (175, 71),
    "2018: Green Rooftop Initiative Launch": (220, 77),
    "2020: Community Garden Expansion": (240, 80)
}

for label, (x, y) in important_years.items():
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, bbox=dict(facecolor='white', alpha=0.5))

# Legend and grid
plt.legend(loc='lower right', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Display
plt.show()