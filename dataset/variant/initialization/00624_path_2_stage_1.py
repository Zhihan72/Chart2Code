import matplotlib.pyplot as plt

# Efficiency scores for renewable energy sources across different regions
energy_sources = ['Renewable Energy']
efficiency_data = [
    75, 85, 80, 88, 90, 95, 93, 77, 82, 78,  # Solar
    60, 72, 68, 66, 74, 75, 73, 71, 70, 69,  # Wind
    85, 87, 90, 92, 88, 85, 89, 91, 86, 84,  # Hydroelectric
    55, 60, 58, 62, 59, 57, 61, 63, 64, 56,  # Biomass
    70, 72, 73, 78, 80, 75, 77, 76, 74, 71,  # Geothermal
]

# Create the plot
fig, ax = plt.subplots(figsize=(8, 12))

# Vertical box plot for single group of combined data
bp = ax.boxplot(efficiency_data, vert=True, patch_artist=True, notch=True, showmeans=True,
                meanline=True, meanprops=dict(linestyle='-', linewidth=2.5, color='blue'))

# Customizing colors for the box
bp['boxes'][0].set(facecolor='#FFC300', alpha=0.6)

# Enhance medians, whiskers, and caps
for whisker, cap, median in zip(bp['whiskers'], bp['caps'], bp['medians']):
    whisker.set(color='#2C3E50', linewidth=2, linestyle="--")
    cap.set(color='#2C3E50', linewidth=2)
    median.set(color='green', linewidth=3)

# Adding title and labels
ax.set_title('Global Renewable Energy Efficiency Evaluation', fontsize=16, fontweight='bold')
ax.set_ylabel('Efficiency Score (%)', fontsize=13)
ax.set_xticklabels(energy_sources, fontsize=12)

# Grid and limits
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_ylim(50, 100)

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Show the plot
plt.show()