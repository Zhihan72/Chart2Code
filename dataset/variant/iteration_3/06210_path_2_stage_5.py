import numpy as np
import matplotlib.pyplot as plt
from math import pi

domains = [
    'AI', 'Quantum Worlds', 'Nano-Tech',
    'Cosmic Flights', 'Solar Power', 'Digital Security'
]

civilization_1 = [9, 8, 7, 7, 8, 9]  # Galactic Confederacy
civilization_3 = [8, 7, 9, 6, 7, 8]  # Star Coalition

data = np.vstack([civilization_1, civilization_3])
civilizations = ['Galactic Confederacy', 'Star Coalition']
num_domains = len(domains)
angles = np.linspace(0, 2 * np.pi, num_domains, endpoint=False).tolist()

def create_radar_chart(ax, data, categories, labels):
    angles_with_closure = angles + angles[:1]
    marker_types = ['o', '^']
    line_styles = ['-', '--']
    new_colors = ['cornflowerblue', 'mediumseagreen']
    for i, group in enumerate(data):
        values = np.append(group, group[0])
        ax.plot(angles_with_closure, values, linestyle=line_styles[i], marker=marker_types[i], 
                label=labels[i], color=new_colors[i])
        ax.fill(angles_with_closure, values, color=new_colors[i], alpha=0.2)
    plt.xticks(angles, categories, size=10, color='black')
    ax.set_rlabel_position(45)
    plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=8)
    plt.ylim(0, 10)

def main():
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    create_radar_chart(ax, data, domains, civilizations)
    plt.title("Technological Readiness Across Galaxies", 
              size=14, color='navy', y=1.1, fontweight='bold')
    plt.legend(loc='lower right', bbox_to_anchor=(1.1, -0.1))
    ax.grid(color='grey', linestyle=':', linewidth=1.5)
    plt.tight_layout()
    plt.show()

main()