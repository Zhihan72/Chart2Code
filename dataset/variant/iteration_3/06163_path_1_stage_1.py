import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2018, 2023)

water = np.array([50, 55, 60, 65, 70])
coffee = np.array([20, 22, 24, 28, 30])
tea = np.array([15, 16, 18, 20, 22])
soda = np.array([10, 12, 14, 16, 18])

data = np.vstack([water, coffee, tea, soda])

fig, ax = plt.subplots(figsize=(12, 8))

# Manually shuffled the colors for each data group
ax.stackplot(years, data, labels=['Water', 'Coffee', 'Tea', 'Soda'],
             colors=['#ffb6c1', '#add8e6', '#8a735b', '#98fb98'], alpha=0.8)

ax.set_title('Beverage Consumption Trends in Aquaville\n(2018-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Monthly Consumption (liters)', fontsize=12)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 201, 20))
ax.set_ylim(0, 170)

ax.legend(loc='upper left', fontsize=10, title='Beverages')
ax.grid(axis='x', linestyle='--', alpha=0.7)
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()