import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)
parks = np.array([10, 15, 25, 35, 45, 55, 65, 75, 90, 100, 120])
gardens = np.array([5, 7, 10, 15, 20, 25, 30, 35, 40, 50, 60])
reserves = np.array([2, 4, 6, 10, 15, 20, 25, 30, 35, 40, 50])

parks_cumulative = np.cumsum(parks)
gardens_cumulative = np.cumsum(gardens)
reserves_cumulative = np.cumsum(reserves)

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, 
             parks_cumulative, 
             gardens_cumulative, 
             reserves_cumulative,
             labels=['Natural Reserves', 'Parks', 'Community Gardens'],
             colors=['#8da0cb', '#66c2a5', '#fc8d62'], alpha=0.7)

ax.set_title('A Decade of Greener Living: Urban Green Space Expansion\nEcoVille, 2020-2030', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=12)
ax.set_ylabel('Cumulative Area of Green Spaces (Hectares)', fontsize=12)
ax.legend(loc='upper left', title='Type of Green Space', fontsize=10)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right', fontsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.annotate('Major Growth\nProject in 2025', xy=(2025, 100), xytext=(2025, 250),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, ha='center')

plt.tight_layout()
plt.show()