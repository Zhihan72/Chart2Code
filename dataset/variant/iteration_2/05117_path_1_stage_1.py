import matplotlib.pyplot as plt
import numpy as np

# Categories and data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
cats = [20, 25, 30, 35, 40, 45]
dogs = [30, 35, 40, 45, 50, 55]
fish = [15, 18, 22, 25, 28, 30]
birds = [10, 12, 15, 20, 25, 28]

fig, ax = plt.subplots(figsize=(12, 7))

x = np.arange(len(months))
bar_width = 0.2

# Assigning shuffled colors to the data groups
bars_cats = ax.bar(x - 3*bar_width/2, cats, width=bar_width, label='Cats', color='lightblue')
bars_dogs = ax.bar(x - bar_width/2, dogs, width=bar_width, label='Dogs', color='lightyellow')
bars_fish = ax.bar(x + bar_width/2, fish, width=bar_width, label='Fish', color='lightcoral')
bars_birds = ax.bar(x + 3*bar_width/2, birds, width=bar_width, label='Birds', color='lightgreen')

ax.set_title('Community Pet Adoption Trends\n(Number of Pets Adopted per Month)', fontsize=15, fontweight='bold', pad=15)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Number of Adoptions', fontsize=12)

ax.set_xticks(x)
ax.set_xticklabels(months, fontsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.6)

ax.legend(title='Pet Type', loc='upper left', fontsize=10)

def add_value_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9)

add_value_labels(bars_cats)
add_value_labels(bars_dogs)
add_value_labels(bars_fish)
add_value_labels(bars_birds)

plt.tight_layout()
plt.show()