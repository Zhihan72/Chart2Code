import matplotlib.pyplot as plt
import numpy as np

cities = ["City A", "City B", "City C", "City D", "City E", "City F", "City G", "City H"]
tree_coverage = np.array([10, 15, 25, 30, 35, 40, 45, 50])
AQI_levels = np.array([150, 130, 100, 90, 85, 75, 70, 65])

temperature_trends = {
    "City A": [5, 15, 25, 10],
    "City B": [8, 18, 28, 12],
    "City C": [10, 20, 30, 15],
    "City D": [12, 22, 32, 17],
    "City E": [14, 24, 34, 19],
    "City F": [16, 26, 36, 21],
    "City G": [18, 28, 38, 23],
    "City H": [20, 30, 40, 25]
}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

ax1.scatter(tree_coverage, AQI_levels, color='green', s=100, alpha=0.8,
            edgecolors='black', linewidth=1.5)

for i, txt in enumerate(cities):
    ax1.annotate(txt,
                 (tree_coverage[i], AQI_levels[i]), 
                 textcoords="offset points", 
                 xytext=(0, 10), 
                 ha='center', 
                 fontsize=10)

ax1.set_title("Tree Coverage vs AQI", fontsize=16, pad=20)
ax1.set_xlabel("Coverage (%)", fontsize=14)
ax1.set_ylabel("AQI", fontsize=14)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.set_xlim(0, 55)
ax1.set_ylim(50, 160)

for city in cities:
    temperatures = temperature_trends[city]
    quarters = ['W', 'Sp', 'Su', 'A']  # Shortened quarter names
    ax2.plot(quarters, temperatures, marker='o', label=city)

ax2.set_title("City Temp Trends", fontsize=16, pad=20)
ax2.set_xlabel("Season", fontsize=14)
ax2.set_ylabel("Temp (°C)", fontsize=14)
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.legend(title='City', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()