import matplotlib.pyplot as plt
import numpy as np

years = ['Anno 2018', 'Year 2019', 'Yr 2020', '2021 AD', 'Year 2022']
org_A = np.array([20, 30, 50, 70, 90])
org_B = np.array([15, 25, 40, 55, 75])
org_C = np.array([10, 20, 30, 50, 65])
org_D = np.array([5, 10, 20, 35, 50]) 
carbon_offset = np.array([200, 300, 450, 600, 750])

fig, ax1 = plt.subplots(figsize=(12, 8))

width = 0.15  
x = np.arange(len(years))

ax1.bar(x - 1.5*width, org_A, width, color='#79C753')
ax1.bar(x - 0.5*width, org_B, width, color='#4CAF50')
ax1.bar(x + 0.5*width, org_C, width, color='#2E7D32')
ax1.bar(x + 1.5*width, org_D, width, color='#1B5E20')

ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=12)

# Adding a secondary y-axis for carbon offset impact
ax2 = ax1.twinx()
ax2.plot(years, carbon_offset, color='dodgerblue', marker='o', linestyle='--', linewidth=2)
ax2.set_ylabel('Offset (Tons)', fontsize=12, color='dodgerblue')
ax2.spines['right'].set_color('dodgerblue')

plt.tight_layout()
plt.show()