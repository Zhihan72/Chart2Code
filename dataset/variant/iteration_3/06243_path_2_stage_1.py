import matplotlib.pyplot as plt
import numpy as np

# Define the core skills for space explorers
skills = ['Piloting', 'Engineering', 'Science', 'Physical Fitness', 'Teamwork', 'Quick Decision Making']

# Number of skills
num_skills = len(skills)

# Define skill levels for each academy
neptune_academy = [8, 7, 9, 6, 8, 7]
mars_academy = [7, 8, 6, 7, 9, 8]

# Close the data loop for radar chart
neptune_academy += neptune_academy[:1]
mars_academy += mars_academy[:1]

# Angles for each skill, including a repeat at the end to close the loop
angles = np.linspace(0, 2 * np.pi, num_skills, endpoint=False).tolist()
angles += angles[:1]

# Initialize the plot
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot data for each academy
ax.plot(angles, neptune_academy, linewidth=2, linestyle='-', label='Neptune Academy', color='#1f77b4', marker='o')
ax.fill(angles, neptune_academy, '#1f77b4', alpha=0.15)

ax.plot(angles, mars_academy, linewidth=2, linestyle='-', label='Mars Academy', color='#ff7f0e', marker='s')
ax.fill(angles, mars_academy, '#ff7f0e', alpha=0.15)

# Title and axis configuration
plt.title("Training Outcomes in Interstellar Space Academies", size=18, color='navy', pad=20)
plt.xticks(angles[:-1], skills, color='darkslategray', size=13, weight='bold')
ax.set_yticks([2, 4, 6, 8])
ax.set_ylim(0, 10)
ax.set_yticklabels(["2", "4", "6", "8"], color='gray', size=10)

# Adding a legend
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=12)

# Enhance grid and improve visibility
ax.spines['polar'].set_visible(False)
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, color='grey')

# Ensuring everything fits nicely
plt.tight_layout()

# Display the plot
plt.show()