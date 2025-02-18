import matplotlib.pyplot as plt
import numpy as np

# Define habitats and insect types
habitats = ['Forests', 'Grasslands', 'Wetlands', 'Deserts', 'Urban Areas']

# Number of insects (in thousands) in each habitat
population_data = np.array([
    [150, 50, 40, 10, 20],  # Forests
    [70, 60, 25, 5, 10],    # Grasslands
    [90, 70, 80, 15, 30],   # Wetlands
    [15, 7, 3, 35, 5],      # Deserts
    [50, 30, 60, 30, 20]    # Urban Areas
])

# Calculate total populations for each habitat
total_populations = np.sum(population_data, axis=1)

# Create plot
fig, ax = plt.subplots(figsize=(10, 6))

# Colors for bar chart
colors = ['#8c564b', '#e377c2', '#2ca02c', '#1f77b4', '#ff7f0e']

# Create vertical bar chart
bars = ax.bar(habitats, total_populations, color=colors, edgecolor='black')

# Add data labels to each bar
for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2,
            f'{int(bar.get_height())}k', ha='center', fontsize=10, fontweight='bold', color='black')

# Customize y-axis
ax.set_ylabel("Insect Population (Thousands)", fontsize=12)
ax.yaxis.grid(True, linestyle='--', alpha=0.6)
ax.set_ylim(0, 350)

# Set titles and labels
ax.set_title("Insect Population Across Habitats", fontsize=16, fontweight='bold', pad=20)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()