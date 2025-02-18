import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Scores by subject
math_scores = np.array([70, 72, 75, 78, 80, 83, 85, 88, 90, 93, 95])
science_scores = np.array([65, 68, 70, 73, 76, 79, 81, 85, 87, 90, 93])
english_scores = np.array([60, 63, 67, 70, 73, 76, 79, 82, 84, 87, 89])

# Combine data for the area plot
scores = np.array([math_scores, science_scores, english_scores])

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the stacked area chart with new colors
ax.stackplot(years, scores, labels=['Mathematics', 'Science', 'English'],
             colors=['#FFB6C1', '#20B2AA', '#FFD700'], alpha=0.8)

# Set title and labels
ax.set_title("Techville Student Performance Evolution (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Scores', fontsize=14)

# Add grid lines for better readability
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Position legend to avoid obscuring the data
ax.legend(loc='upper left', title='Subjects', fontsize=10)

# Customize x-axis ticks
ax.set_xticks(years)
plt.xticks(rotation=45)

# Automatically adjust layout to fit all elements comfortably
plt.tight_layout()

# Show the plot
plt.show()