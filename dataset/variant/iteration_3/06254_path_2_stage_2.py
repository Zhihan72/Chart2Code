import matplotlib.pyplot as plt
import numpy as np

cities = np.arange(1, 11)
green_space_per_capita = np.array([15, 30, 25, 40, 50, 32, 22, 60, 45, 35])
happiness_index = np.array([6.0, 7.5, 7.0, 8.0, 9.0, 7.2, 6.5, 9.5, 8.2, 7.8])

plt.figure(figsize=(12, 7))
plt.scatter(green_space_per_capita, happiness_index, color='royalblue', edgecolors='black', s=150, alpha=0.7)

for i, city in enumerate(cities):
    plt.annotate(f'C{city}', 
                 (green_space_per_capita[i], happiness_index[i]),
                 textcoords="offset points",
                 xytext=(5, 5),
                 ha='center', fontsize=10, color='black')

plt.title("Green Space vs. Happiness", fontsize=16, fontweight='bold')
plt.xlabel("Green Space (sqm)", fontsize=13)
plt.ylabel("Happiness Index", fontsize=13)

plt.grid(True, linestyle='--', alpha=0.6)

m, b = np.polyfit(green_space_per_capita, happiness_index, 1)
plt.plot(green_space_per_capita, m * green_space_per_capita + b, color='crimson', linestyle='--', linewidth=2, label='Trend')

plt.legend(loc='lower right')
plt.tight_layout()
plt.show()