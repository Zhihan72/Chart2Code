import matplotlib.pyplot as plt
import numpy as np

weeks = np.arange(1, 11)

sales = np.array([60, 75, 90, 120, 130, 160, 170, 150, 135, 125])
temperature = np.array([20, 22, 25, 27, 30, 32, 33, 31, 28, 26])
satisfaction = np.array([6, 7, 7.5, 8, 9, 9, 9.5, 8.5, 8, 7.5])

plt.figure(figsize=(14, 9))

# Shuffle the color map by assigning a different 'cmap' available (e.g., 'plasma' instead of 'viridis')
scatter = plt.scatter(temperature, sales, s=satisfaction*100, c=satisfaction, cmap='plasma', alpha=0.75, edgecolors='black', linewidth=1)

plt.title("Impact of Temperature on Ice Cream Sales and Customer Satisfaction\nin Fictional Town's Summer Weeks", fontsize=18, fontweight='bold', pad=20)
plt.xlabel("Temperature (°C)", fontsize=14)
plt.ylabel("Ice Cream Sales (Units)", fontsize=14)

for i, week in enumerate(weeks):
    plt.annotate(f"Week {week}", (temperature[i] + 0.5, sales[i]), fontsize=10, fontweight='bold', bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray'))

plt.grid(True, linestyle='--', alpha=0.6)

cbar = plt.colorbar(scatter)
cbar.set_label('Customer Satisfaction (0 to 10)', fontsize=12)

plt.tight_layout()

plt.show()