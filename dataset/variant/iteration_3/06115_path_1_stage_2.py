import matplotlib.pyplot as plt
import numpy as np

# Data setup
energy_contribution = np.array([45, 25, 15, 10, 5])  # Percentage values

# Define colors for each source
colors = ['#FFD700', '#1f77b4', '#2ca02c', '#d62728', '#9467bd']

# Create the figure and axis objects
fig, ax = plt.subplots(figsize=(10, 6))

# Creating the vertical bar chart
bars = ax.bar(range(len(energy_contribution)), energy_contribution, color=colors, edgecolor='black')

# Annotating each bar with the percentage value
for bar, contribution in zip(bars, energy_contribution):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{height}%', va='bottom', ha='center', fontsize=10, color='black')

# Adding grid to the primary y-axis
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.6)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()