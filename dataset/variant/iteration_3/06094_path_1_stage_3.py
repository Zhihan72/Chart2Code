import numpy as np
import matplotlib.pyplot as plt

skills = ['Pilot', 'Combat', 'Negot.', 'Engin.', 'Science']
species = ['Humans', 'Cybrgs', 'Xenos', 'Avians']

performance = np.array([
    [8, 6, 7, 5, 9],  # Humans
    [9, 8, 6, 9, 7],  # Cybrgs
    [6, 10, 5, 4, 6], # Xenos
    [5, 7, 9, 6, 8]   # Avians
])

num_skills = len(skills)

def create_radar_chart(title, labels, data, categories):
    angles = np.linspace(0, 2 * np.pi, num_skills, endpoint=False).tolist()
    angles += angles[:1]

    data = np.concatenate((data, data[:, [0]]), axis=1)

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    color = '#4682B4'

    for idx, d in enumerate(data):
        ax.fill(angles, d, color=color, alpha=0.25)
        ax.plot(angles, d, color=color, linewidth=2, label=categories[idx])

    ax.xaxis.grid(True, linestyle='--')
    ax.spines['polar'].set_visible(True)
    ax.spines['polar'].set_color('#708090')

    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=10)

    plt.title(title, size=16, fontweight='bold', pad=20, va='bottom')
    plt.legend(loc='upper left', bbox_to_anchor=(1.2, 1.0), title="Species")

    plt.tight_layout()
    plt.show()

create_radar_chart(
    "Space Competition\nPerformance Assessment",
    skills, performance, species
)