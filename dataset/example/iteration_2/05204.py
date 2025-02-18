import matplotlib.pyplot as plt
import numpy as np

# Define aspects of superhero capabilities in a league
superheroes = ["Iron Avenger", "Dark Knight", "Scarlet Witch", "Green Guardian", "Fastest Man"]
categories = ["Strength", "Tech Savvy", "Magic", "Durability", "Speed"]

# Scores for each superhero, on a scale of 1 to 10
capabilities = np.array([
    [8, 9, 2, 8, 7],  # Iron Avenger
    [7, 9, 1, 7, 6],  # Dark Knight
    [5, 4, 10, 6, 4], # Scarlet Witch
    [6, 4, 4, 10, 5], # Green Guardian
    [3, 2, 3, 3, 10]  # Fastest Man
])

num_vars = len(categories)

# Compute angles for each category
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Initialize radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Define color palette
colors = ["#FF0000", "#000000", "#800080", "#008000", "#FFD700"]

# Function to plot each superhero's data
for idx, (data, color) in enumerate(zip(capabilities, colors)):
    data = np.concatenate((data, [data[0]]))
    ax.plot(angles, data, linewidth=2, linestyle='solid', marker='o', color=color, label=superheroes[idx])
    ax.fill(angles, data, color=color, alpha=0.3)
    for angle, val in zip(angles, data):
        ax.text(angle, val + 0.5, f'{val:.1f}', horizontalalignment='center', verticalalignment='center', fontsize=8, color=color)

# Add category labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, fontweight='bold')

# Customize radial and circular grid
ax.set_yticks(range(1, 11))
ax.set_yticklabels([])
ax.yaxis.grid(True, color='gray', linestyle='--', linewidth=0.7)
ax.xaxis.grid(True, color='gray', linestyle='--', linewidth=0.7)

# Title and legend
ax.set_title("League of Heroes: Capabilities Comparison", fontsize=16, fontweight='bold', va='bottom')
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), title="Superheroes", fontsize=10)

# Background color
ax.set_facecolor('#f0f0f0')

# Adjust layout and show
plt.tight_layout()
plt.show()