import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2018, 2023)

water = np.array([50, 55, 60, 65, 70])
coffee = np.array([20, 22, 24, 28, 30])
tea = np.array([15, 16, 18, 20, 22])
soda = np.array([10, 12, 14, 16, 18])

data = np.vstack([water, coffee, tea, soda])

fig, ax = plt.subplots(figsize=(12, 8))

# Altered the marker types and line styles for each data group
ax.stackplot(years, data, labels=['Water', 'Coffee', 'Tea', 'Soda'],
             colors=['#add8e6', '#98fb98', '#8a735b', '#ffb6c1'], alpha=0.8, linestyle='-', linewidth=2)

# Random alterations in aesthetics
ax.set_title('Beverage Consumption Trends in Aquaville\n(2018-2022)', fontsize=18, fontweight='normal', pad=10)
ax.set_xlabel('Year', fontsize=14, fontstyle='italic')
ax.set_ylabel('Avg. Monthly Consumption (liters)', fontsize=14, fontstyle='italic')
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 201, 20))
ax.set_ylim(0, 170)

# Altered legend and grid settings
ax.legend(loc='upper right', fontsize=12, title='Beverages', title_fontsize='13', shadow=True)
ax.grid(axis='both', linestyle=':', linewidth=0.5)
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()