import matplotlib.pyplot as plt
import numpy as np

# Define months and corresponding average rainfall (in millimeters)
months = np.arange(1, 13)
rainfall = np.array([85, 78, 92, 110, 134, 158, 102, 75, 65, 45, 40, 70])

# Sort the rainfall data and associated months for a sorted bar chart
sorted_indices = np.argsort(rainfall)
sorted_rainfall = rainfall[sorted_indices]
sorted_months = months[sorted_indices]
sorted_month_labels = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])[sorted_indices]

# Define a consistent color for all bars
consistent_color = 'skyblue'

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot sorted bar chart for average monthly rainfall
bars = ax.bar(sorted_month_labels, sorted_rainfall, color=consistent_color, edgecolor='black')

# Annotate each bar with the rainfall amount
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}', xy=(bar.get_x() + bar.get_width() / 2, height), 
                xytext=(0, 3), textcoords='offset points', ha='center', fontsize=10, color='black')

# Add titles and labels
ax.set_title("Average Monthly Rainfall in Rainforestia (Sorted)\n(One Year Period)", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Month", fontsize=14)
ax.set_ylabel("Average Rainfall (mm)", fontsize=14)

# Add gridlines
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Automatically adjust layout before displaying
plt.tight_layout()

# Display the plot
plt.show()