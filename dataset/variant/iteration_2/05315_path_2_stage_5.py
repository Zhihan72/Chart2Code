import matplotlib.pyplot as plt
import numpy as np

fruits = ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Strawberries']
children_preferences = [30, 20, 15, 25, 10]

combined_preferences = list(zip(children_preferences, fruits))
combined_preferences.sort(reverse=True)

sorted_children_preferences, sorted_fruits = zip(*combined_preferences)

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.4
indices = np.arange(len(sorted_fruits))
children_index = indices

bar_color = '#FFA07A'
ax.bar(children_index, sorted_children_preferences, width=bar_width, color=bar_color)

ax.set_title("Fruit Choices: Kids", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Fruit", fontsize=14)
ax.set_ylabel("%", fontsize=14)
ax.set_xticks(indices)
ax.set_xticklabels(sorted_fruits, fontsize=12)

for i in range(len(sorted_fruits)):
    ax.annotate(f'{sorted_children_preferences[i]}%',
                xy=(children_index[i], sorted_children_preferences[i]),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()