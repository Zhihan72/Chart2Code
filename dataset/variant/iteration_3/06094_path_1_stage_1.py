import numpy as np
import matplotlib.pyplot as plt

# Altered skills and species names
skills = ['Pilot Skills', 'Combat Skills', 'Negotiation', 'Engineering', 'Scientific Knowledge']
species = ['Humanoids', 'Cyborgs', 'Xenomorphs', 'Avians']

# Altered performance data
performance = np.array([
    [8, 6, 7, 5, 9],  # Humanoids
    [9, 8, 6, 9, 7],  # Cyborgs
    [6, 10, 5, 4, 6], # Xenomorphs
    [5, 7, 9, 6, 8]   # Avians
])

num_skills = len(skills)

# Function to create a radar chart
def create_radar_chart(title, labels, data, categories):
    angles = np.linspace(0, 2 * np.pi, num_skills, endpoint=False).tolist()
    angles += angles[:1]  # Complete the circle

    # Extend data for closure
    data = np.concatenate((data, data[:, [0]]), axis=1)

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Randomize colors and line styles
    colors = ['#FFD700', '#32CD32', '#FF6347', '#4682B4']
    line_styles = ['-', '--', '-.', ':']
    marker_styles = ['o', 's', 'D', '^']
    for idx, (d, color, ls, marker) in enumerate(zip(data, colors, line_styles, marker_styles)):
        ax.fill(angles, d, color=color, alpha=0.25)
        ax.plot(angles, d, color=color, linewidth=2, linestyle=ls, marker=marker, label=categories[idx])

    # Add minor grid and randomize border color
    ax.xaxis.grid(True, linestyle='--')
    ax.spines['polar'].set_visible(True)
    ax.spines['polar'].set_color('#708090')

    # Customize labels
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=10)

    plt.title(title, size=16, fontweight='bold', pad=20, va='bottom')
    plt.legend(loc='upper left', bbox_to_anchor=(1.2, 1.0), title="Species")

    plt.tight_layout()
    plt.show()

create_radar_chart(
    "Intergalactic Space Competition\nSpecies Performance Assessment",
    skills, performance, species
)