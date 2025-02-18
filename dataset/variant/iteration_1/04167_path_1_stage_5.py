import matplotlib.pyplot as plt
import numpy as np

# Data for each team's hours
alpha_hours = [15, 18, 24, 20, 22, 17, 21, 23, 19, 26, 29, 18, 20, 24, 22, 27, 30, 20, 22, 24, 26, 20, 27, 19, 18, 24, 25, 23, 21, 20]
beta_hours = [20, 15, 17, 16, 19, 22, 21, 24, 22, 23, 18, 20, 19, 21, 23, 26, 28, 29, 30, 24, 25, 20, 22, 24, 26, 19, 28, 27, 26, 24]
gamma_hours = [30, 28, 32, 35, 29, 34, 33, 31, 29, 28, 30, 32, 25, 27, 26, 28, 32, 33, 34, 37, 35, 36, 34, 28, 27, 29, 30, 33, 34, 35]
delta_hours = [17, 19, 23, 20, 21, 18, 17, 16, 20, 24, 23, 25, 27, 28, 22, 20, 19, 18, 15, 17, 20, 19, 18, 20, 22, 23, 19, 21, 24, 25]

# Calculate total hours for each team
total_hours = [sum(alpha_hours), sum(beta_hours), sum(gamma_hours), sum(delta_hours)]

teams = ["Red Team", "Blue Group", "Yellow Crew", "Green Squad"]

# Set up subplot with 2 rows and 1 column
fig, axs = plt.subplots(2, 1, figsize=(16, 8))

colors = ['#8ecae6', '#219ebc', '#023047', '#ffb703']

# 1st chart: Horizontal boxplot with adjusted properties
box = axs[0].boxplot(
    [alpha_hours, beta_hours, gamma_hours, delta_hours],
    vert=False, patch_artist=True, notch=True, # Set vert to False for horizontal layout
    boxprops=dict(facecolor='skyblue', color='navy'),
    whiskerprops=dict(color='navy'),
    capprops=dict(color='navy'),
    flierprops=dict(marker='o', color='red', markersize=6, alpha=0.6),
    medianprops=dict(color='orange', linewidth=2)
)

# Apply colors to box plot patches
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Set y-axis ticks and labels for the first subplot
axs[0].set_yticks(np.arange(1, len(teams)+1))
axs[0].set_yticklabels(teams, fontsize=12, fontweight='bold')

# 2nd chart: Horizontal bar chart
axs[1].barh(teams, total_hours, color=colors, edgecolor='navy')
axs[1].set_xlim(0, max(total_hours) * 1.1)

plt.tight_layout()
plt.show()