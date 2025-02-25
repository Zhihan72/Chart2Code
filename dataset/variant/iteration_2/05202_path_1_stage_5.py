import matplotlib.pyplot as plt
import numpy as np

years = ['2021', '2020', '2019', '2022', '2018']  # Random year order
org_A = np.array([20, 30, 50, 70, 90])
org_B = np.array([15, 25, 40, 55, 75])
carbon_offset = np.array([200, 300, 450, 600, 750])

fig, ax1 = plt.subplots(figsize=(12, 8))

height = 0.2
y = np.arange(len(years))

ax1.barh(y - height/2, org_A, height, color='#FF5733')
ax1.barh(y + height/2, org_B, height, color='#33C1FF')

ax1.set_title('Efforts in Forest Areas by Various Groups\n(2021-2018)', fontsize=16, fontweight='bold', pad=20)  # Modified title
ax1.set_xlabel('Plants Increased (x1000)', fontsize=12)  # Modified x-axis label
ax1.set_ylabel('Year Category', fontsize=12)  # Modified y-axis label
ax1.set_yticks(y)
ax1.set_yticklabels(years, fontsize=12)

ax2 = ax1.twiny()
ax2.plot(carbon_offset, y, color='gold', marker='o', linestyle='--', linewidth=2)
ax2.set_xlabel('CO2 Compensation (kTonnes)', fontsize=12, color='gold')  # Modified x-axis label
ax2.spines['top'].set_color('gold')

plt.tight_layout()
plt.show()