import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1990, 2021)
ice_cream_sales = np.array([
    10, 11, 11.3, 11.5, 12, 12.6, 12.9, 13.2, 14.5, 14.1,
    14.8, 15.6, 15.8, 16.7, 17.5, 17.9, 19.2, 19.1, 19.4, 20.1,
    20.3, 21.2, 21.6, 21.9, 22.5, 22.7, 23.2, 23.8, 24.2, 25.1,
    25.3
])

plt.figure(figsize=(14, 7))
plt.plot(years, ice_cream_sales, color='blue', marker='s', linestyle='--', linewidth=3, markersize=8, label='Frozen Treats Sales (Billion USD)')

highlight_indices = [0, 10, 20, 30]
for i in highlight_indices:
    plt.annotate(
        f'Sales: {ice_cream_sales[i]:.1f} B',
        (years[i], ice_cream_sales[i]),
        textcoords="offset points",
        xytext=(-5, 10),
        ha='center',
        fontsize=10,
        color='blue',
        bbox=dict(boxstyle='round,pad=0.3', edgecolor='gray', facecolor='white', alpha=0.5)
    )

plt.title('Global Frozen Delight Sales Over Time\nSpanning 1990 to 2020', fontsize=16, pad=20)
plt.xlabel('Timeline (Years)', fontsize=12)
plt.ylabel('Frozen Delights (in Billion USD)', fontsize=12)
plt.xticks(years[::2], rotation=45)
plt.yticks(np.arange(10, 26, 2))
plt.grid(False)  # Remove grid
plt.legend(loc='lower right', fontsize=10)  # Change legend location
plt.tight_layout()
plt.show()