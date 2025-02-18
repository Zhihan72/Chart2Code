import matplotlib.pyplot as plt
import numpy as np

weeks = np.arange(1, 11)
sales = np.array([60, 75, 90, 120, 130, 160, 170, 150, 135, 125])

# Manually shuffled satisfaction values to change assigned colors
shuffled_satisfaction = np.array([9, 7.5, 8.5, 8, 9, 7, 9.5, 8, 7.5, 6])

plt.figure(figsize=(14, 9))
plt.barh(weeks, sales, color=plt.cm.viridis(shuffled_satisfaction / max(shuffled_satisfaction)), edgecolor='black')

plt.title("Impact of Weeks on Ice Cream Sales and Customer Satisfaction", fontsize=18, fontweight='bold', pad=20)
plt.xlabel("Ice Cream Sales (Units)", fontsize=14)
plt.ylabel("Weeks", fontsize=14)

for i, (sales_val, week) in enumerate(zip(sales, weeks)):
    plt.text(sales_val + 2, week, f"Week {week}", fontsize=10, fontweight='bold', va='center')

plt.tight_layout()
plt.show()