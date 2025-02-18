import matplotlib.pyplot as plt
import numpy as np

# Data for the transport modes and their adoption rates (in thousands)
transport_modes = ['Hyperloop', 'Flying Cars', 'MagLev Trains', 'Teleports', 'Autonomous Buses']
adoption_rates = np.array([80, 120, 150, 60, 90])

# Colors for each transport mode
colors = ['#ff8c00', '#32cd32', '#4682b4', '#6a5acd', '#ff69b4']

# Positions of the bars on the x-axis
x_positions = np.arange(len(transport_modes))

# Plot the bar chart
fig, ax = plt.subplots(figsize=(12, 7))

bars = ax.bar(x_positions, adoption_rates, color=colors, edgecolor='grey', linewidth=2, width=0.55, linestyle='-.')

# Titles and labels
ax.set_title('Futuristic Transport Adoption Rates\nYear 2050', fontsize=18, fontweight='heavy', pad=25)
ax.set_xlabel('Transport Modes', fontsize=12, fontstyle='italic', color='darkred')
ax.set_ylabel('Adoption Rate (in thousands)', fontsize=12, fontstyle='italic', color='darkblue')

# Assign the x-ticks and labels
ax.set_xticks(x_positions)
ax.set_xticklabels(transport_modes, fontsize=10, rotation=45, ha='right')

# Annotating the bars with their respective values
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 3, f'{yval}k', ha='center', va='bottom', fontsize=10, fontweight='medium')

# Removing gridlines for a cleaner look
# Grid is removed to alter style

# Altering legend style
legend_labels = ['Fast', 'Instant', 'Eco', 'Rapid', 'Luxurious']
ax.legend(bars, legend_labels, title='Features', title_fontsize='10', loc='best', fontsize=8, frameon=True, shadow=True, fancybox=True)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()