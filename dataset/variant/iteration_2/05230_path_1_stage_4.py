import matplotlib.pyplot as plt
import numpy as np

# Data for popularity (percentage)
languages = ['Python', 'JavaScript', 'Java', 'C++']
popularity = [30, 25, 20, 15]

# Data for projected job demand growth (in thousands)
years = np.array([2023, 2024, 2025, 2026, 2027])
projected_jobs_growth = {
    'Python': [150, 155, 160, 165, 170],
    'JavaScript': [130, 135, 140, 145, 150],
    'Java': [120, 122, 124, 126, 128],
    'C++': [100, 102, 104, 106, 108]
}

# Choose a single color
single_color = '#3776AB'

# Create the figure and axis objects
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the bar chart for popularity with a single color
bars = ax1.barh(languages, popularity, color=single_color, height=0.6)

# Add a secondary y-axis for the line plot
ax2 = ax1.twinx()

# Plot the line charts for projected job demand growth with a single color
for idx, (language, growth) in enumerate(projected_jobs_growth.items()):
    ax2.plot(growth, years, color=single_color, linestyle='-', marker='o')

# Set axis limits to improve visualization
ax1.set_xlim(0, 35)
ax2.set_ylim(2022, 2028)

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()