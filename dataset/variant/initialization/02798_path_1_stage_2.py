import matplotlib.pyplot as plt
import numpy as np

# Decades from the 1960s to the 2020s
decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])

# Hypothetical number of solar flares detected each decade - shuffled values
solar_flares = np.array([150, 230, 270, 120, 260, 180, 210])

plt.figure(figsize=(12, 7))
plt.plot(decades, solar_flares, color='orange', marker='o', linestyle='-', linewidth=2, markersize=8)
plt.title('Solar Flare Detection over Decades\nMonitoring Frequency for Space Weather Analysis', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Decade', fontsize=14)
plt.ylabel('Number of Solar Flares', fontsize=14)

# Randomly altered annotations to match shuffled data
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
                 textcoords='offset points', arrowprops=dict(arrowstyle="->", color='grey'), fontsize=10)

plt.tight_layout()
plt.show()