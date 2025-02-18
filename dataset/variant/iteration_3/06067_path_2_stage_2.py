import numpy as np
import matplotlib.pyplot as plt

categories = ['Vitamin C', 'Fiber', 'Antioxidants', 'Natural Sugars', 'Water Content']
fruits = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Blueberry']

# Manually shuffled data for each fruit
data = {
    'Apple': [8, 9, 7, 6, 8],
    'Banana': [6, 8, 9, 5, 5],
    'Orange': [7, 9, 6, 8, 7],
    'Strawberry': [9, 5, 8, 9, 7],
    'Blueberry': [5, 9, 8, 10, 7]
}

num_vars = len(categories)

def create_radar_chart(ax, data, color):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data += data[:1]
    angles += angles[:1]
    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, color=color, linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=11)

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

colors = ['#FF9999', '#FFE766', '#FFA07A', '#7FFFD4', '#B0E0E6']

for fruit, color in zip(fruits, colors):
    create_radar_chart(ax, data[fruit], color)

ax.set_title('Fruit Nutritional Analysis', size=16, weight='bold', pad=20)

plt.tight_layout()
plt.show()