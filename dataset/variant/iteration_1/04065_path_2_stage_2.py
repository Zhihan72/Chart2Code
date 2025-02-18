import matplotlib.pyplot as plt
import numpy as np

weeks = np.arange(1, 11)
sales = np.array([60, 75, 90, 120, 130, 160, 170, 150, 135, 125])
temperature = np.array([20, 22, 25, 27, 30, 32, 33, 31, 28, 26])

# Manually shuffled satisfaction values to change assigned colors
shuffled_satisfaction = np.array([9, 7.5, 8.5, 8, 9, 7, 9.5, 8, 7.5, 6])

plt.figure(figsize=(14, 9))
bar_chart = plt.barh(temperature, sales, color=plt.cm.viridis(shuffled_satisfaction / max(shuffled_satisfaction)), edgecolor='black')

plt.title("Impact of Temperature on Ice Cream Sales and Customer Satisfaction\nin Fictional Town's Summer Weeks", fontsize=18, fontweight='bold', pad=20)
plt.xlabel("Ice Cream Sales (Units)", fontsize=14)
plt.ylabel("Temperature (°C)", fontsize=14)

for i, (sales_val, temp, week) in enumerate(zip(sales, temperature, weeks)):
    plt.text(sales_val + 2, temp, f"Week {week}", fontsize=10, fontweight='bold', va='center')

plt.grid(True, linestyle='--', alpha=0.6, axis='x')

sm = plt.cm.ScalarMappable(cmap='viridis', norm=plt.Normalize(0, 10))
sm.set_array([])
cbar = plt.colorbar(sm, ax=plt.gca())
cbar.set_label('Customer Satisfaction (0 to 10)', fontsize=12)

plt.tight_layout()
plt.show()