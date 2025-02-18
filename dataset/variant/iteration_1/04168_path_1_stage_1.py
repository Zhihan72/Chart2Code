import matplotlib.pyplot as plt
import numpy as np

# Define the years for analysis
years = np.arange(1990, 2021)

# Representing the usage of different music formats over the years (in percentage)
physical_media = np.array([90, 87, 85, 82, 76, 70, 65, 60, 55, 50, 45, 40, 35, 32, 28, 24, 20, 18, 15, 12, 10, 8, 6, 5, 4, 3, 3, 3, 2, 1, 1])
digital_downloads = np.array([0, 1, 2, 4, 6, 7, 8, 9, 12, 15, 20, 25, 30, 35, 40, 42, 45, 48, 50, 52, 53, 54, 56, 58, 60, 60, 58, 55, 50, 48, 45])
streaming = np.array([0, 0, 0, 0, 0, 0, 1, 2, 3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 48, 50, 55, 60, 62, 65, 68, 72, 75, 78, 82, 85, 88])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Colors for different music formats
colors = ['#ff9999', '#66b3ff', '#99ff99']

# Plot the data without 'others'
ax.stackplot(years, physical_media, digital_downloads, streaming, 
             labels=['Physical Media', 'Digital Downloads', 'Streaming'], 
             colors=colors, alpha=0.85)

# Title and labels
ax.set_title("Evolution of Music Consumption Formats (1990-2020)", fontsize=18, fontweight='bold')
ax.set_xlabel("Year", fontsize=14, fontweight='semibold')
ax.set_ylabel("Percentage of Total Consumption (%)", fontsize=14, fontweight='semibold')

# Add grid lines for better readability
ax.grid(linestyle='--', alpha=0.5)

# Customize the legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Music Formats', title_fontsize='13', fontsize=11)

# Set x-axis ticks
plt.xticks(years[::2])

# Add annotations for significant milestones and trends
ax.annotate('Launch of Napster\n(first major P2P file sharing service)', 
            xy=(1999, 50), xytext=(2001, 70), 
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax.annotate('Streaming services gain traction', 
            xy=(2015, 35), xytext=(2010, 50), 
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax.annotate('Covid-19 Pandemic\nBoost in Streaming and Digital Downloads', 
            xy=(2020, 75), xytext=(2014, 80), 
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the final plot
plt.show()