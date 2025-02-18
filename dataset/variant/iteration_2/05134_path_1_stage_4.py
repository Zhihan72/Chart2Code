import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

years = np.arange(2010, 2023)

green_space_area = np.array([120, 130, 145, 160, 175, 190, 200, 215, 225, 240, 260, 270, 280])
health_index = np.array([62, 64, 67, 69, 72, 74, 76, 78, 80, 83, 85, 87, 90])

x_smooth = np.linspace(green_space_area.min(), green_space_area.max(), 300)
spl = make_interp_spline(green_space_area, health_index, k=3)
y_smooth = spl(x_smooth)

plt.figure(figsize=(12, 8))
plt.scatter(green_space_area, health_index, color='forestgreen', edgecolor='black', s=100)
plt.plot(x_smooth, y_smooth, color='forestgreen', linestyle='-', linewidth=2)

plt.title("Community Health and Green Areas Influence\n2000's - Present", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Area of Green Spaces (ha)", fontsize=14, labelpad=10)
plt.ylabel("Health Index Score", fontsize=14, labelpad=10)

important_years = {
    "Renovation of Main Park - 2015": (175, 71),
    "Launch of Rooftop Greenery Initiative - 2018": (220, 77),
    "Expansion of Community Gardens - 2020": (240, 80)
}

for label, (x, y) in important_years.items():
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, bbox=dict(facecolor='white', alpha=0.5))

plt.tight_layout()
plt.show()