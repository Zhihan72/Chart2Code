import matplotlib.pyplot as plt
import numpy as np

# Solar power generation in a futuristic Mars colony scenario
years = np.arange(2030, 2041)
solar_panels_A = np.array([50, 55, 60, 62, 65, 67, 70, 73, 75, 78, 80])
solar_panels_B = np.array([45, 50, 52, 55, 60, 62, 65, 68, 70, 72, 75])
solar_panels_C = np.array([40, 42, 45, 48, 50, 55, 57, 60, 65, 67, 70])

# Create a figure with multiple subplots
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting the data for each set of solar panels
ax.plot(years, solar_panels_A, label='Solar Panels Array A', linestyle='-', marker='o', color='#ff5733', linewidth=2, markersize=6)
ax.plot(years, solar_panels_B, label='Solar Panels Array B', linestyle='--', marker='s', color='#33ff57', linewidth=2, markersize=6)
ax.plot(years, solar_panels_C, label='Solar Panels Array C', linestyle=':', marker='^', color='#3357ff', linewidth=2, markersize=6)

# Annotations to highlight significant points
ax.annotate('Milestone 1', xy=(2035, 67), xytext=(2033, 72), 
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold')
ax.annotate('Milestone 2', xy=(2040, 67), xytext=(2038, 74),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold')

# Define titles and labels
ax.set_title('Mars Colony Solar Power Generation:\nProgress Across Different Arrays (2030-2040)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Power Generation (GW)', fontsize=12)

# Grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Set x-ticks and y-ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(40, 85, step=5))

# Add legend with custom settings to avoid data overlap
ax.legend(loc='upper left', fontsize=10, title='Solar Panel Arrays', title_fontsize='12')

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()