import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
agri_gdp = [5.5, 6.0, 6.8, 7.2]
manu_gdp = [4.4, 4.9, 5.5, 6.1]
serv_gdp = [6.2, 6.7, 7.1, 7.5]

# Cumulative GDP without tech_gdp
cumulative_gdp = np.cumsum([sum(x) for x in zip(agri_gdp, manu_gdp, serv_gdp)])

fig, ax1 = plt.subplots(figsize=(14, 7))

width = 0.2
x_indices = np.arange(len(quarters))

ax1.bar(x_indices - width, agri_gdp, width=width, color='tab:green')
ax1.bar(x_indices, manu_gdp, width=width, color='tab:blue')
ax1.bar(x_indices + width, serv_gdp, width=width, color='tab:orange')

ax1.set_title('Planet X GDP (2023)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Qtr', fontsize=12)
ax1.set_ylabel('GDP (bil)', fontsize=12)
ax1.set_xticks(x_indices)
ax1.set_xticklabels(quarters)

ax2 = ax1.twinx()
ax2.plot(x_indices, cumulative_gdp, color='black', marker='o', linestyle='-', linewidth=2)

for i, val in enumerate(cumulative_gdp):
    ax2.text(i, val, f'{val:.1f}', color='black', fontsize=10, ha='center', va='bottom')

plt.tight_layout()
plt.show()