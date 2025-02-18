import matplotlib.pyplot as plt
import numpy as np

# Data preparation
years = ['2018', '2019', '2020', '2021']
genres = ['Action', 'Adventure', 'Puzzle', 'Sports', 'RPG']

# Units sold (in thousands) for each genre over the years
units_sold = {
    'Action': [150, 180, 200, 230],
    'Adventure': [120, 130, 140, 150],
    'Puzzle': [90, 100, 110, 120],
    'Sports': [110, 115, 120, 125],
    'RPG': [80, 85, 90, 95]
}

# Colors for each genre
colors = ['#ff6666', '#ffcc99', '#99ff99', '#66b3ff', '#c2c2f0']

# Calculate the midpoint for diverging bars
baseline = np.zeros(len(years))

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each genre's units sold as a diverging bar chart
for i, (genre, values) in enumerate(units_sold.items()):
    adjusted_values = np.array(values) - np.mean(values)
    ax.bar(years, adjusted_values, label=genre, color=colors[i], alpha=0.8, bottom=baseline)
    baseline += adjusted_values

# Set labels and title
ax.set_xlabel('Years', fontsize=12, weight='bold')
ax.set_ylabel('Deviation from Mean (Thousands)', fontsize=12, weight='bold')
ax.set_title('Diverging Video Game Sales by Genre Over Years', fontsize=16, weight='bold', pad=20)
ax.legend(title='Genres', fontsize=10, title_fontsize='12', loc='upper right')

# Add grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout for better fit and readability
plt.tight_layout()

# Show plot
plt.show()