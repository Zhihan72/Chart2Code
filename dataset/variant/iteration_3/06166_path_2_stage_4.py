import matplotlib.pyplot as plt
import numpy as np

categories = ['Brains', 'Muscle', 'Speediness', 'Stamina', 'Might', 'Fight Skills']
num_vars = len(categories)

superheroes = {
    'Steelman': [9, 7, 9, 8, 10, 7],
    'Dark Knight': [4, 9, 6, 5, 6, 9],
    'Amazon Warrior': [8, 8, 7, 7, 8, 9],
    'Sprinter': [6, 6, 10, 5, 7, 6],
}

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def plot_radar_no_style(data, title):
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    plt.xticks(angles[:-1], categories, fontsize=12)
    ax.set_rscale('linear')
    ax.set_rlabel_position(0)
    plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)
    plt.ylim(0, 10)

    single_color = '#4682B4'  # Choose a single color for all data groups

    for hero, values in data.items():
        values += values[:1]
        ax.fill(angles, values, color=single_color, alpha=0.25)
        ax.plot(angles, values, color=single_color, linewidth=2, linestyle='solid')

    ax.spines['polar'].set_visible(False)
    plt.title(title, size=16, color='darkblue', y=1.1, weight='bold', ha='center')
    plt.tight_layout()
    plt.show()

plot_radar_no_style(superheroes, "Annual Report on Superhero Abilities 2023")