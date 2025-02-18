import matplotlib.pyplot as plt
import numpy as np

# Backstory: Monitoring the impact of different environmental conservation strategies on badger populations in British woodlands over a decade.

# Define the years
years = np.arange(2010, 2021)

# Badger population data in four different woodlands with various conservation strategies implemented
woodland_A = np.array([150, 152, 157, 159, 165, 170, 175, 178, 180, 185, 190])
woodland_B = np.array([130, 132, 135, 137, 142, 145, 150, 152, 158, 160, 162])
woodland_C = np.array([110, 112, 115, 117, 118, 120, 124, 126, 128, 130, 133])
woodland_D = np.array([95, 97, 100, 102, 104, 106, 108, 110, 112, 115, 117])

# Define colors and markers for each woodland
colors = ['#556B2F', '#8B4513', '#4682B4', '#DAA520']
markers = ['o', 's', 'd', '^']

# Plotting
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot lines and annotate data points with the population values
woodlands_data = [woodland_A, woodland_B, woodland_C, woodland_D]
woodland_names = ["Woodland A", "Woodland B", "Woodland C", "Woodland D"]

for data, name, color, marker in zip(woodlands_data, woodland_names, colors, markers):
    ax1.plot(years, data, label=name, color=color, marker=marker, linewidth=2, alpha=0.8)
    for (x, y) in zip(years, data):
        ax1.annotate(f'{y}', xy=(x, y), xytext=(0, 5),
                     textcoords='offset points', ha='center', fontsize=9, color=color)

# Set the title, labels, and grid
ax1.set_title('Impact of Conservation Strategies:\nMonitoring Badger Populations in British Woodlands (2010-2020)', 
              fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Badger Population', fontsize=14)
ax1.grid(True, linestyle='--', alpha=0.6)

# Add legend
ax1.legend(title='Woodlands', title_fontsize='13', loc='upper left', frameon=False)

# Customize the x-axis for better readability
plt.xticks(years, rotation=45)
plt.ylim(90, 200)  # Ensure all data points are visible

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()