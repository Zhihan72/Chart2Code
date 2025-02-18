import matplotlib.pyplot as plt
import numpy as np

fruits = ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Strawberries']
children_preferences = [30, 20, 15, 25, 10]

# Sort the data in ascending order
sorted_indices = np.argsort(children_preferences)
sorted_fruits = [fruits[i] for i in sorted_indices]
sorted_preferences = [children_preferences[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.4
indices = np.arange(len(fruits))
children_index = indices

bars_children = ax.bar(children_index, sorted_preferences, width=bar_width, label='Children', color='#FF6347', edgecolor='black', linestyle='-.', hatch='/')

ax.set_title("Fruit Preferences among Children", fontsize=18, fontweight='light', pad=10)
ax.set_xlabel("Fruits", fontsize=13, fontstyle='italic')
ax.set_ylabel("Preferences (%)", fontsize=13, fontstyle='italic')

ax.set_xticks(indices)
ax.set_xticklabels(sorted_fruits, fontsize=11, rotation=15)

for bar in bars_children:
    height = bar.get_height()
    ax.annotate(f'{height}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5), textcoords="offset points",
                ha='center', va='bottom', fontsize=11, fontweight='bold', color='blue')

ax.legend(title='Group', fontsize=12, title_fontsize='13', loc='upper left')

ax.yaxis.grid(True, linestyle='-', alpha=0.5)

plt.tight_layout()

plt.show()