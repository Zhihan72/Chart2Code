import numpy as np
import matplotlib.pyplot as plt

novels = [
    "The Forgotten Realm", 
    "Ember's Tales", "Kingdom's Oath", "Myth's End"
]
categories = ['Geography', 'Magic System', 'Cultural Complexity', 'Political Intrigue', 'Mythology']

data = np.array([
    [8, 7, 6, 5, 9],
    [7, 6, 8, 5, 7],
    [6, 5, 9, 8, 6],
    [9, 8, 5, 7, 9]
])

num_vars = len(categories)

def create_radar_chart(data, num_vars):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data = np.concatenate((data, data[:, [0]]), axis=1)
    angles += angles[:1]
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    styles = [
        {'color': '#FF9999', 'marker': 'o', 'linestyle': '-'},
        {'color': '#99CCFF', 'marker': 's', 'linestyle': '--'},
        {'color': '#FF66B3', 'marker': 'd', 'linestyle': '-.'},
        {'color': '#C2F0C2', 'marker': '^', 'linestyle': ':'}
    ]

    for d, style in zip(data, styles):
        ax.plot(angles, d, color=style['color'], marker=style['marker'], linestyle=style['linestyle'], alpha=0.7)
        ax.fill(angles, d, color=style['color'], alpha=0.3)

    ax.set_yticks([])
    ax.set_xticks(angles[:-1])
    ax.spines['polar'].set_visible(True)
    ax.grid(linestyle=':', linewidth=0.5, alpha=0.7)

    plt.tight_layout()
    plt.legend(novels, loc='upper right', bbox_to_anchor=(1.1, 1.1))
    plt.show()

create_radar_chart(data, num_vars)