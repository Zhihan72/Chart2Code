import matplotlib.pyplot as plt
import numpy as np

num_vars = 6

superheroes = {
    'Superman': [8, 6, 10, 7, 9, 8],
    'Batman': [5, 8, 5, 6, 7, 8],
    'Wonder Woman': [9, 7, 8, 6, 9, 7],
    'Flash': [7, 5, 9, 4, 6, 7],
    'Aquaman': [7, 6, 7, 7, 6, 7],
}

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def plot_radar(data):
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    ax.set_theta_offset(np.pi / 3)
    ax.set_theta_direction(1)

    ax.set_rscale('log')
    ax.set_yticklabels([])  # Remove y-tick labels
    plt.ylim(1, 10)

    colors_and_styles = [
        ('#FF6347', '-.', 'o'),
        ('#4682B4', '--', 'v'),
        ('#32CD32', ':', '^'),
        ('#FFD700', '-', '<'),
        ('#6A5ACD', '-.', '>')
    ]

    for (color, linestyle, marker), (hero, values) in zip(colors_and_styles, data.items()):
        values += values[:1]
        ax.fill(angles, values, color=color, alpha=0.15)
        ax.plot(angles, values, color=color, linewidth=2, linestyle=linestyle, marker=marker, label=hero)

    plt.legend(loc='lower left', bbox_to_anchor=(-0.1, 0), fontsize=11, frameon=False, borderaxespad=2.0)
    plt.tight_layout()
    plt.show()

plot_radar(superheroes)