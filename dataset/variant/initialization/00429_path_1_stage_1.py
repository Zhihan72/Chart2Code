import matplotlib.pyplot as plt
import numpy as np

# Data setup
age_groups = ['Children', 'Teenagers', 'Young Adults', 'Middle-Aged', 'Seniors']
instruments = ['Piano', 'Guitar', 'Violin', 'Drums', 'Flute', 'Trumpet', 'Saxophone']

# Number of people in each age group who prefer each instrument
preferences = np.array([
    [30, 40, 45, 20, 10, 15, 25],  # Children
    [20, 55, 35, 45, 20, 25, 30],  # Teenagers
    [50, 35, 30, 40, 15, 30, 20],  # Young Adults
    [60, 50, 30, 25, 10, 20, 15],  # Middle-Aged
    [20, 25, 20, 10, 50, 20, 40]   # Seniors
])

# Reverse half of the data for diverging effect around the central axis
preferences[:, :preferences.shape[1]//2] *= -1

# Create the plot
fig, ax = plt.subplots(figsize=(14, 9))

# Define bar positions and width
bar_width = 0.12
indices = np.arange(len(age_groups))

# Colors for the instruments
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Plotting diverging bars for each age group
for i, instrument in enumerate(instruments):
    bars = ax.barh(
        indices, 
        preferences[:, i], 
        height=bar_width, 
        label=instrument, 
        color=colors[i],
        left=indices * bar_width,
        edgecolor='black'
    )

# Set labels and title
ax.set_xlabel('Number of People', fontsize=12)
ax.set_ylabel('Age Groups', fontsize=12)
ax.set_title('Musical Instrument Preference Diverging Bar Chart', fontsize=16, fontweight='bold')
ax.set_yticks(indices)
ax.set_yticklabels(age_groups, fontsize=10)

# Add legend
ax.legend(title='Instruments', fontsize=9, loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=4)

# Adding grid for better readability
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Improve the layout
plt.tight_layout()

# Display the plot
plt.show()