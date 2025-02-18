import numpy as np
import matplotlib.pyplot as plt

# Backstory:
# Research on the correlation between different types of soil and crop yields in a farming community.
# Study includes data collected for three types of soil - Clay, Loam, and Sandy - over multiple years.

# Data representation
years = np.array([2010, 2012, 2014, 2016, 2018, 2020, 2022])
clay_yield = np.array([20, 22, 21, 24, 26, 25, 28])
loam_yield = np.array([30, 32, 33, 35, 36, 38, 40])
sandy_yield = np.array([15, 17, 16, 18, 20, 19, 21])

# Secondary Data for subplot: Soil PH Values
soil_types = ['Clay', 'Loam', 'Sandy']
average_ph = [6.5, 7.2, 6.8]

# Create a 1x2 subplot layout
fig, axs = plt.subplots(1, 2, figsize=(15, 7))

# First subplot: Crop Yield vs Years Scatter Plot
axs[0].scatter(years, clay_yield, color='brown', label='Clay Soil', s=100, alpha=0.7, edgecolors='k', marker='o')
axs[0].scatter(years, loam_yield, color='green', label='Loam Soil', s=100, alpha=0.7, edgecolors='k', marker='s')
axs[0].scatter(years, sandy_yield, color='yellow', label='Sandy Soil', s=100, alpha=0.7, edgecolors='k', marker='D')

# Add trendlines for each soil type
clay_coefs = np.polyfit(years, clay_yield, 1)
loam_coefs = np.polyfit(years, loam_yield, 1)
sandy_coefs = np.polyfit(years, sandy_yield, 1)

axs[0].plot(years, np.poly1d(clay_coefs)(years), color='brown', linestyle='--', label='Clay Trendline')
axs[0].plot(years, np.poly1d(loam_coefs)(years), color='green', linestyle='--', label='Loam Trendline')
axs[0].plot(years, np.poly1d(sandy_coefs)(years), color='yellow', linestyle='--', label='Sandy Trendline')

# Add plot details to the first subplot
axs[0].set_title('Crop Yield Over Time on Different Soil Types', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Crop Yield (tons per hectare)', fontsize=12)
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].legend(title='Soil Types', fontsize=10, loc='upper left')

# Second subplot: Soil PH Values Bar Plot
axs[1].bar(soil_types, average_ph, color=['brown', 'green', 'yellow'], alpha=0.7)
axs[1].set_title('Average PH Values of Different Soil Types', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Soil Type', fontsize=12)
axs[1].set_ylabel('PH Value', fontsize=12)
axs[1].set_ylim(6, 8)
axs[1].grid(True, linestyle='--', alpha=0.6)
axs[1].set_yticks(np.arange(6, 8.5, 0.5))

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()