import matplotlib.pyplot as plt
import numpy as np

# Define habitats and insect types
habitats = ['Forests', 'Grasslands', 'Wetlands', 'Deserts', 'Urban Areas']

# Number of insects (in thousands) in each habitat
population_data = np.array([
    [150, 50, 40, 10, 20],
    [70, 60, 25, 5, 10],
    [90, 70, 80, 15, 30],
    [15, 7, 3, 35, 5],
    [50, 30, 60, 30, 20]
])

# Calculate total populations for each habitat
total_populations = np.sum(population_data, axis=1)

# Sort habitats and populations in descending order
sorted_indices = np.argsort(-total_populations)
sorted_habitats = np.array(habitats)[sorted_indices]
sorted_total_populations = total_populations[sorted_indices]

# Calculate the average number of Dragonflies across habitats
average_dragonflies = np.mean(population_data[:, -1])

# Create plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# New colors for bar chart
new_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create horizontal bar chart
bars = ax1.barh(sorted_habitats, sorted_total_populations, color=new_colors, edgecolor='black', height=0.6)

# Add data labels to each bar
for bar in bars:
    ax1.text(bar.get_width() + 5, bar.get_y() + bar.get_height() / 2,
             f'{int(bar.get_width())}k', va='center', fontsize=10, fontweight='bold', color='black')

# Customize x-axis
ax1.set_xlabel("Insect Population (Thousands)", fontsize=12)
ax1.xaxis.grid(True, linestyle='--', alpha=0.6)
ax1.set_xlim(0, 350)

# Create a secondary y-axis for the overlay line plot
ax2 = ax1.twiny()

# Add a line plot for the average Dragonflies
ax2.axvline(average_dragonflies, color='darkred', linestyle='-', linewidth=2, label='Avg Dragonflies: {:.1f}'.format(average_dragonflies))
ax2.set_xlim(0, 100)

# Add a legend
fig.legend(loc='upper right', bbox_to_anchor=(0.85, 0.9))

# Set titles and labels
ax1.set_title("The Buzz of the Ecosystem:\nInsect Population and Average Dragonflies Across Habitats",
              fontsize=16, fontweight='bold', pad=20)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()