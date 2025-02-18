import matplotlib.pyplot as plt
import numpy as np

# Data
energy_sources = ['Wind', 'Solar', 'Hydropower', 'Biomass', 'Other', 'Geothermal']
percentages = [27, 23, 18, 12, 12, 8]

# Sort data in descending order
sorted_indices = np.argsort(percentages)[::-1]
sorted_sources = [energy_sources[i] for i in sorted_indices]
sorted_percentages = [percentages[i] for i in sorted_indices]

single_color = '#2ca02c'

# Create a figure and a bar chart
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(sorted_sources, sorted_percentages, color=single_color, edgecolor='black')

ax.set_title("2022 Energy Mix Global Overview", fontsize=16, fontweight='light', pad=15)
ax.set_ylabel("Percentage (%)")
ax.set_xlabel("Energy Sources")

# Add a subplot for growth
years = np.arange(2012, 2023)
growth = [8, 10, 12, 15, 18, 21, 24, 28, 32, 35, 40]

ax_inset = fig.add_axes([0.7, 0.2, 0.2, 0.25])
ax_inset.plot(years, growth, linestyle='--', marker='o', color='green')
ax_inset.set_title("Growth of Renewables (2012-2022)", fontsize=9)
ax_inset.set_ylabel("Percentage (%)", fontsize=7)
ax_inset.set_xlabel("Yearly Progress", fontsize=7)
ax_inset.tick_params(axis='both', labelsize=7)

plt.tight_layout()
plt.show()