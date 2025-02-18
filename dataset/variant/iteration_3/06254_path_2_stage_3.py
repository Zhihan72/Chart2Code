import matplotlib.pyplot as plt
import numpy as np

cities = np.arange(1, 11)
green_space_per_capita = np.array([15, 30, 25, 40, 50, 32, 22, 60, 45, 35])
happiness_index = np.array([6.0, 7.5, 7.0, 8.0, 9.0, 7.2, 6.5, 9.5, 8.2, 7.8])

plt.figure(figsize=(12, 7))
plt.scatter(green_space_per_capita, happiness_index, color='darkorange', edgecolors='gray', s=100, alpha=0.9, marker='x')

for i, city in enumerate(cities):
    plt.annotate(f'C{city}', 
                 (green_space_per_capita[i], happiness_index[i]),
                 textcoords="offset points",
                 xytext=(-10, -10),
                 ha='right', fontsize=11, color='purple')

plt.title("Green Space vs. Happiness", fontsize=16, fontweight='bold')
plt.xlabel("Green Space (sqm)", fontsize=14, color='green')
plt.ylabel("Happiness Index", fontsize=14, color='green')

plt.grid(True, linestyle='-.', alpha=0.4)

m, b = np.polyfit(green_space_per_capita, happiness_index, 1)
plt.plot(green_space_per_capita, m * green_space_per_capita + b, color='blue', linestyle='-', linewidth=1.5, label='Trend Line')

plt.legend(loc='upper left', fontsize=12, frameon=True, shadow=True, borderpad=1)
plt.tight_layout()
plt.show()