import matplotlib.pyplot as plt
import numpy as np

# Backstory: An interstellar space agency is tracking the growth in exploration missions to different planets over several decades.

# Time periods in decades
decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']

# Names of the planets
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Number of exploration missions to each planet per decade
missions = np.array([
    [2, 5, 10, 7, 3, 1, 0, 0],  # 1960s
    [3, 6, 12, 9, 4, 2, 0, 0],  # 1970s
    [4, 8, 15, 12, 6, 3, 1, 0], # 1980s
    [6, 12, 18, 15, 8, 4, 2, 1],# 1990s
    [10, 15, 20, 18, 12, 7, 4, 2],# 2000s
    [15, 20, 25, 22, 15, 10, 6, 4],# 2010s
    [20, 25, 30, 28, 18, 12, 8, 5] # 2020s
])

# Plotting the bar chart
fig, ax = plt.subplots(figsize=(16, 9))

# Creating an array of colors for the respective planets
colors = ['#d32f2f', '#f57c00', '#fbc02d', '#388e3c', '#1976d2', '#7b1fa2', '#5d4037', '#607d8b']

# Setting the bar width
bar_width = 0.10

# Creating positions for the bars
indices = np.arange(len(decades))

# Plotting each planet's data
for i, planet in enumerate(planets):
    ax.bar(indices + i * bar_width, missions[:, i], bar_width, label=planet, color=colors[i])

# Adding titles and labels
ax.set_title('Interstellar Exploration Missions per Planet over Decades', fontsize=20, fontweight='bold')
ax.set_xlabel('Decades', fontsize=15)
ax.set_ylabel('Number of Missions', fontsize=15)
ax.set_xticks(indices + 3.5 * bar_width)
ax.set_xticklabels(decades)

# Adding legends
ax.legend(title='Planets', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adding annotations on each bar
for i in range(len(decades)):
    for j in range(len(planets)):
        ax.text(i + j * bar_width, missions[i, j] + 0.5, f'{missions[i, j]}', ha='center', va='bottom', fontsize=10, color='black')

# Improving layout to prevent overlap
plt.tight_layout()
plt.show()