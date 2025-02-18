import numpy as np
import matplotlib.pyplot as plt
from math import pi

domains = [
    'Quantum Computing', 'Artificial Intelligence', 'Nanotechnology',
    'Space Travel', 'Energy Generation', 'Cybersecurity'
]

civilization_1 = [9, 8, 7, 7, 8, 9]  # Celestial Federation
civilization_3 = [8, 7, 9, 6, 7, 8]  # Nebula Alliance

data = np.vstack([civilization_1, civilization_3])
civilizations = ['Celestial Federation', 'Nebula Alliance']
num_domains = len(domains)
angles = np.linspace(0, 2 * np.pi, num_domains, endpoint=False).tolist()

def create_radar_chart(ax, data, categories, labels):
    angles_with_closure = angles + angles[:1]
    for i, group in enumerate(data):
        values = np.append(group, group[0])
        ax.fill(angles_with_closure, values, alpha=0.4, label=labels[i]) # Ensure areas are filled
    plt.xticks(angles, categories, size=10)
    ax.set_rlabel_position(30)
    plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)
    plt.ylim(0, 10)

def main():
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    create_radar_chart(ax, data, domains, civilizations)
    plt.title("Interplanetary Alliance Technological Preparedness", 
              size=16, color='darkblue', y=1.1, fontweight='bold')
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.tight_layout()
    plt.show()

main()