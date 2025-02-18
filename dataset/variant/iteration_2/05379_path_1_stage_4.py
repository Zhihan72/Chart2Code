import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Altered names for colonies and attributes
colonies = ['Space Haven', 'Orbital Station', 'Lunar Post']
attributes = ['Creativity', 'Social', 'Mindfulness', 'Fitness', 'Meditation']

# Randomly altered data for the labels (not values)
data = [
    [7, 9, 8, 6, 8],  # Space Haven
    [6, 8, 7, 7, 9],  # Orbital Station
    [9, 7, 8, 6, 7]   # Lunar Post
]

data = np.array(data)
num_attributes = len(attributes)

angles = np.linspace(0, 2 * pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

colors = ['#ff7f0e', '#2ca02c', '#d62728']

for i, colony_data in enumerate(data):
    values = colony_data.tolist()
    values += values[:1]
    ax.fill(angles, values, color=colors[i], alpha=0.25, label=colonies[i])

# Shuffled attributes names, altered axis label appearance
plt.xticks(angles[:-1], attributes, color='darkred', size=10, fontweight='heavy')
ax.set_rlabel_position(45)
plt.yticks([2, 4, 6, 8, 10], ["Small", "Medium", "Adequate", "Good", "Excellent"], color="darkred", size=8, fontweight='heavy')
plt.ylim(0, 10)

# Altered title
plt.title("Interplanetary Relaxation Study:\nHabitat Activity Preferences", size=14, color='darkgreen', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), title="Habitats", fontsize='medium', title_fontsize='13')

plt.tight_layout()
plt.show()