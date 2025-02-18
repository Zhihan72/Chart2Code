import numpy as np
import matplotlib.pyplot as plt
from math import pi

domains = ['Quantum', 'AI', 'Nano', 'Space', 'Energy', 'Cyber']

civilization_1 = [8, 9, 7, 9, 7, 8]
civilization_2 = [9, 7, 6, 9, 8, 6]
civilization_3 = [7, 8, 9, 6, 8, 7]

data = np.vstack([civilization_1, civilization_2, civilization_3])

civilizations = ['Celestial Fed.', 'Galactic Un.', 'Nebula All.']

num_domains = len(domains)
angles = np.linspace(0, 2 * np.pi, num_domains, endpoint=False).tolist()

def create_radar_chart(ax, data, categories, labels, colors):
    angles_with_closure = angles + angles[:1]
    for i, group in enumerate(data):
        values = np.append(group, group[0])
        # Altering line style and marker
        ax.plot(angles_with_closure, values, linewidth=2, linestyle='dotted', marker='o', label=labels[i], color=colors[i])
        ax.fill(angles_with_closure, values, alpha=0.25, color=colors[i])

    plt.xticks(angles, categories, size=10)
    ax.set_rlabel_position(30)
    # Removed y-ticks for stylistic change
    plt.ylim(0, 10)

def main():
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    
    # Altered colors
    colors = ['#e377c2', '#8c564b', '#9467bd']
    
    create_radar_chart(ax, data, domains, civilizations, colors)
    
    # Changed title color and position
    plt.title("Tech. Preparedness", size=16, color='purple', y=1.15, fontweight='bold')
    # Altered legend position
    plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1.2))
    
    # Added grid with dashed lines
    ax.grid(color='grey', linestyle='--', linewidth=0.5)

    plt.tight_layout()
    plt.show()

main()