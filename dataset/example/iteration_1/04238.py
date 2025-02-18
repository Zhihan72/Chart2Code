import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The city council of Greentown has initiated an expansive urban gardening project over five years
# to increase the amount of green spaces and promote community engagement.

# Years of the project
years = np.array([2019, 2020, 2021, 2022, 2023])

# Number of urban gardens created each year
gardens_created = np.array([5, 15, 25, 40, 60])

# Number of community volunteers joining each year
volunteers_joined = np.array([50, 120, 180, 250, 320])

# Average area of gardens created each year (in square meters)
average_area = np.array([200, 250, 300, 350, 400])

# Plotting the bar chart for gardens created each year and volunteers joined each year
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart for gardens created each year
bar_width = 0.35
bar1 = ax1.bar(years - bar_width/2, gardens_created, bar_width, label='Gardens Created', color='#66c2a5')

# Bar chart for volunteers joined each year
ax2 = ax1.twinx()
bar2 = ax2.bar(years + bar_width/2, volunteers_joined, bar_width, label='Volunteers Joined', color='#fc8d62')

# Add average garden area as a line plot on secondary y-axis
line = ax2.plot(years, average_area, color='blue', marker='o', linestyle='-', label='Avg Garden Area', lw=2, markerfacecolor='blue')

# Title and labels
ax1.set_title("Urban Gardening Project in Greentown: Growth and Development (2019-2023)", fontsize=14, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Gardens Created", fontsize=12)
ax2.set_ylabel("Volunteers & Avg Garden Area (sq m)", fontsize=12)

ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Legends
bars = bar1 + bar2
labels = [b.get_label() for b in bars] + ['Avg Garden Area']
ax2.legend(bars, labels, loc='upper left')

# Ensure a clean layout
plt.tight_layout()

# Show the plot
plt.show()