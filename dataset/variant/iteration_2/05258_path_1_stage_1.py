import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Categories
categories = ['Storytelling', 'Musicianship', 'Herbal Knowledge', 'Combat Skills', 'Mysticism', 'Charm', 'Alchemy']

# Altered skills for three legendary bards
bard_1 = np.array([6, 9, 4, 8, 5, 7, 9])  # Altered values within original structure
bard_2 = np.array([9, 7, 6, 8, 5, 8, 7])  # Altered values
bard_3 = np.array([5, 9, 6, 6, 7, 7, 8])  # Altered values

# Combine data for easier handling
bards_data = [bard_1, bard_2, bard_3]
bards_names = ['Lyrical Linden', 'Melodic Melody', 'Harmonious Harper']

# Compute angles for each axis
num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Color palette
colors = ['#FF6347', '#4682B4', '#32CD32']

# Function to create radar chart
def create_radar_chart(ax, data, categories, bards_names, color):
    for bard_data, bard_name, color in zip(data, bards_names, color):
        values = np.concatenate((bard_data, [bard_data[0]]))
        ax.plot(angles, values, linewidth=2, linestyle='solid', label=bard_name, color=color)
        ax.fill(angles, values, color=color, alpha=0.2)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, color='black', size=10)

    ax.set_rlabel_position(0)
    plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color='grey', size=7)
    ax.set_ylim(0, 10)

# Create figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), subplot_kw=dict(polar=True))

# Radar chart
create_radar_chart(ax1, bards_data, categories, bards_names, colors)
ax1.set_title('Legendary Bards: Skills and Talents', size=14, color='darkblue', y=1.1, fontweight='bold')
ax1.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Bar chart
ax2.remove()
ax2 = fig.add_subplot(1, 2, 2)
x = np.arange(num_vars)
width = 0.25

ax2.bar(x - width, bard_1, width, color=colors[0], label=bards_names[0])
ax2.bar(x, bard_2, width, color=colors[1], label=bards_names[1])
ax2.bar(x + width, bard_3, width, color=colors[2], label=bards_names[2])

ax2.set_ylabel('Skill Level')
ax2.set_title('Comparison of Bard Skills', fontsize=13, fontweight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(categories, rotation=45, ha="right", fontsize=10)
ax2.legend(loc='upper left')
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()
plt.show()