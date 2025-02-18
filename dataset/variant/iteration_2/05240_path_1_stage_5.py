import matplotlib.pyplot as plt
import numpy as np

continents = ['South America', 'Asia', 'Europe', 'North America', 'Africa']
animals = ['Condors', 'Pandas', 'Tigers', 'Elephants', 'Bears', 'Kangaroos', 'Lions']

data = [
    [0, 0, 0, 0, 1.5, 2.3, 0.1],
    [0, 1.5, 1.2, 0, 0, 0.5, 3.1],
    [0, 0, 0, 0.4, 0, 1.1, 0.7],
    [1.2, 0, 0, 1.8, 0.5, 0, 0],
    [10, 0.7, 0, 0.2, 0, 2.2, 1.6]
]
data_transposed = np.array(data).T

reference_index = 0  # Using 'Condors' as the reference
reference_data = data_transposed[reference_index]

# New set of colors for positive and negative bars for additional animals
colors_pos = ['#007f7f', '#b22222', '#ff69b4', '#8a2be2', '#ff4500', '#32cd32', '#6495ed']
colors_neg = ['#afeeee', '#ffb6c1', '#dda0dd', '#c2c2c2', '#ffd700', '#90ee90', '#add8e6']

fig, ax = plt.subplots(figsize=(12, 8))

for idx, (animal_data, positive_color, negative_color) in enumerate(zip(data_transposed, colors_pos, colors_neg)):
    if idx == reference_index:
        continue
    
    diff_data = animal_data - reference_data
    positive_diff = np.clip(diff_data, 0, None)
    negative_diff = np.clip(diff_data, None, 0)
    
    ax.bar(continents, positive_diff, label=f'{animals[idx]} vs {animals[reference_index]}', color=positive_color)
    ax.bar(continents, negative_diff, color=negative_color)

for continent_idx, (cont_pos, cont_neg) in enumerate(zip(positive_diff, negative_diff)):
    if cont_pos > 0:
        ax.text(continent_idx, cont_pos / 2, f'{cont_pos:.1f}', ha='center', va='center', color='white', fontsize=9, fontweight='bold')
    if cont_neg < 0:
        ax.text(continent_idx, cont_neg / 2, f'{cont_neg:.1f}', ha='center', va='center', color='white', fontsize=9, fontweight='bold')

ax.axhline(0, color='black', linewidth=0.8)
ax.set_title('Animal Revival Numbers Comparison by Continent (2015-2025)', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Continents', fontsize=12, labelpad=15)
ax.set_ylabel('Population Change (Relative to Condors, Thousands)', fontsize=12, labelpad=15)
ax.legend(title='Animal Comparison', loc='best')
ax.yaxis.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()
plt.show()