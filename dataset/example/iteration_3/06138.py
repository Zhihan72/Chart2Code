import matplotlib.pyplot as plt
import numpy as np

# Backstory: We are analyzing the growth of various types of hobbies and leisure activities from 2010 to 2020.
# The chart visualizes how people's engagement in different hobbies has evolved over the years, helping trend analysts understand the shifting patterns of leisure preferences.

# Define the years
years = np.arange(2010, 2021)

# Define engagement data for each hobby (in arbitrary engagement units)
reading = np.array([50, 52, 53, 54, 55, 56, 57, 59, 60, 62, 65])
gaming = np.array([20, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65])
sports = np.array([30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])
traveling = np.array([10, 12, 15, 18, 22, 26, 30, 35, 40, 45, 50])
cooking = np.array([15, 16, 18, 19, 20, 21, 23, 25, 27, 28, 30])
crafting = np.array([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

# Stack data for plotting
hobbies_data = np.vstack([reading, gaming, sports, traveling, cooking, crafting])

# Define the colors
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0', '#FFB6C1']

# Create the stacked area chart
plt.figure(figsize=(14, 8))
plt.stackplot(years, hobbies_data, labels=['Reading', 'Gaming', 'Sports', 'Traveling', 'Cooking', 'Crafting'], colors=colors, alpha=0.8)

# Title and axis labels
plt.title('Evolution of Hobbies and Leisure Activities (2010-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Engagement Units', fontsize=14)

# Adding gridlines for better readability
plt.grid(visible=True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Place legend outside the plot
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12, title='Hobbies')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()