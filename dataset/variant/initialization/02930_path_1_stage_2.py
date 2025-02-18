import matplotlib.pyplot as plt
import numpy as np

# Data for the transport modes and adoption rates
transport_modes = ['Hyperloop', 'Flying Cars', 'MagLev Trains', 'Teleports', 'Autonomous Buses']
adoption_rates = np.array([80, 120, 150, 60, 90])
colors = ['#4682b4', '#32cd32', '#ff69b4', '#6a5acd', '#ff8c00']

# Sort the data in descending order of adoption rates
sorted_indices = np.argsort(adoption_rates)[::-1]
transport_modes_sorted = [transport_modes[i] for i in sorted_indices]
adoption_rates_sorted = adoption_rates[sorted_indices]
colors_sorted = [colors[i] for i in sorted_indices]

# Positions of the bars on the x-axis
x_positions = np.arange(len(transport_modes_sorted))

# Plot the sorted bar chart
fig, ax = plt.subplots(figsize=(12, 7))
bars = ax.bar(x_positions, adoption_rates_sorted, color=colors_sorted, edgecolor='black', width=0.6)

# Titles and labels
ax.set_title('Futuristic City Transport Adoption Rates\nin the Year 2050', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Transport Modes', fontsize=14)
ax.set_ylabel('Adoption Rate (in thousands)', fontsize=14)

# Assign the x-ticks and labels
ax.set_xticks(x_positions)
ax.set_xticklabels(transport_modes_sorted, fontsize=12, rotation=30, ha='right')

# Annotate bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 2, f'{yval}k', ha='center', va='bottom', fontsize=12, fontweight='bold')

# Gridlines
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()