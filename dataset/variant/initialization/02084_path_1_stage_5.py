import matplotlib.pyplot as plt
import numpy as np

countries = ['Australia', 'Brazil', 'China', 'Germany', 'India', 'Japan', 'South Africa', 'Spain', 'United States']
renewable_percentages = [41, 83, 35, 48, 28, 25, 18, 45, 20]
co2_reduction = [37, 78, 32, 52, 20, 15, 12, 38, 10]

# Sorting the countries and data based on renewable_percentages in descending order
sorted_indices = np.argsort(renewable_percentages)[::-1]
countries = np.array(countries)[sorted_indices]
renewable_percentages = np.array(renewable_percentages)[sorted_indices]
co2_reduction = np.array(co2_reduction)[sorted_indices]

# Applying a new set of colors using 'viridis' colormap
colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(countries)))

fig, ax1 = plt.subplots(figsize=(14, 8))

bars = ax1.barh(countries, renewable_percentages, color=colors, edgecolor='black', height=0.6)
ax1.set_xlabel('Renewable Energy (%)', fontsize=12)
ax1.set_xlim(0, 100)
ax1.set_yticks(np.arange(len(countries)))
ax1.set_yticklabels(countries, fontsize=12)
ax1.bar_label(bars, fmt='%.0f%', padding=3, fontsize=11)

ax2 = ax1.twiny()
ax2.plot(co2_reduction, countries, 'o-', color='blue', markerfacecolor='white', markersize=8, linewidth=2)
ax2.set_xlabel('Reduction in CO2 Emissions (%)', fontsize=12)
ax2.set_xlim(0, 100)
ax2.xaxis.label.set_color('blue')
ax2.tick_params(axis='x', colors='blue')

ax1.set_title('2023 Countries: Renewable & Emission Cuts', fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()