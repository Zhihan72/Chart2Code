import matplotlib.pyplot as plt
import numpy as np

# Data
fruits = ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Strawberries']
children_preferences = [30, 20, 15, 25, 10]
adults_preferences = [25, 15, 30, 20, 10]

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.4
indices = np.arange(len(fruits))
children_index = indices - bar_width/2
adults_index = indices + bar_width/2

bars_children = ax.bar(children_index, children_preferences, width=bar_width, label='Children', color='#8A2BE2', edgecolor='black', linestyle='-.', hatch='/')
bars_adults = ax.bar(adults_index, adults_preferences, width=bar_width, label='Adults', color='#FFD700', edgecolor='black', linestyle='--', hatch='\\')

ax.set_title("Fruit Preferences among Children and Adults", fontsize=18, fontweight='light', pad=10)
ax.set_xlabel("Fruits", fontsize=13, fontstyle='italic')
ax.set_ylabel("Preferences (%)", fontsize=13, fontstyle='italic')

ax.set_xticks(indices)
ax.set_xticklabels(fruits, fontsize=11, rotation=15)

for bars in (bars_children, bars_adults):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5), textcoords="offset points",
                    ha='center', va='bottom', fontsize=11, fontweight='bold', color='blue')

ax.legend(title='Group', fontsize=12, title_fontsize='13', loc='upper left')

ax.yaxis.grid(True, linestyle='-', alpha=0.5)

plt.tight_layout()

plt.show()