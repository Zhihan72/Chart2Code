import matplotlib.pyplot as plt
import numpy as np

planets = ['Earth', 'Mars', 'Jupiter', 'Neptune', 'Saturn', 'Venus']
food_categories = ['Fruits', 'Vegetables', 'Meat', 'Dairy', 'Grains']
preferences = [
    [30, 25, 20, 15, 10],  # Earth
    [10, 10, 40, 30, 10],  # Mars
    [15, 20, 30, 20, 15],  # Jupiter
    [20, 30, 20, 10, 20],  # Neptune
    [25, 15, 25, 20, 15],  # Saturn
    [20, 25, 25, 15, 15],  # Venus
]
colors = ['#FFD700', '#32CD32', '#FF6347', '#87CEFA', '#D2B48C']

# Create subplots for each planet
fig, axes = plt.subplots(1, 6, figsize=(24, 6), subplot_kw=dict(aspect="equal"))
fig.suptitle('Galactic Food Preferences Survey:\nA Study Across Different Planets', fontsize=16, fontweight='bold', y=1.02)

for i, ax in enumerate(axes.flat):
    wedges, texts, autotexts = ax.pie(
        preferences[i], labels=food_categories, autopct='%1.1f%%',
        startangle=140, colors=colors, pctdistance=0.85,
        wedgeprops=dict(width=0.3), explode=[0.05 if j == 0 else 0 for j in range(len(food_categories))],
        shadow=True
    )

    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(centre_circle)

    for text in texts:
        text.set_fontsize(10)
        text.set_color('black')

    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(9)
        autotext.set_weight('bold')

    ax.set_title(planets[i], fontsize=14, pad=15)

handles = [plt.Line2D([0], [0], color=colors[k], lw=4) for k in range(len(food_categories))]
fig.legend(handles, food_categories, loc='upper center', ncol=5, frameon=False, fontsize=12, title='Food Categories', title_fontsize=12)

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.show()