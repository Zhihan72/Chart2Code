import matplotlib.pyplot as plt
import numpy as np

# Data for the transport modes and their adoption rates (in thousands)
transport_modes = ['Hyperloop', 'Flying Cars', 'MagLev Trains', 'Teleports', 'Autonomous Buses']
adoption_rates = np.array([80, 120, 150, 60, 90])

# Colors for each transport mode
colors = ['#ff8c00', '#32cd32', '#4682b4', '#6a5acd', '#ff69b4']

# Plot the horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 7))

bars = ax.barh(np.arange(len(transport_modes)), adoption_rates, color=colors, edgecolor='grey', linewidth=2, height=0.55, linestyle='-.')

# Titles and labels
ax.set_title('Futuristic Transport Adoption Rates\nYear 2050', fontsize=18, fontweight='heavy', pad=25)
ax.set_xlabel('Adoption Rate (in thousands)', fontsize=12, fontstyle='italic', color='darkblue')
ax.set_ylabel('Transport Modes', fontsize=12, fontstyle='italic', color='darkred')

# Assign the y-ticks and labels
ax.set_yticks(np.arange(len(transport_modes)))
ax.set_yticklabels(transport_modes, fontsize=10)

# Annotating the bars with their respective values
for bar in bars:
    xval = bar.get_width()
    ax.text(xval + 3, bar.get_y() + bar.get_height()/2, f'{xval}k', ha='left', va='center', fontsize=10, fontweight='medium')

# Altering legend style
legend_labels = ['Fast', 'Instant', 'Eco', 'Rapid', 'Luxurious']
ax.legend(bars, legend_labels, title='Features', title_fontsize='10', loc='best', fontsize=8, frameon=True, shadow=True, fancybox=True)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()