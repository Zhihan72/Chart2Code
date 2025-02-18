import numpy as np
import matplotlib.pyplot as plt

novels = [
    "The Forgotten Realm", 
    "Ember's Tales", "Kingdom's Oath", "Myth's End"
]
categories = ['Geography', 'Magic System', 'Cultural Complexity', 'Political Intrigue', 'Mythology']

data = np.array([
    [8, 7, 6, 5, 9],  # The Forgotten Realm
    [7, 6, 8, 5, 7],  # Ember's Tales
    [6, 5, 9, 8, 6],  # Kingdom's Oath
    [9, 8, 5, 7, 9]   # Myth's End
])

num_vars = len(categories)

def create_radar_chart(data, num_vars):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data = np.concatenate((data, data[:, [0]]), axis=1)
    angles += angles[:1]
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    colors = ['#FFCC99', '#FF9999', '#C2C2F0', '#99FF99']
    for d, color in zip(data, colors):
        ax.fill(angles, d, color=color, alpha=0.5)

    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])

    plt.tight_layout()
    plt.show()

create_radar_chart(data, num_vars)