import matplotlib.pyplot as plt
import numpy as np

skills = ['Piloting', 'Engineering', 'Science', 'Physical Fitness', 'Teamwork', 'Quick Decision Making']
num_skills = len(skills)

neptune_academy = [8, 7, 9, 6, 8, 7]
mars_academy = [7, 8, 6, 7, 9, 8]

neptune_academy += neptune_academy[:1]
mars_academy += mars_academy[:1]

angles = np.linspace(0, 2 * np.pi, num_skills, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Changed marker from fill to plot with new line style and marker
ax.plot(angles, neptune_academy, 'o-.', color='#1f77b4', alpha=0.8, label='Neptune Academy')
ax.plot(angles, mars_academy, 's--', color='#ff7f0e', alpha=0.8, label='Mars Academy')

ax.set_yticks([2, 4, 6, 8])
ax.set_ylim(0, 10)
ax.yaxis.grid(True)  # Enabled grid lines for y-axis

# Changed the location and appearance of the legend
ax.legend(loc='upper left', frameon=False)

# Changed the appearance of the border
ax.spines['polar'].set_visible(False)

plt.show()