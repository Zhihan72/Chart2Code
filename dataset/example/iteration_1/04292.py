import matplotlib.pyplot as plt
import numpy as np

# Backstory: The chart represents the usage of different types of food delivery services over the past decade (2012-2022).
# This data is visualized to show how consumers' preferences among various food delivery services evolved over these years.

# Define years from 2012 to 2022
years = np.arange(2012, 2023)

# Constructing data for different food delivery services (in percentage usage of total market)
services = {
    "App-based Delivery": [5, 10, 20, 35, 45, 50, 55, 60, 65, 70, 75],
    "Restaurant Direct Delivery": [40, 35, 30, 28, 25, 23, 20, 18, 16, 15, 12],
    "Takeaway": [55, 50, 45, 37, 30, 25, 20, 15, 10, 7, 5]
}

# Convert list of services to numpy array for stacking
stacked_data = np.array(list(services.values()))

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 9))

# Plotting the stacked area chart
ax.stackplot(years, stacked_data, labels=services.keys(), alpha=0.8)

# Title and labels
ax.set_title("Evolution of Food Delivery Service Usage\n(2012-2022)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Usage Percentage (%)", fontsize=12)

# Adding a legend with more space and styling
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Delivery Services', fontsize=10, title_fontsize='12', frameon=True)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Grid settings
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Automatic layout adjustment to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()