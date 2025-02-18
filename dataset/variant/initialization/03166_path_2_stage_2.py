import matplotlib.pyplot as plt
import numpy as np

countries = ['Finland', 'Sweden', 'Brazil', 'Iceland', 'Denmark', 
             'Switzerland', 'Germany', 'Norway', 'USA', 'Italy']
consumption = np.array([12.0, 10.5, 5.0, 9.0, 8.5, 7.9, 6.5, 9.8, 4.5, 4.0])

color_map = plt.get_cmap("YlGnBu")
colors = color_map(np.linspace(0.3, 0.9, len(countries)))

colors_shuffled = [
    colors[3], colors[6], colors[8], colors[1], colors[0], 
    colors[4], colors[2], colors[9], colors[5], colors[7]
]

fig, ax = plt.subplots(figsize=(12, 8))

bars = ax.barh(countries, consumption, color=colors_shuffled, height=0.6, edgecolor='darkblue')

for bar, value in zip(bars, consumption):
    ax.text(value + 0.1, bar.get_y() + bar.get_height() / 2, f'{value:.1f} kg', 
            va='center', fontsize=9, color='darkblue')

ax.set_title('Global Coffee Culture:\nAnnual Consumption Per Capita by Country', 
             fontsize=18, color='darkgreen', weight='bold', pad=20)
ax.set_xlabel('Consumption (kg per person)', fontsize=12, color='darkolivegreen')
ax.set_ylabel('Countries', fontsize=12, color='darkolivegreen')

ax.set_xlim(0, max(consumption) + 2)
ax.xaxis.grid(True, linestyle='--', color='grey', alpha=0.4)
ax.set_axisbelow(True)

ax.set_yticks(np.arange(len(countries)))
ax.set_yticklabels(countries, fontsize=11, color='darkgreen')

plt.tight_layout()
plt.show()