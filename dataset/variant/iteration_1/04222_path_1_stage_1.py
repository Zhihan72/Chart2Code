import matplotlib.pyplot as plt
import numpy as np

# Define the fantasy creatures and attributes
creatures = ['Dragon', 'Elf', 'Orc', 'Wizard']
attributes = ['Strength', 'Intelligence', 'Agility', 'Magic Power', 'Stealth']

# Data for each creature as competency levels (scale of 1-10)
data = {
    'Dragon': [9, 7, 6, 10, 5],
    'Elf': [5, 8, 9, 6, 8],
    'Orc': [10, 5, 7, 3, 6],
    'Wizard': [4, 10, 5, 9, 7]
}

num_vars = len(attributes)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Function to create radar charts
def radar_chart(ax, values, creature_name, color):
    values += values[:1]
    ax.fill(angles, values, color=color, alpha=0.5)  # Increased alpha for better fill visibility

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(attributes, color='grey', fontsize=12)
    ax.set_yticklabels([])

    ax.set_title(creature_name, size=15, color=color, pad=20)

colors = ['#FF4500', '#32CD32', '#8B0000', '#1E90FF']

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 10), subplot_kw=dict(polar=True))
fig.subplots_adjust(hspace=0.4, wspace=0.4)

for ax, (creature, color) in zip(axs.flat, zip(creatures, colors)):
    radar_chart(ax, data[creature], creature, color)

plt.suptitle("Fantasy Creatures' Competency Assessment Across Various Attributes", 
             fontsize=18, fontweight='bold', color='darkslateblue')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()