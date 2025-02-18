import matplotlib.pyplot as plt
import numpy as np

# Backstory: 
# This chart displays the annual revenue of different movie genres over the last five years. 
# Movie genres have been diversifying, and this chart helps in understanding which genres are performing better with time.

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
for genre_data, color, label in zip([action, comedy, drama, sci_fi, animation], colors, ['Action', 'Comedy', 'Drama', 'Sci-Fi', 'Animation']):
    ax.bar(years, genre_data, bottom=bottom_values, label=label, color=color, alpha=0.85)
    bottom_values += genre_data

# Adding title and labels
ax.set_title('Annual Revenue of Movie Genres (2018-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14, labelpad=10)
ax.set_ylabel('Revenue (in Million USD)', fontsize=14, labelpad=10)

# Customize ticks
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Adding the legend
ax.legend(title='Genres', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Add a grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to fit everything nicely
plt.tight_layout()

# Display the plot
plt.show()