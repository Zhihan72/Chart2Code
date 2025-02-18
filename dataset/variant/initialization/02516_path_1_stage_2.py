import matplotlib.pyplot as plt
import numpy as np

# Define proficiency data for each industry
proficiency_healthcare = [7, 6, 8, 5, 9, 7]
proficiency_finance = [8, 7, 7, 8, 6, 9]
proficiency_technology = [9, 8, 6, 9, 7, 8]

# Additional projected data for 2030
proficiency_projection_2030 = {
    'Healthcare': [8, 7, 9, 6, 9, 8],
    'Finance': [9, 8, 8, 9, 7, 9],
    'Technology': [9, 9, 7, 9, 8, 9]
}

num_vars = len(proficiency_healthcare)

# Compute angles for radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
proficiency_healthcare += proficiency_healthcare[:1]
proficiency_finance += proficiency_finance[:1]
proficiency_technology += proficiency_technology[:1]
angles += angles[:1]

# Initialize the figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8), subplot_kw={})
fig.subplots_adjust(wspace=0.5)

# Radar chart
ax = axs[0]
# ax.set_polar(True)
ax.plot(angles, proficiency_healthcare, linewidth=2, linestyle='solid', color='#1f77b4')
ax.fill(angles, proficiency_healthcare, alpha=0.25, color='#1f77b4')
ax.plot(angles, proficiency_finance, linewidth=2, linestyle='solid', color='#ff7f0e')
ax.fill(angles, proficiency_finance, alpha=0.25, color='#ff7f0e')
ax.plot(angles, proficiency_technology, linewidth=2, linestyle='solid', color='#2ca02c')
ax.fill(angles, proficiency_technology, alpha=0.25, color='#2ca02c')
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels([])

# Horizontal bar chart for projected 2030 data
ax2 = axs[1]
height = 0.2  
y = np.arange(num_vars)

# Bar positions and heights
ax2.barh(y - height, proficiency_projection_2030['Healthcare'], height, color='#1f77b4')
ax2.barh(y, proficiency_projection_2030['Finance'], height, color='#ff7f0e')
ax2.barh(y + height, proficiency_projection_2030['Technology'], height, color='#2ca02c')

ax2.set_yticks(y)
ax2.set_yticklabels([])
ax2.set_xticklabels([])

plt.tight_layout()
plt.show()