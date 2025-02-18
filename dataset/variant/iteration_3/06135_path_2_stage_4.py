import matplotlib.pyplot as plt
import numpy as np

# Data for plant growth under different sunlight conditions
sunlight = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
succulent_growth = np.array([2, 3, 5, 8, 10, 12, 14, 16, 17.5, 18])
pothos_growth = np.array([1, 2, 4, 7, 11, 16, 20, 23, 25, 27])
cactus_growth = np.array([2, 4, 6, 7, 8, 10, 11, 11.5, 12, 12.5])
sizes = np.array([50, 70, 90, 110, 130, 150, 170, 190, 210, 230])

plt.figure(figsize=(14, 8))
plt.scatter(sunlight, succulent_growth, s=sizes, c='purple', alpha=0.6, edgecolor='k')
plt.scatter(sunlight, pothos_growth, s=sizes, c='purple', alpha=0.6, edgecolor='k')
plt.scatter(sunlight, cactus_growth, s=sizes, c='purple', alpha=0.6, edgecolor='k')

plt.title('Sun Power on Greenery Rise\nTracked by Days', fontsize=16, fontweight='bold')
plt.xlabel('Luminosity Hours', fontsize=12)
plt.ylabel('Height Climb (cm)', fontsize=12)

plt.tight_layout()
plt.show()