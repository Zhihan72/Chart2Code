import matplotlib.pyplot as plt
import numpy as np

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
ax1.bar(years - bar_width/2, gardens_created, bar_width, color='#66c2a5')

# Bar chart for volunteers joined each year
ax2 = ax1.twinx()
ax2.bar(years + bar_width/2, volunteers_joined, bar_width, color='#fc8d62')

# Add average garden area as a line plot on secondary y-axis
ax2.plot(years, average_area, color='blue', marker='o', linestyle='-', lw=2, markerfacecolor='blue')

ax1.set_xticks(years)
ax1.set_xticklabels([])

plt.tight_layout()
plt.show()