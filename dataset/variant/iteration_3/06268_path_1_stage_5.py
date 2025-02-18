import matplotlib.pyplot as plt
import numpy as np

years = ['2020', '2021', '2018', '2019']
genres = ['Puzzle', 'Action', 'RPG', 'Sports']

units_sold = {
    'Puzzle': [90, 100, 110, 120],
    'Action': [150, 180, 200, 230],
    'RPG': [80, 85, 90, 95],
    'Sports': [110, 115, 120, 125]
}

# Changed colors to vary the palette style
colors = ['#ff6666', '#66ccff', '#99ff99', '#ffcc99']

fig, ax1 = plt.subplots(figsize=(12, 8))

index = np.arange(len(years))
cumulative_values = np.zeros(len(years))

# Changed bar styles, marker types and their arrangement stylistically
for i, (genre, values) in enumerate(units_sold.items()):
    ax1.bar(index, values, label=genre, color=colors[i], hatch='/' if i % 2 == 0 else '\\', edgecolor='black', alpha=0.9, bottom=cumulative_values)
    cumulative_values += np.array(values)

# Updated font size, weight, and style elements
ax1.set_xlabel('Timeline', fontsize=14, weight='light')
ax1.set_ylabel('Thousands of Units Sold', fontsize=14, weight='light')
ax1.set_title('Distribution of Game Sales by Genre', fontsize=18, style='italic', pad=15)
ax1.set_xticks(index)
ax1.set_xticklabels(years, fontsize=12, weight='light')

# Changed legend and grid properties
ax1.legend(title='Game Types', fontsize=11, title_fontsize='13', loc='upper center')
ax1.grid(axis='y', linestyle=':', alpha=0.85)

# Removed borders from the plot to give it a cleaner look
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()