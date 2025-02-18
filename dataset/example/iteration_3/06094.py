import numpy as np
import matplotlib.pyplot as plt

# Backstory: The radar chart is for assessing the performance of different species in an intergalactic space competition across various skills.

# List of skills and species names
skills = ['Pilot Skills', 'Combat Skills', 'Negotiation', 'Engineering', 'Scientific Knowledge']
species = ['Humanoids', 'Cyborgs', 'Xenomorphs', 'Avians']

# Data representing the performance of each species in different skills
performance = np.array([
    [8, 6, 7, 5, 9],  # Humanoids
    [9, 8, 6, 9, 7],  # Cyborgs
    [6, 10, 5, 4, 6], # Xenomorphs
    [5, 7, 9, 6, 8]   # Avians
])

num_skills = len(skills)

# Function to create a radar chart
def create_radar_chart(title, labels, data, categories):
    # Calculate angles for each skill
    angles = np.linspace(0, 2 * np.pi, num_skills, endpoint=False).tolist()
    angles += angles[:1]  # Complete the circle

    # Extend data for closure
    data = np.concatenate((data, data[:, [0]]), axis=1)

    # Initialize the plot
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Plot each species' data
    colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']
    for idx, (d, color) in enumerate(zip(data, colors)):
        ax.fill(angles, d, color=color, alpha=0.25)
        ax.plot(angles, d, color=color, linewidth=2, label=categories[idx])

    # Customize the radar chart
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=10)

    # Add title and legend
    plt.title(title, size=16, fontweight='bold', pad=20, va='bottom')
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), title="Species")

    # Automatically adjust layout
    plt.tight_layout()

    # Display the plot
    plt.show()

# Call the function with the data
create_radar_chart(
    "Intergalactic Space Competition\nSpecies Performance Assessment",
    skills, performance, species
)