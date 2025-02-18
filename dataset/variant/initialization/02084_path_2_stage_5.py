import matplotlib.pyplot as plt
import numpy as np

countries = ['Nor', 'Ger', 'Chn', 'USA', 'Ind', 'Bra', 'Esp', 'Aus', 'Jpn', 'SA']
renewable_percentages = [28, 83, 25, 35, 45, 18, 41, 48, 98, 20]

# Set different colors for bars
bar_colors = ['blue', 'red', 'green', 'purple', 'orange', 'cyan', 'magenta', 'yellow', 'pink', 'grey']

fig, ax1 = plt.subplots(figsize=(14, 8))

bars = ax1.bar(countries, renewable_percentages, color=bar_colors, edgecolor='white')
ax1.set_ylabel('Renewable %', fontsize=14, fontstyle='italic')
ax1.set_ylim(0, 100)
ax1.set_xticks(np.arange(len(countries)))
ax1.set_xticklabels(countries, rotation=30, ha='right', fontsize=10)
ax1.xaxis.grid(True, linestyle='-.', which='both', color='mistyrose', alpha=0.5)
ax1.yaxis.grid(True, linestyle=':', which='both', color='lightgrey', alpha=0.7)
ax1.bar_label(bars, fmt='%.0f%%', padding=3, fontsize=12, fontweight='bold')

ax1.set_title('Renewable Energy 2023', fontsize=18, fontweight='bold', color='darkblue', pad=25)

# Randomly choosing from available markers for line plot
ax1.plot(renewable_percentages, linestyle='--', marker='o', color='darkgreen', markersize=8)

plt.tight_layout()
plt.show()