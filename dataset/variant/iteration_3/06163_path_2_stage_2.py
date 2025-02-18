import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2018, 2023)
water = np.array([55, 60, 50, 70, 65])
coffee = np.array([28, 22, 30, 24, 20])
tea = np.array([18, 22, 16, 15, 20])
soda = np.array([16, 12, 18, 10, 14])

data = np.vstack([water, coffee, tea, soda])

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, data, colors=['#add8e6', '#8a735b', '#98fb98', '#ffb6c1'], alpha=0.8)

ax.set_title('Beverage Consumption Trends in Aquaville\n(2018-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Monthly Consumption (liters)', fontsize=12)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 201, 20))
ax.set_ylim(0, 170)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()