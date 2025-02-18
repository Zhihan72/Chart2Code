import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])
solar_flares = np.array([120, 150, 180, 210, 260, 230, 270])

plt.figure(figsize=(12, 7))
plt.plot(decades, solar_flares, color='coral', marker='x', linestyle='--', linewidth=2.5, markersize=10)

# Remove title and labels
# plt.title('Detection of Solar Flares per Decade', fontsize=16, fontweight='bold', pad=20)
# plt.xlabel('Decade', fontsize=14)
# plt.ylabel('Count of Solar Flares', fontsize=14)

# Remove annotations
# annotations = [
#     ("Cycle 20 Peak", 1960, 120),
#     ("Cycle 21 Peak", 1980, 180),
#     ("Cycle 22 Peak", 1990, 210),
#     ("Halloween Storms", 2000, 260),
#     ("Solar Cycle 24", 2010, 230),
#     ("Cycle 25 Surge", 2020, 270)
# ]
# for text, x, y in annotations:
#     plt.annotate(text, xy=(x, y), xytext=(-50, 10),
#                  textcoords='offset points', arrowprops=dict(arrowstyle="<|-", color='firebrick'), fontsize=10)

plt.grid(True, linestyle='-', alpha=0.3)

# Remove legend
# plt.legend(loc='lower right', fontsize=12, frameon=False)

plt.gca().spines['top'].set_visible(False)
plt.tight_layout()
plt.show()