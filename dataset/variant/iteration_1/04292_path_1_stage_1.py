import matplotlib.pyplot as plt
import numpy as np

# Define years from 2012 to 2022
years = np.arange(2012, 2023)

# Construct data for different food delivery services
services = {
    "Digital App Dispatch": [5, 10, 20, 35, 45, 50, 55, 60, 65, 70, 75],
    "In-House Restaurant Delivery": [40, 35, 30, 28, 25, 23, 20, 18, 16, 15, 12],
    "Pickup Service": [55, 50, 45, 37, 30, 25, 20, 15, 10, 7, 5]
}

# Convert list of services to numpy array for stacking
stacked_data = np.array(list(services.values()))

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 9))

# Plotting the stacked area chart
ax.stackplot(years, stacked_data, labels=services.keys(), alpha=0.8)

# Title and labels
ax.set_title("Trends in Food Dispatch Preferences (2012-2022)", fontsize=16, fontweight='bold')
ax.set_xlabel("Timeline", fontsize=12)
ax.set_ylabel("Market Fraction (%)", fontsize=12)

# Adding a legend with more space and styling
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Service Types', fontsize=10, title_fontsize='12', frameon=True)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Grid settings
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Automatic layout adjustment to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()