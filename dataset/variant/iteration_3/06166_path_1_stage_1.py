import matplotlib.pyplot as plt
import numpy as np

categories = ['Strength', 'Intelligence', 'Speed', 'Durability', 'Power', 'Combat Skills']
num_vars = len(categories)

# Modified data for each superhero with manually altered traits
superheroes = {
    'Superman': [8, 6, 10, 7, 9, 8],
    'Batman': [5, 8, 5, 6, 7, 8],
    'Wonder Woman': [9, 7, 8, 6, 9, 7],
    'Flash': [7, 5, 9, 4, 6, 7],
    'Aquaman': [7, 6, 7, 7, 6, 7],
}

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def plot_radar(data, title):
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    plt.xticks(angles[:-1], categories, fontsize=12)
    ax.set_rscale('linear')
    ax.set_rlabel_position(0)
    plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)
    plt.ylim(0, 10)

    colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#6A5ACD']
    
    for color, (hero, values) in zip(colors, data.items()):
        values += values[:1]
        ax.fill(angles, values, color=color, alpha=0.25, label=hero)
        ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')

    plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=12)
    plt.title(title, size=16, color='darkblue', y=1.1, weight='bold', ha='center')
    plt.tight_layout()
    plt.show()

plot_radar(superheroes, "Comparison of Core Superhero Traits\nAnnual Review 2023")