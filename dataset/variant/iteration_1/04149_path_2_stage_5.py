import matplotlib.pyplot as plt
import numpy as np

quarters = ['Q1', 'Q2', 'Q3', 'Q4']
agri_gdp = [5.5, 6.0, 6.8, 7.2]
manu_gdp = [4.4, 4.9, 5.5, 6.1]
serv_gdp = [6.2, 6.7, 7.1, 7.5]

# Calculate total GDP for each quarter
total_gdp = [sum(x) for x in zip(agri_gdp, manu_gdp, serv_gdp)]

# Sort the data in descending order by total GDP
sorted_indices = np.argsort(total_gdp)[::-1]
sorted_quarters = [quarters[i] for i in sorted_indices]
sorted_agri_gdp = [agri_gdp[i] for i in sorted_indices]
sorted_manu_gdp = [manu_gdp[i] for i in sorted_indices]
sorted_serv_gdp = [serv_gdp[i] for i in sorted_indices]
sorted_total_gdp = [total_gdp[i] for i in sorted_indices]

fig, ax1 = plt.subplots(figsize=(14, 7))

width = 0.2
x_indices = np.arange(len(quarters))

ax1.bar(x_indices - width, sorted_agri_gdp, width=width, color='#FF5733')
ax1.bar(x_indices, sorted_manu_gdp, width=width, color='#33B5E5')
ax1.bar(x_indices + width, sorted_serv_gdp, width=width, color='#EDAE49')

ax1.set_title('Planet X GDP (2023) - Sorted by Total GDP', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Qtr', fontsize=12)
ax1.set_ylabel('GDP (bil)', fontsize=12)
ax1.set_xticks(x_indices)
ax1.set_xticklabels(sorted_quarters)

ax2 = ax1.twinx()
ax2.plot(x_indices, np.cumsum(sorted_total_gdp), color='black', marker='o', linestyle='-', linewidth=2)

for i, val in enumerate(np.cumsum(sorted_total_gdp)):
    ax2.text(i, val, f'{val:.1f}', color='black', fontsize=10, ha='center', va='bottom')

plt.tight_layout()
plt.show()