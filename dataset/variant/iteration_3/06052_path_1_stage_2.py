import matplotlib.pyplot as plt
import numpy as np

categories = ['Electronics', 'Furniture', 'Clothing', 'Books', 'Toys', 'Groceries']
sales = [150, 90, 130, 80, 120, 170]
satisfaction_rates = [85, 75, 70, 60, 80, 90]

# Shuffle the colors manually
colors = ['#2ca02c', '#9467bd', '#1f77b4', '#8c564b', '#ff7f0e', '#d62728']

fig, ax1 = plt.subplots(figsize=(12, 8))

x_pos = np.arange(len(categories))

ax1.bar(x_pos, sales, color=colors, alpha=0.7)

ax2 = ax1.twinx()
ax2.plot(x_pos, satisfaction_rates, 'o-', color='green', markersize=10)

fig.tight_layout()

plt.show()