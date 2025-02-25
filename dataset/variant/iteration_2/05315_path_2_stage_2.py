import matplotlib.pyplot as plt
import numpy as np

fruits = ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Strawberries']
children_preferences = [30, 20, 15, 25, 10]
adults_preferences = [25, 15, 30, 20, 10]

combined_preferences = list(zip(children_preferences, adults_preferences, fruits))
combined_preferences.sort(reverse=True)

sorted_children_preferences, sorted_adults_preferences, sorted_fruits = zip(*combined_preferences)

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.4
indices = np.arange(len(sorted_fruits))
children_index = indices - bar_width/2
adults_index = indices + bar_width/2

# Applying the same color to both groups
bar_color = '#FFA07A'
ax.bar(children_index, sorted_children_preferences, width=bar_width, label='Children', color=bar_color)
ax.bar(adults_index, sorted_adults_preferences, width=bar_width, label='Adults', color=bar_color)

ax.set_title("Fruit Preferences among Children and Adults in the Community", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Fruits", fontsize=14)
ax.set_ylabel("Preferences (%)", fontsize=14)
ax.set_xticks(indices)
ax.set_xticklabels(sorted_fruits, fontsize=12)

for i in range(len(sorted_fruits)):
    ax.annotate(f'{sorted_children_preferences[i]}%',
                xy=(children_index[i], sorted_children_preferences[i]),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10)
    ax.annotate(f'{sorted_adults_preferences[i]}%',
                xy=(adults_index[i], sorted_adults_preferences[i]),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10)

ax.legend(title='Age Group')
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()