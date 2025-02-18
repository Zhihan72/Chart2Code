import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define domains for the axis labels
domains = [
    'Quantum Computing', 'Artificial Intelligence', 'Nanotechnology',
    'Space Travel', 'Energy Generation', 'Cybersecurity'
]

# Data for each civilization
civilization_1 = [8, 9, 7, 9, 7, 8]
civilization_2 = [9, 7, 6, 9, 8, 6]
civilization_3 = [7, 8, 9, 6, 8, 7]

# Stack data vertically for ease of manipulation
data = np.vstack([civilization_1, civilization_2, civilization_3])

# Labels for each civilization
civilizations = ['Celestial Federation', 'Galactic Union', 'Nebula Alliance']

# Calculate number of domains and generate angles for radar plot
num_domains = len(domains)
angles = np.linspace(0, 2 * np.pi, num_domains, endpoint=False).tolist()

def create_radar_chart(ax, data, categories, labels, colors):
    # Close the radar chart by appending the first angle at the end for closure
    angles_with_closure = angles + angles[:1]
    for i, group in enumerate(data):
        # Append the first value to close the chart shape
        values = np.append(group, group[0])
        # Plot the radar chart and fill it
        ax.plot(angles_with_closure, values, linewidth=2, linestyle='solid', label=labels[i], color=colors[i])
        ax.fill(angles_with_closure, values, alpha=0.25, color=colors[i])
    
    # Set the labels and limits for the radar chart
    plt.xticks(angles, categories, size=10)
    ax.set_rlabel_position(30)
    plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)
    plt.ylim(0, 10)

def main():
    # Create a polar subplot
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Line colors
    
    # Generate the radar chart with filled areas
    create_radar_chart(ax, data, domains, civilizations, colors)
    
    # Set the title and legend for the plot
    plt.title("Interplanetary Alliance Technological Preparedness", 
              size=16, color='darkblue', y=1.1, fontweight='bold')
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

    plt.tight_layout()
    plt.show()

main()