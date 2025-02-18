import matplotlib.pyplot as plt
import numpy as np

# Altered Backstory: An overview of animal number revival in different continents over several years post protective actions.
continents = ['South America', 'Asia', 'Europe', 'North America', 'Africa']
animals = ['Condors', 'Pandas', 'Tigers', 'Elephants', 'Bears']

# Population increase data (in thousands)
data = [
    [0, 0, 0, 0, 1.5],
    [0, 1.5, 1.2, 0, 0],
    [0, 0, 0, 0.4, 0],
    [1.2, 0, 0, 1.8, 0.5],
    [10, 0.7, 0, 0.2, 0]
]
data_transposed = np.array(data).T

colors = ['#8e44ad', '#52c94c', '#4c8ec9', '#c94c4c', '#c9b34c']

fig, ax = plt.subplots(figsize=(12, 8))

bottom_values = np.zeros(len(continents))
for idx, (animal_data, color) in enumerate(zip(data_transposed, colors)):
    ax.bar(continents, animal_data, label=animals[idx], color=color, bottom=bottom_values, edgecolor='black')
    bottom_values += animal_data

for continent_idx, continent_data in enumerate(data):
    bottom = 0
    for animal_idx, value in enumerate(continent_data):
        if value > 0:
            ax.text(continent_idx, bottom + value / 2, f'{value}', ha='center', va='center', color='white', fontsize=9, fontweight='bold')
        bottom += value

# Altered Chart configurations
ax.set_title('Animal Number Revival Post Protective Efforts (2015-2025)', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Continents', fontsize=12, labelpad=15)
ax.set_ylabel('Increased Population (Thousands)', fontsize=12, labelpad=15)
ax.legend(title='Animals', loc='upper left', bbox_to_anchor=(1.05, 1))
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()