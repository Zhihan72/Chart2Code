import matplotlib.pyplot as plt
import numpy as np

# Define the categories and data for different adventurers' abilities
categories = ['Strength', 'Agility', 'Intelligence', 'Charisma', 'Resilience']
num_vars = len(categories)

# Data for each adventurer
arthur = [8, 6, 7, 9, 8]
morgana = [7, 8, 9, 6, 7]

# Average data across remaining adventurers
average_abilities = [
    np.mean([arthur[i], morgana[i]]) 
    for i in range(num_vars)
]

# Initialize the figure
fig, ax = plt.subplots(figsize=(8, 8))

# Create bar chart
ax.bar(categories, average_abilities, color=['b', 'g', 'purple', 'orange', 'c'])
ax.set_ylim(0, 10)
ax.set_title('Average Abilities Across Categories', fontsize=14, fontweight='bold')
ax.set_ylabel('Average Rating')
ax.set_xlabel('Ability')
for i, score in enumerate(average_abilities):
    ax.text(i, score + 0.2, f'{score:.1f}', ha='center', color='black', fontweight='bold')

# Automatically adjust the layout for optimal spacing
plt.tight_layout()

# Display the chart
plt.show()