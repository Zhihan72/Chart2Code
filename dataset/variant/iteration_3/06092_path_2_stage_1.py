import matplotlib.pyplot as plt
import numpy as np

# Define age groups and genres
age_groups = ['Kids (5-12)', 'Teens (13-19)', 'Adults (20-40)', 'Seniors (40+)']
genres = ['Fantasy', 'Science Fiction', 'Mystery', 'Non-fiction', 'Romance', 'Horror']

# Percentage preference data for each genre in each age group
data = {
    'Kids (5-12)': [40, 10, 5, 20, 20, 5],
    'Teens (13-19)': [25, 30, 10, 15, 15, 5],
    'Adults (20-40)': [20, 15, 25, 30, 5, 5],
    'Seniors (40+)': [10, 10, 35, 30, 5, 10]
}

# Colors for genres
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Summary data for an overall pie chart
total_per_genre = np.array([sum(data[group][i] for group in age_groups) for i in range(len(genres))])

# Create subplots
fig, axs = plt.subplots(2, 3, figsize=(18, 12))

# Plot each age group's data
for i, (group, group_data) in enumerate(data.items()):
    ax = axs[i // 3, i % 3]
    
    wedges, _ = ax.pie(
        group_data,
        colors=colors,
        startangle=90,
        pctdistance=0.85,
        wedgeprops=dict(edgecolor='w', linewidth=0.5),
    )
    
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)
    
    ax.set(aspect="equal")

# Overall pie chart for all age groups
ax = axs[1, 2]
wedges, _ = ax.pie(
    total_per_genre,
    colors=colors,
    startangle=90,
    pctdistance=0.85,
    wedgeprops=dict(edgecolor='w', linewidth=0.5),
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

ax.set(aspect="equal")

# Adjust layout
plt.tight_layout(rect=[0, 0, 0.9, 0.95])

# Show plot
plt.show()