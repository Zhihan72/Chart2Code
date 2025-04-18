import matplotlib.pyplot as plt
import numpy as np

alpha_hours = [15, 18, 24, 20, 22, 17, 21, 23, 19, 26, 29, 18, 20, 24, 22, 27, 30, 20, 22, 24, 26, 20, 27, 19, 18, 24, 25, 23, 21, 20]
beta_hours = [20, 15, 17, 16, 19, 22, 21, 24, 22, 23, 18, 20, 19, 21, 23, 26, 28, 29, 30, 24, 25, 20, 22, 24, 26, 19, 28, 27, 26, 24]
gamma_hours = [30, 28, 32, 35, 29, 34, 33, 31, 29, 28, 30, 32, 25, 27, 26, 28, 32, 33, 34, 37, 35, 36, 34, 28, 27, 29, 30, 33, 34, 35]
delta_hours = [17, 19, 23, 20, 21, 18, 17, 16, 20, 24, 23, 25, 27, 28, 22, 20, 19, 18, 15, 17, 20, 19, 18, 20, 22, 23, 19, 21, 24, 25]
omega_hours = [12, 10, 15, 13, 16, 14, 20, 22, 19, 21, 18, 14, 17, 19, 20, 26, 24, 21, 23, 20, 20, 19, 17, 14, 25, 28, 27, 26, 24, 20]

# Calculate the total monthly operational hours for each terrain
total_hours = [sum(alpha_hours), sum(beta_hours), sum(gamma_hours), sum(delta_hours), sum(omega_hours)]

# Team labels
teams = ["Red Team", "Blue Group", "Yellow Crew", "Green Squad", "Orange Faction"]

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [2, 1]})

# Box Plot
colors = ['#8ecae6', '#219ebc', '#023047', '#ffb703', '#fb8500']
box = axs[0].boxplot(
    [alpha_hours, beta_hours, gamma_hours, delta_hours, omega_hours], 
    vert=False, patch_artist=True, notch=True,
    boxprops=dict(facecolor='skyblue', color='navy'),
    whiskerprops=dict(color='navy'),
    capprops=dict(color='navy'),
    flierprops=dict(marker='o', color='red', markersize=6, alpha=0.6),
    medianprops=dict(color='orange', linewidth=2)
)

for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

axs[0].set_yticks(np.arange(1, len(teams)+1))
axs[0].set_yticklabels(teams, fontsize=12, fontweight='bold')

# Bar Chart
axs[1].barh(teams, total_hours, color=colors, edgecolor='navy')
axs[1].set_xlim(0, max(total_hours) * 1.1)

plt.tight_layout()
plt.show()