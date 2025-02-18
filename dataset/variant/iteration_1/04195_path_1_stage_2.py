import matplotlib.pyplot as plt
import numpy as np

# Define years
years = np.arange(2010, 2021)

# Randomly altered data for digital content consumption (in hours per week)
streaming_services = np.array([3, 6, 9, 14, 24, 36, 44, 56, 68, 71, 79])
podcasts = np.array([2, 1, 4, 6, 10, 9, 16, 20, 23, 24, 29])
ebooks = np.array([1, 3, 2, 5, 4, 8, 9, 11, 11, 14, 16])
online_magazines = np.array([4, 3, 5, 8, 8, 11, 11, 13, 14, 15, 16])

# Create a figure and adjust size
fig, ax = plt.subplots(figsize=(12, 8))

# Plot data using multiple line charts
ax.plot(years, streaming_services, marker='o', color='#1f77b4')
ax.plot(years, podcasts, marker='o', color='#ff7f0e')
ax.plot(years, ebooks, marker='o', color='#2ca02c')
ax.plot(years, online_magazines, marker='o', color='#d62728')

# Set grid
ax.grid(True, linestyle='--', alpha=0.7)

# Rotate x-ticks for better readability
plt.xticks(rotation=45, ha='right')

# Add a tight layout
plt.tight_layout()

# Show the plot
plt.show()