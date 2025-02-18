import matplotlib.pyplot as plt
import numpy as np

countries = ['Norway', 'Germany', 'China', 'United States', 'India', 'Brazil', 'Spain', 'Australia', 'Japan', 'South Africa']
renewable_percentages = [28, 83, 25, 35, 45, 18, 41, 48, 98, 20]

# Set a single color for all bars
single_color = 'green'

fig, ax1 = plt.subplots(figsize=(14, 8))

bars = ax1.bar(countries, renewable_percentages, color=single_color, edgecolor='black')
ax1.set_ylabel('Percentage of Energy from Renewables (%)', fontsize=12)
ax1.set_ylim(0, 100)
ax1.set_xticks(np.arange(len(countries)))
ax1.set_xticklabels(countries, rotation=45, ha='right', fontsize=12)
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
ax1.bar_label(bars, fmt='%.0f%%', padding=3, fontsize=11)

ax1.set_title('Renewable Energy Adoption by Country in 2023', fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()