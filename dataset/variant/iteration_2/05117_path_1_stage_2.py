import matplotlib.pyplot as plt
import numpy as np

# Categories and data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
cats = [20, 25, 30, 35, 40, 45]
dogs = [30, 35, 40, 45, 50, 55]
fish = [15, 18, 22, 25, 28, 30]
birds = [10, 12, 15, 20, 25, 28]

fig, ax = plt.subplots(figsize=(12, 7))

# Bar details
y = np.arange(len(months))
bar_height = 0.2

# Create horizontal bars
bars_cats = ax.barh(y - 3*bar_height/2, cats, height=bar_height, label='Cats', color='lightblue')
bars_dogs = ax.barh(y - bar_height/2, dogs, height=bar_height, label='Dogs', color='lightyellow')
bars_fish = ax.barh(y + bar_height/2, fish, height=bar_height, label='Fish', color='lightcoral')
bars_birds = ax.barh(y + 3*bar_height/2, birds, height=bar_height, label='Birds', color='lightgreen')

ax.set_title('Community Pet Adoption Trends\n(Number of Pets Adopted per Month)', fontsize=15, fontweight='bold', pad=15)
ax.set_xlabel('Number of Adoptions', fontsize=12)
ax.set_ylabel('Month', fontsize=12)

ax.set_yticks(y)
ax.set_yticklabels(months, fontsize=10)
ax.grid(axis='x', linestyle='--', alpha=0.6)

ax.legend(title='Pet Type', loc='upper right', fontsize=10)

def add_value_labels(bars):
    for bar in bars:
        width = bar.get_width()
        ax.annotate(f'{width}',
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(3, 0),
                    textcoords="offset points",
                    ha='left', va='center', fontsize=9)

add_value_labels(bars_cats)
add_value_labels(bars_dogs)
add_value_labels(bars_fish)
add_value_labels(bars_birds)

plt.tight_layout()
plt.show()