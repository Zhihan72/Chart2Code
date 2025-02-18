import matplotlib.pyplot as plt
import numpy as np

# Define months
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Data for recycling rates (in tons)
plastic_recycling = [8.5, 8.7, 9.1, 9.5, 9.7, 10.0, 9.8, 9.9, 10.3, 10.5, 10.7, 11.0]
glass_recycling = [5.0, 5.1, 5.2, 5.4, 5.6, 5.7, 5.8, 5.9, 6.0, 6.2, 6.3, 6.5]
metal_recycling = [3.0, 3.1, 3.2, 3.4, 3.5, 3.7, 3.6, 3.8, 4.0, 4.1, 4.3, 4.4]
paper_recycling = [12.0, 12.3, 12.5, 13.0, 13.2, 13.5, 13.6, 13.8, 14.0, 14.3, 14.5, 14.8]

# Total waste recycling for checking progress
total_recycling = np.array(plastic_recycling) + np.array(glass_recycling) + np.array(metal_recycling) + np.array(paper_recycling)

# Calculate the percentage contribution of each material
plastic_percentage = (np.array(plastic_recycling) / total_recycling) * 100
glass_percentage = (np.array(glass_recycling) / total_recycling) * 100
metal_percentage = (np.array(metal_recycling) / total_recycling) * 100
paper_percentage = (np.array(paper_recycling) / total_recycling) * 100

# Plotting the data
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# Bar chart for monthly recycling rates
bar_width = 0.2
x_indexes = np.arange(len(months))

ax[0].bar(x_indexes - bar_width, plastic_recycling, width=bar_width, color='#FF5733', alpha=0.8)
ax[0].bar(x_indexes, glass_recycling, width=bar_width, color='#33FF57', alpha=0.8)
ax[0].bar(x_indexes + bar_width, metal_recycling, width=bar_width, color='#3357FF', alpha=0.8)
ax[0].bar(x_indexes + 2*bar_width, paper_recycling, width=bar_width, color='#FFD700', alpha=0.8)

# Titles and labels
ax[0].set_title('Monthly Recycling Rates in GreenVille (in tons)', fontsize=14, fontweight='bold')
ax[0].set_xlabel('Months', fontsize=12)
ax[0].set_ylabel('Recycled Waste (Tons)', fontsize=12)
ax[0].set_xticks(x_indexes + bar_width / 2)
ax[0].set_xticklabels(months, rotation=45, ha='right')

# Stacked bar chart for percentage contributions
ax[1].bar(months, plastic_percentage, color='#FF5733', alpha=0.8)
ax[1].bar(months, glass_percentage, bottom=plastic_percentage, color='#33FF57', alpha=0.8)
ax[1].bar(months, metal_percentage, bottom=plastic_percentage+glass_percentage, color='#3357FF', alpha=0.8)
ax[1].bar(months, paper_percentage, bottom=plastic_percentage+glass_percentage+metal_percentage, color='#FFD700', alpha=0.8)

# Titles and labels
ax[1].set_title('Percentage Contributions of Recycled Materials (2023)', fontsize=14, fontweight='bold')
ax[1].set_xlabel('Months', fontsize=12)
ax[1].set_ylabel('Percentage (%)', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()