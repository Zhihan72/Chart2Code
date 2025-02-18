import matplotlib.pyplot as plt
import numpy as np

# Define the traits categories
categories = ['Strength', 'Intelligence', 'Speed', 'Durability', 'Power', 'Combat Skills']
num_vars = len(categories)

# Define the data for each superhero explicitly, removing Aquaman
superheroes = {
    'Superman': [9, 7, 9, 8, 10, 7],
    'Batman': [4, 9, 6, 5, 6, 9],
    'Wonder Woman': [8, 8, 7, 7, 8, 9],
    'Flash': [6, 6, 10, 5, 7, 6],
}

# Create angles for each category in the plot
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

def plot_radar(data, title):
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    plt.xticks(angles[:-1], categories, fontsize=12)
    ax.set_rscale('linear')
    ax.set_rlabel_position(0)
    plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)
    plt.ylim(0, 10)

    # Define color palette
    colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']
    
    # Plot each superhero's data
    for color, (hero, values) in zip(colors, data.items()):
        values += values[:1]  # Complete the loop
        ax.fill(angles, values, color=color, alpha=0.25, label=hero)
        ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')

    plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=12)
    plt.title(title, size=16, color='darkblue', y=1.1, weight='bold', ha='center')
    plt.tight_layout()
    plt.show()

# Call the plot function with our updated data and title
plot_radar(superheroes, "Comparison of Core Superhero Traits\nAnnual Review 2023")