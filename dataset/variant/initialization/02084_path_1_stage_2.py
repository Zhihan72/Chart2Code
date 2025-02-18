import matplotlib.pyplot as plt
import numpy as np

countries = ['Australia', 'Brazil', 'China', 'Germany', 'India', 'Japan', 'South Africa', 'Spain', 'United States']
renewable_percentages = [41, 83, 35, 48, 28, 25, 18, 45, 20]
co2_reduction = [37, 78, 32, 52, 20, 15, 12, 38, 10]

colors = plt.cm.Greens(np.linspace(0.4, 0.9, len(countries)))

fig, ax1 = plt.subplots(figsize=(14, 8))

bars = ax1.barh(countries, renewable_percentages, color=colors, edgecolor='black', height=0.6)
ax1.set_xlabel('Renewable Energy (%)', fontsize=12)
ax1.set_xlim(0, 100)
ax1.set_yticks(np.arange(len(countries)))
ax1.set_yticklabels(countries, fontsize=12)
ax1.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
ax1.bar_label(bars, fmt='%.0f%', padding=3, fontsize=11)

ax2 = ax1.twiny()
ax2.plot(co2_reduction, countries, 'o-', color='blue', markerfacecolor='white', markersize=8, linewidth=2, label='Emission Cuts (%)')
ax2.set_xlabel('Reduction in CO2 Emissions (%)', fontsize=12)
ax2.set_xlim(0, 100)
ax2.xaxis.label.set_color('blue')
ax2.tick_params(axis='x', colors='blue')

ax1.set_title('2023 Countries: Renewable & Emission Cuts', fontsize=16, fontweight='bold', pad=20)

fig.legend(loc='upper right', bbox_to_anchor=(0.9, 0.9), fontsize=12)

plt.tight_layout()
plt.show()