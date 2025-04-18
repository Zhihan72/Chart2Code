import numpy as np
import matplotlib.pyplot as plt

skills = ['Pilot Skills', 'Combat Skills', 'Negotiation', 'Engineering', 'Scientific Knowledge']
species = ['Humanoids', 'Cyborgs', 'Xenomorphs', 'Avians']

performance = np.array([
    [8, 6, 7, 5, 9],  # Humanoids
    [9, 8, 6, 9, 7],  # Cyborgs
    [6, 10, 5, 4, 6], # Xenomorphs
    [5, 7, 9, 6, 8]   # Avians
])

num_skills = len(skills)

def create_radar_chart(title, labels, data, categories):
    angles = np.linspace(0, 2 * np.pi, num_skills, endpoint=False).tolist()
    angles += angles[:1]

    data = np.concatenate((data, data[:, [0]]), axis=1)

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    colors = ['#FF4500', '#3CB371', '#1E90FF', '#9370DB']
    for idx, (d, color) in enumerate(zip(data, colors)):
        ax.fill(angles, d, color=color, alpha=0.25)
        ax.plot(angles, d, color=color, linewidth=2)

    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=10)

    plt.title(title, size=16, fontweight='bold', pad=20, va='bottom')

    plt.tight_layout()
    plt.show()

create_radar_chart(
    "Intergalactic Space Competition\nSpecies Performance Assessment",
    skills, performance, species
)