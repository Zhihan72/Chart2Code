import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])
solar_flares = np.array([150, 230, 270, 120, 260, 180, 210])

plt.figure(figsize=(12, 7))
# Set a single consistent color for the line and markers
plt.plot(decades, solar_flares, color='blue', marker='o', linestyle='-', linewidth=2, markersize=8)
plt.title('Solar Flare Detection over Decades\nMonitoring Frequency for Space Weather Analysis', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Decade', fontsize=14)
plt.ylabel('Number of Solar Flares', fontsize=14)

# Setting the same color for annotation arrows as the line plot
annotations = [
    ("Cycle 21 Peak", 1960, 150),
    ("Solar Cycle 24", 1980, 180),
    ("Cycle 25 Surge", 1990, 210),
    ("Cycle 20 Peak", 2000, 120),
    ("Halloween Storms", 2010, 260),
    ("Cycle 22 Peak", 2020, 270)
]
for text, x, y in annotations:
    plt.annotate(text, xy=(x, y), xytext=(-60, 10),
                 textcoords='offset points', arrowprops=dict(arrowstyle="->", color='blue'), fontsize=10)

plt.tight_layout()
plt.show()