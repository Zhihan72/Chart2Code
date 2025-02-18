import matplotlib.pyplot as plt
import numpy as np

# Define the stats for Dragon and Unicorn
dragon_stats = [8, 6, 9, 7, 5]
unicorn_stats = [5, 9, 7, 8, 9]

# Create angles in radians for each axis of the radar chart
angles = np.linspace(0, 2 * np.pi, len(dragon_stats), endpoint=False).tolist()
angles += angles[:1]  # Close the loop

def plot_creature(ax, stats, color):
    stats += stats[:1]  # Close the loop for each creature
    ax.fill(angles, stats, color=color, alpha=0.25)  # Fill the areas with color

# Create the polar subplot for the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot Dragon and Unicorn stats
plot_creature(ax, dragon_stats, 'firebrick')
plot_creature(ax, unicorn_stats, 'forestgreen')

# Remove x-axis labels and adjust radial labels
plt.xticks([])
ax.set_rlabel_position(30)
plt.yticks([])
plt.ylim(0, 10)

plt.tight_layout()
plt.show()