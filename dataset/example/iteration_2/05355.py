import matplotlib.pyplot as plt
import numpy as np

# Backstory: We are simulating the growth of cloned plant species over the span of a year on a new terraform Mars base. 
# We measure the weekly height growth of three different plant species to understand their growth patterns.

# Simulated data: Heights of three different plant species over 52 weeks
weeks = np.arange(1, 53)

# Specified growth trends for three different plant species
species_1_growth = 2 + 0.5 * weeks + 0.1 * np.sin(2 * np.pi * weeks / 10)  # Slow-growing species with some periodic fluctuations
species_2_growth = 3 + 0.6 * weeks + 0.2 * np.cos(2 * np.pi * weeks / 15)  # Moderate growth with slight cyclic variation
species_3_growth = 1.5 + 0.8 * weeks + 0.15 * np.sin(2 * np.pi * weeks / 8)  # Fast-growing species with more frequent fluctuations

# Creating the line plot with subplots for a clearer view
fig, ax = plt.subplots(figsize=(14, 8))

# Plot lines for each species
ax.plot(weeks, species_1_growth, marker='o', linestyle='-', label='Species A', color='#1a9850', linewidth=2)
ax.plot(weeks, species_2_growth, marker='s', linestyle='--', label='Species B', color='#d73027', linewidth=2)
ax.plot(weeks, species_3_growth, marker='^', linestyle=':', label='Species C', color='#4575b4', linewidth=2)

# Highlight some points of interest with annotations
ax.annotate('Rapid growth start', xy=(10, species_1_growth[9]), xytext=(15, 20),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9, fontweight='bold')
ax.annotate('Stable growth midpoint', xy=(26, species_2_growth[25]), xytext=(30, 34),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9, fontweight='bold')

# Label data points selectively to avoid clutter
for i, week in enumerate(weeks):
    if i % 10 == 0:  # label every 10th week
        ax.text(week, species_1_growth[i] + 0.5, f'{species_1_growth[i]:.1f}', fontsize=8, ha='center', va='bottom')
        ax.text(week, species_2_growth[i] + 0.5, f'{species_2_growth[i]:.1f}', fontsize=8, ha='center', va='bottom')
        ax.text(week, species_3_growth[i] + 0.5, f'{species_3_growth[i]:.1f}', fontsize=8, ha='center', va='bottom')

# Customizing the plot with a detailed title
plt.title("Simulated Growth of Cloned Plant Species Over One Year on Mars\nWeekly Height Measurements in Controlled Environments", 
          fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Week of the Year', fontsize=12)
ax.set_ylabel('Height (cm)', fontsize=12)
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.legend(title='Plant Species', loc='upper left', fontsize=10, frameon=False)
plt.xticks(weeks[::4], rotation=45)  # Rotate x-ticks and show every 4th week for better spacing
plt.tight_layout()

# Show the plot
plt.show()