import matplotlib.pyplot as plt
import numpy as np

years = ['Anno 2018', 'Year 2019', 'Yr 2020', '2021 AD', 'Year 2022']
org_A = np.array([20, 30, 50, 70, 90])
org_B = np.array([15, 25, 40, 55, 75])
org_C = np.array([10, 20, 30, 50, 65])
org_D = np.array([5, 10, 20, 35, 50]) 
carbon_offset = np.array([200, 300, 450, 600, 750])

fig, ax1 = plt.subplots(figsize=(12, 8))

height = 0.15  
y = np.arange(len(years))

ax1.barh(y - 1.5*height, org_A, height, color='#2E7D32')
ax1.barh(y - 0.5*height, org_B, height, color='#1B5E20')
ax1.barh(y + 0.5*height, org_C, height, color='#4CAF50')
ax1.barh(y + 1.5*height, org_D, height, color='#79C753')

ax1.set_yticks(y)
ax1.set_yticklabels(years, fontsize=12)

ax2 = ax1.twiny()
ax2.plot(carbon_offset, y, color='dodgerblue', marker='o', linestyle='--', linewidth=2)
ax2.set_xlabel('Offset (Tons)', fontsize=12, color='dodgerblue')
ax2.spines['top'].set_color('dodgerblue')

plt.tight_layout()
plt.show()