import matplotlib.pyplot as plt
import numpy as np

# Publishers and genres
publishers = ['Publisher A', 'Publisher C', 'Publisher D']
genres = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy', 'Historical']

# Publication data for five years (Year 1-5) without Publisher B
data = np.array([
    [120, 150, 80, 100, 90],     # Publisher A
    [90, 130, 110, 95, 85],      # Publisher C
    [170, 160, 150, 140, 130]    # Publisher D
])

# Years
years = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']

# Plotting the data

fig, ax = plt.subplots(figsize=(12, 8))

# Number of bars per group
num_years = len(years)
num_publishers = data.shape[0]

# Bar widths and positions
bar_width = 0.15
positions = np.arange(len(genres))

# Colors for publishers
colors = ['#FF6347', '#32CD32', '#FFD700']  # Updated colors after removing Publisher B

# Plot bar groups for each publisher
for idx, (publisher, color) in enumerate(zip(publishers, colors)):
    bar_positions = positions + idx * bar_width
    ax.bar(bar_positions, data[idx], width=bar_width, color=color, label=publisher, alpha=0.75)

# Customizing the plot
ax.set_xlabel('Book Genres', fontsize=12)
ax.set_ylabel('Number of Publications', fontsize=12)
ax.set_title('Annual Book Publications by Genre\nAcross Major Publishers', fontsize=14, fontweight='bold')
ax.set_xticks(positions + bar_width * (num_publishers - 1) / 2)
ax.set_xticklabels(genres)

# Adding a legend
ax.legend(title='Publishers', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Adding data labels above the bars
for idx, (publisher, color) in enumerate(zip(publishers, colors)):
    bar_positions = positions + idx * bar_width
    for x, y in zip(bar_positions, data[idx]):
        plt.text(x, y + 2, y, ha='center', va='bottom', fontsize=10, color=color)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()