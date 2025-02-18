import matplotlib.pyplot as plt
import numpy as np

# Updated years to include an additional year
years = np.arange(2018, 2024)

# Original data
water = np.array([50, 55, 60, 65, 70, 75])
coffee = np.array([20, 22, 24, 28, 30, 33])
tea = np.array([15, 16, 18, 20, 22, 25])
soda = np.array([10, 12, 14, 16, 18, 20])

# Additional made-up data series
juice = np.array([5, 6, 7, 8, 9, 10])
milk = np.array([10, 11, 12, 13, 14, 16])

# Updated data to include the additional series
data = np.vstack([water, coffee, tea, soda, juice, milk])

# Updated color list to accommodate new groups
colors = ['#add8e6', '#98fb98', '#8a735b', '#ffb6c1', '#ffdda0', '#c9c0bb']

fig, ax = plt.subplots(figsize=(12, 8))

# Updated plotting with new data series
ax.stackplot(years, data, colors=colors, alpha=0.8, linestyle='-', linewidth=2)

ax.set_xticks(years)
ax.set_yticks(np.arange(0, 201, 20))
ax.set_ylim(0, 200)  # Updated Y-axis limit to account for the new data

ax.grid(axis='both', linestyle=':', linewidth=0.5)
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()