import numpy as np
import matplotlib.pyplot as plt

cities = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
populations = [3000000, 50000, 2000000, 150000, 450000, 1200000, 600000, 850000, 1500000, 300000]
park_counts = [20, 300, 350, 35, 75, 200, 90, 150, 250, 50]

fig, ax = plt.subplots(figsize=(12, 8))

ax.scatter(populations, park_counts, s=populations, alpha=0.6, edgecolors='w', c=park_counts, cmap='plasma')

for i, city in enumerate(cities):
    ax.annotate(city, (populations[i], park_counts[i]), fontsize=10, ha='right')

coefficients = np.polyfit(populations, park_counts, 1)
polynomial = np.poly1d(coefficients)
trendline = polynomial(populations)
ax.plot(populations, trendline, color='red', linestyle='--', linewidth=1.5)

ax.set_xlabel('Population', fontsize=12)
ax.set_ylabel('Parks', fontsize=12)

plt.tight_layout()
plt.show()