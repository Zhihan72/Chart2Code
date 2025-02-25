import matplotlib.pyplot as plt
import numpy as np

# Define years and categories
years = np.arange(2023, 2031)

# Data for each category (number of exhibitors)
ai_exhibitors = [15, 20, 25, 30, 38, 42, 45, 48]
robotics_exhibitors = [10, 15, 22, 28, 37, 41, 44, 47]
quantum_exhibitors = [5, 8, 12, 18, 27, 32, 39, 43]
ar_exhibitors = [7, 10, 14, 19, 26, 33, 37, 40]

# Define cumulative values for stacked bar chart
robotics_cumulative = np.array(ai_exhibitors) + np.array(robotics_exhibitors)
quantum_cumulative = robotics_cumulative + np.array(quantum_exhibitors)
ar_cumulative = quantum_cumulative + np.array(ar_exhibitors)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(14, 7))

# Plot the stacked bar chart
ax.bar(years, ai_exhibitors, color='skyblue', alpha=0.8)
ax.bar(years, robotics_exhibitors, bottom=ai_exhibitors, color='lightgreen', alpha=0.8)
ax.bar(years, quantum_exhibitors, bottom=robotics_cumulative, color='salmon', alpha=0.8)
ax.bar(years, ar_exhibitors, bottom=quantum_cumulative, color='plum', alpha=0.8)

# Remove textual elements such as title, axis labels, and legends
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.set_yticks(np.arange(0, 150, step=10))
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()