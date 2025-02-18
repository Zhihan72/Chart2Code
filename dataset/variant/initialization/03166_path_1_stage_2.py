import matplotlib.pyplot as plt
import numpy as np

countries = ['Finland', 'Sweden', 'Norway', 'Iceland', 'Denmark', 
             'Switzerland', 'Germany', 'Brazil', 'USA', 'Italy']
consumption = np.array([12.0, 10.5, 9.8, 9.0, 8.5, 7.9, 6.5, 5.0, 4.5, 4.0])

# Sort the data in descending order
sorted_indices = np.argsort(-consumption)
sorted_countries = [countries[i] for i in sorted_indices]
sorted_consumption = consumption[sorted_indices]

color_map = plt.get_cmap("coolwarm")
colors = color_map(np.linspace(0.3, 0.9, len(countries)))

fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.barh(sorted_countries, sorted_consumption, color=colors, height=0.6, edgecolor='grey', linestyle='-.')

for bar, value in zip(bars, sorted_consumption):
    ax.text(value + 0.2, bar.get_y() + bar.get_height() / 2, f'{value:.1f} kg', 
            va='center', fontsize=10, color='black', weight='bold')

ax.set_title('Annual Coffee Consumption by Country', fontsize=18, color='navy', pad=20)
ax.set_xlabel('Consumption (kg per person)', fontsize=12, color='slateblue')
ax.set_ylabel('Countries', fontsize=12, color='slateblue')

ax.set_xlim(0, max(sorted_consumption) + 2)
ax.xaxis.grid(True, linestyle=':', color='lightgray', alpha=0.6)
ax.set_axisbelow(True)

ax.set_yticks(np.arange(len(sorted_countries)))
ax.set_yticklabels(sorted_countries, fontsize=11, color='navy')

plt.tight_layout()

plt.show()