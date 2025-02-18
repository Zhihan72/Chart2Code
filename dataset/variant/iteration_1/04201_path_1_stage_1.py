import matplotlib.pyplot as plt
import numpy as np

# Data: Number of stars per brightness range in different constellations for each month 
brightness_bins = ['0-2', '2-4', '4-6', '6-8', '8-10']
stars_jun = [20, 30, 55, 40, 25]
stars_dec = [25, 35, 45, 50, 30]

# Creating figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

# Plotting histograms for june and december
axs[0].bar(brightness_bins, stars_jun, color='lightgreen', edgecolor='black')
axs[0].set_title('Star Brightness in Jun')
axs[0].set_xlabel('Brightness Range (Magnitude)')
axs[0].set_ylabel('Number of Stars')
axs[0].grid(axis='y', linestyle='--', alpha=0.7)

axs[1].bar(brightness_bins, stars_dec, color='lightcoral', edgecolor='black')
axs[1].set_title('Star Brightness in Dec')
axs[1].set_xlabel('Brightness Range (Magnitude)')
axs[1].grid(axis='y', linestyle='--', alpha=0.7)

# Global plot settings
fig.suptitle('Brightness of Stars in Different Constellations:\nObservation Data for Selected Months', fontsize=16, fontweight='bold')

# Using tight_layout to optimize the layout of subplots
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plot
plt.show()