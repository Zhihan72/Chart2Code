import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Backstory:
# In a distant galaxy, various cosmic civilizations have been advancing in different technological domains to prepare for an upcoming interplanetary alliance. 
# Our radar chart showcases the technological capabilities of these civilizations across key areas that are crucial for the alliance.

# Define the technological domains
domains = [
    'Quantum Computing', 'Artificial Intelligence', 'Nanotechnology',
    'Space Travel', 'Energy Generation', 'Cybersecurity'
]

# Data representing the capabilities of different civilizations (on a scale of 1 to 10)
civilization_1 = [9, 8, 7, 7, 8, 9]  # Celestial Federation
civilization_2 = [6, 9, 8, 7, 9, 6]  # Galactic Union
civilization_3 = [8, 7, 9, 6, 7, 8]  # Nebula Alliance

# Combine data
data = np.vstack([civilization_1, civilization_2, civilization_3])

# Civilization names for the legend
civilizations = ['Celestial Federation', 'Galactic Union', 'Nebula Alliance']

# Number of domains
num_domains = len(domains)

# Calculate angle for each domain
angles = np.linspace(0, 2 * np.pi, num_domains, endpoint=False).tolist()

# Function to create a radar chart
def create_radar_chart(ax, data, categories, labels):
    angles_with_closure = angles + angles[:1]
    for i, group in enumerate(data):
        values = np.append(group, group[0])
        ax.plot(angles_with_closure, values, linewidth=2, linestyle='solid', label=labels[i])
        ax.fill(angles_with_closure, values, alpha=0.25)
    plt.xticks(angles, categories, size=10)
    ax.set_rlabel_position(30)
    plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)
    plt.ylim(0, 10)

# Main function to set up plots
def main():
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

    create_radar_chart(ax, data, domains, civilizations)
    
    plt.title("Interplanetary Alliance Technological Preparedness", 
              size=16, color='darkblue', y=1.1, fontweight='bold')
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

    plt.tight_layout()
    plt.show()

main()