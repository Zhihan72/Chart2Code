import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2018, 2023)
water = np.array([55, 60, 50, 70, 65])
coffee = np.array([28, 22, 30, 24, 20])
tea = np.array([18, 22, 16, 15, 20])
soda = np.array([16, 12, 18, 10, 14])

data = np.vstack([water, coffee, tea, soda])

fig, ax = plt.subplots(figsize=(12, 8))

# Randomly altered colors for demonstration
ax.stackplot(years, data, colors=['#ffb6c1', '#98fb98', '#8a735b', '#add8e6'], alpha=0.8)

# Randomly altered titles and labels
ax.set_title('Drink Usage Patterns in Waterville\n(2018-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=12)
ax.set_ylabel('Monthly Average Use (liters)', fontsize=12)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 201, 20))
ax.set_ylim(0, 170)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()