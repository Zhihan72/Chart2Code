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

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Calculate the bottom values for stacking
bottom_values = np.zeros(len(years))

# Plot each genre as a stacked bar
for genre_data, color, label in zip(
    [action, comedy, drama, sci_fi, animation],
    colors,
    ['Humor', 'Thrill', 'Serious', 'Futuristic', 'Cartoon']  # Changed labels
):
    ax.bar(years, genre_data, bottom=bottom_values, label=label, color=color, alpha=0.85)
    bottom_values += genre_data

# Adding a shuffled title and labels
ax.set_title('Movie Revenue Trends (2018-2022)', fontsize=16, fontweight='bold', pad=20)  # Changed title
ax.set_xlabel('Timeline', fontsize=14, labelpad=10)  # Changed x-axis label
ax.set_ylabel('Earnings (Million USD)', fontsize=14, labelpad=10)  # Changed y-axis label

# Customize ticks
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Adding the legend
ax.legend(title='Category', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)  # Changed legend title

# Add a grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to fit everything nicely
plt.tight_layout()

# Display the plot
plt.show()