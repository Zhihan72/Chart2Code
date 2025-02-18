import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2000 to 2025
years = np.arange(2000, 2026)

# Food consumption (in kilotons) across different types over the years
fruits_consumption = [20, 22, 24, 26, 29, 32, 35, 38, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 85, 90, 95, 100, 105, 110, 115]
vegetables_consumption = [15, 17, 20, 22, 25, 28, 32, 35, 38, 42, 46, 50, 54, 58, 63, 68, 73, 78, 83, 88, 93, 98, 104, 110, 116, 122]
meats_consumption = [25, 28, 30, 32, 35, 39, 43, 47, 51, 55, 60, 65, 70, 75, 80, 85, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144]
dairy_consumption = [10, 10.5, 11, 11.8, 12.6, 13.5, 14.4, 15.3, 16.2, 17.2, 18.2, 19.2, 20.2, 21.2, 22.2, 23.2, 24.2, 25.2, 26.2, 27.2, 28.2, 29.2, 30.2, 31.2, 32.2, 33.2]

# Stack data for plotting
data = np.vstack([fruits_consumption, vegetables_consumption, meats_consumption, dairy_consumption])

# Define distinct colors for each food type
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Create the area plot
fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, data, labels=['Fruits', 'Vegetables', 'Meats', 'Dairy'],
             colors=colors, alpha=0.8)

# Titles and labels
ax.set_title('Global Food Consumption Trends\nAcross Different Food Types (2000-2025)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Consumption (Kilotons)', fontsize=12)

# Adding a legend
ax.legend(loc='upper left', title="Food Types")

# Customizing grid and style
ax.grid(linestyle='--', linewidth=0.5, alpha=0.7)

# Highlighting significant trends
ax.annotate('Significant rise in Meat consumption', xy=(2015, 70), xytext=(2010, 90),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='red')

ax.annotate('Gradual increase in Vegetable consumption', xy=(2018, 82), xytext=(2015, 100),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='green')

# Rotating x-axis labels for better readability
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()