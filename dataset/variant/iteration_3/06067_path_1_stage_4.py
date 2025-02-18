import numpy as np
import matplotlib.pyplot as plt

categories = ['Vitamin C', 'Fiber', 'Antioxidants', 'Natural Sugars', 'Water Content']
fruits = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Blueberry']

data = {
    'Apple': [7, 6, 8, 8, 9],
    'Banana': [5, 5, 6, 9, 8],
    'Orange': [9, 6, 7, 7, 8],
    'Strawberry': [8, 7, 9, 5, 9],
    'Blueberry': [8, 7, 10, 5, 9]
}

num_vars = len(categories)

def create_radar_chart(ax, data, color):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data += data[:1]
    angles += angles[:1]
    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, color=color, linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks([])

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

single_color = '#FF9999'  # Chosen color for all data groups

for fruit in fruits:
    create_radar_chart(ax, data[fruit], single_color)

plt.show()