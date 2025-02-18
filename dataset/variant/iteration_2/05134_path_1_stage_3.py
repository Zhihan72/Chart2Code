import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Years remain unchanged
years = np.arange(2010, 2023)

# Manually shuffled data while preserving dimensionality
green_space_area = np.array([120, 130, 145, 160, 175, 190, 200, 215, 225, 240, 260, 270, 280])
health_index = np.array([62, 64, 67, 69, 72, 74, 76, 78, 80, 83, 85, 87, 90])

x_smooth = np.linspace(green_space_area.min(), green_space_area.max(), 300)
spl = make_interp_spline(green_space_area, health_index, k=3)
y_smooth = spl(x_smooth)

plt.figure(figsize=(12, 8))
plt.scatter(green_space_area, health_index, color='forestgreen', edgecolor='black', s=100)
plt.plot(x_smooth, y_smooth, color='forestgreen', linestyle='-', linewidth=2)

plt.title("Impact of Urban Green Spaces on Community Health\n(2010-2022)", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Urban Green Space Area (hectares)", fontsize=14, labelpad=10)
plt.ylabel("Community Health Index (out of 100)", fontsize=14, labelpad=10)

important_years = {
    "2015: Major Park Renovation": (175, 71),
    "2018: Green Rooftop Initiative Launch": (220, 77),
    "2020: Community Garden Expansion": (240, 80)
}

for label, (x, y) in important_years.items():
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, bbox=dict(facecolor='white', alpha=0.5))

plt.tight_layout()
plt.show()