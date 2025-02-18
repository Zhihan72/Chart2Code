import matplotlib.pyplot as plt
import numpy as np

# Sectors and energy sources
sectors = ['Residential', 'Commercial', 'Industrial', 'Public Services']
energy_sources = ['Renewable', 'Fossil Fuels', 'Nuclear']

# Projected energy consumption data (in terawatt-hours, TWh)
energy_consumption = np.array([
    [120, 180, 30],  # Residential
    [110, 210, 60],  # Commercial
    [90, 240, 80],   # Industrial
    [70, 110, 40]    # Public Services
])

# Calculate total energy consumption for each sector
total_energy = energy_consumption.sum(axis=1)

# Sort sectors and energy consumption based on total energy
sorted_indices = np.argsort(total_energy)
sectors_sorted = [sectors[i] for i in sorted_indices]
energy_consumption_sorted = energy_consumption[sorted_indices]

# Create figure and axes for the bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Colors for each energy source
source_colors = ['#4CAF50', '#FF6347', '#FFD700']

# Plot each energy source on top of the previous one
bottom = np.zeros(len(sectors))
for i, source in enumerate(energy_sources):
    ax.bar(sectors_sorted, energy_consumption_sorted[:, i], label=source, color=source_colors[i], alpha=0.85, bottom=bottom)
    bottom += energy_consumption_sorted[:, i]

# Add labels and title
ax.set_ylabel('Energy Consumption (TWh)', fontsize=12, fontweight='bold')
ax.set_xlabel('Sectors', fontsize=12, fontweight='bold')
ax.set_title('Sorted Smart City Initiatives: Energy Consumption by Sector and Source (2025 Projections)', 
             fontsize=14, fontweight='bold', pad=15)

# Adding legend
ax.legend(title='Energy Sources', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Customize tick labels
ax.set_xticks(np.arange(len(sectors)))
ax.set_xticklabels(sectors_sorted, rotation=45, ha='right', fontsize=10)

# Adding a grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Annotate each bar segment with its value
for bar in ax.patches:
    height = bar.get_height()
    if height > 0:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_y() + height / 2,
            f'{int(height)}',
            ha='center', va='center',
            fontsize=10, color='black'
        )

# Automatically adjust layout for better presentation
plt.tight_layout()

# Display the chart
plt.show()