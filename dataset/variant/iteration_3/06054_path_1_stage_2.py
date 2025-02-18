import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

north_america_renewable = [50, 70, 110, 150, 200, 260, 330, 410, 500, 600, 710]
europe_renewable = [60, 80, 100, 140, 200, 280, 360, 450, 550, 670, 800]
asia_renewable = [40, 60, 90, 130, 180, 240, 310, 390, 480, 580, 690]
south_america_renewable = [20, 30, 50, 75, 110, 150, 200, 260, 330, 410, 500]

data = np.array([
    north_america_renewable,
    europe_renewable,
    asia_renewable,
    south_america_renewable
])

fig, ax = plt.subplots(figsize=(12, 8))

# Stackplot without stylistic elements
ax.stackplot(
    years, data,
    colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd'], alpha=0.85
)

ax.set_title(
    "A Decade of Renewable Energy Growth:\nContribution by Region (2010-2020)",
    fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Renewable Energy Production (TWh)", fontsize=14)

# Removing grid lines, legends, and annotations
fig.tight_layout()

plt.show()