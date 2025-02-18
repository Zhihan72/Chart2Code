import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# In the futuristic city of Techville, there are annual events showcasing emerging 
# technologies in three major fields: Artificial Intelligence, Robotics, and Quantum Computing. 
# The event organizers track the number of exhibitors in each field to analyze trends over the years.

# Define years and categories
years = np.arange(2023, 2031)
categories = ['Artificial Intelligence', 'Robotics', 'Quantum Computing']

# Data for each category (number of exhibitors)
ai_exhibitors = [15, 20, 25, 30, 38, 42, 45, 48]
robotics_exhibitors = [10, 15, 22, 28, 37, 41, 44, 47]
quantum_exhibitors = [5, 8, 12, 18, 27, 32, 39, 43]

# Define cumulative values for stacked bar chart
robotics_cumulative = np.array(ai_exhibitors) + np.array(robotics_exhibitors)
quantum_cumulative = robotics_cumulative + np.array(quantum_exhibitors)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(14, 7))

# Plot the stacked bar chart
ax.bar(years, ai_exhibitors, label='Artificial Intelligence', color='skyblue', alpha=0.8)
ax.bar(years, robotics_exhibitors, bottom=ai_exhibitors, label='Robotics', color='lightgreen', alpha=0.8)
ax.bar(years, quantum_exhibitors, bottom=robotics_cumulative, label='Quantum Computing', color='salmon', alpha=0.8)

# Title and labels
ax.set_title('Exhibitor Trends in Techville’s Annual Showcase (2023-2030)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Exhibitors', fontsize=14)

# Adjust x-axis ticks and labels for better readability
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.set_yticks(np.arange(0, 150, step=10))

# Add legend and grid
ax.legend(loc='upper left', fontsize=12, title='Fields')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()