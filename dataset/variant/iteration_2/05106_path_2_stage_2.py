import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2018, 2023)

# Annual revenue data for each genre in millions of USD
action = np.array([500, 550, 600, 650, 700])
comedy = np.array([300, 310, 320, 330, 340])
drama = np.array([400, 450, 460, 470, 480])
sci_fi = np.array([200, 210, 220, 250, 300])
animation = np.array([150, 160, 170, 180, 190])

# Colors for each genre
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

fig, ax = plt.subplots(figsize=(12, 8))

# Parameters for the bars
bar_width = 0.15
x_indices = np.arange(len(years))

# Plot each genre as a grouped bar
ax.bar(x_indices - 2*bar_width, action, width=bar_width, color=colors[0], alpha=0.85)
ax.bar(x_indices - bar_width, comedy, width=bar_width, color=colors[1], alpha=0.85)
ax.bar(x_indices, drama, width=bar_width, color=colors[2], alpha=0.85)
ax.bar(x_indices + bar_width, sci_fi, width=bar_width, color=colors[3], alpha=0.85)
ax.bar(x_indices + 2*bar_width, animation, width=bar_width, color=colors[4], alpha=0.85)

# Adding title and labels
ax.set_title('Annual Revenue of Movie Genres (2018-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14, labelpad=10)
ax.set_ylabel('Revenue (in Million USD)', fontsize=14, labelpad=10)

# Customize ticks
ax.set_xticks(x_indices)
ax.set_xticklabels(years, rotation=45, ha='right')

# Adjust layout to fit everything nicely
plt.tight_layout()

# Display the plot
plt.show()