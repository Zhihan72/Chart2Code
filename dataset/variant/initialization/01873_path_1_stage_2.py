import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1990, 2021)
ice_cream_sales = np.array([
    10, 10.5, 11, 11.2, 11.8, 12.3, 13, 13.5, 14, 14.2, 
    15, 15.5, 16, 16.8, 17.3, 18, 18.5, 19, 19.7, 20, 
    20.5, 21, 21.5, 22, 22.3, 22.8, 23.5, 24, 24.5, 25, 
    25.5
])

plt.figure(figsize=(14, 7))
# Changed the legend label
plt.plot(years, ice_cream_sales, color='orange', marker='o', linestyle='-', linewidth=2, markersize=6, label='Frozen Treats Sales (Billion USD)')

highlight_indices = [0, 10, 20, 30]
for i in highlight_indices:
    # Changed value annotation text
    plt.annotate(
        f'Sales: {ice_cream_sales[i]:.1f} B',
        (years[i], ice_cream_sales[i]),
        textcoords="offset points",
        xytext=(-5, 10),
        ha='center',
        fontsize=10,
        color='orange',  
        bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='lightgray', alpha=0.5)
    )

# Changed title
plt.title('Global Frozen Delight Sales Over Time\nSpanning 1990 to 2020', fontsize=16, pad=20)
# Changed axis labels
plt.xlabel('Timeline (Years)', fontsize=12)
plt.ylabel('Frozen Delights (in Billion USD)', fontsize=12)
plt.xticks(years[::2], rotation=45)
plt.yticks(np.arange(10, 26, 2))
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper left', fontsize=10)
plt.tight_layout()
plt.show()