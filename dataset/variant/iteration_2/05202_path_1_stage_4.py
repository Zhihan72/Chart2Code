import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2020', '2021', '2022']
org_A = np.array([20, 30, 50, 70, 90])
org_B = np.array([15, 25, 40, 55, 75])
carbon_offset = np.array([200, 300, 450, 600, 750])

fig, ax1 = plt.subplots(figsize=(12, 8))

height = 0.2
y = np.arange(len(years))

# Changed color for organization A's bar to '#FF5733'
ax1.barh(y - height/2, org_A, height, color='#FF5733')

# Changed color for organization B's bar to '#33C1FF'
ax1.barh(y + height/2, org_B, height, color='#33C1FF')

ax1.set_title('Forest Conservation Efforts by Organizations\n(2018-2022)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Trees Planted (Thousands)', fontsize=12)
ax1.set_ylabel('Year', fontsize=12)
ax1.set_yticks(y)
ax1.set_yticklabels(years, fontsize=12)

ax2 = ax1.twiny()

# Using a consistent color theme. Changed line color to 'gold' and marker to red.
ax2.plot(carbon_offset, y, color='gold', marker='o', linestyle='--', linewidth=2)
ax2.set_xlabel('Carbon Offset (Tonnes)', fontsize=12, color='gold')
ax2.spines['top'].set_color('gold')

plt.tight_layout()
plt.show()