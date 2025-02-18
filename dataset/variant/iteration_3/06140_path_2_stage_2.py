import matplotlib.pyplot as plt

# Create some fictional productivity data over the days of the week
productivity_data = {
    'Monday': [4, 5, 6, 5, 7, 8, 5, 6, 4, 6],
    'Tuesday': [6, 7, 5, 6, 8, 9, 7, 6, 8, 9],
    'Wednesday': [7, 8, 6, 7, 9, 9, 7, 8, 6, 7],
    'Thursday': [5, 6, 5, 6, 7, 7, 8, 6, 5, 6],
    'Friday': [4, 5, 4, 5, 6, 6, 5, 4, 5, 6],
    'Saturday': [2, 3, 2, 4, 3, 4, 3, 2, 3, 4],
    'Sunday': [1, 2, 1, 3, 2, 2, 3, 1, 2, 1]
}

# Prepare data for the box plot
box_plot_data = list(productivity_data.values())

fig, ax = plt.subplots(figsize=(14, 10))

# Create the horizontal box plot
ax.boxplot(box_plot_data, vert=False, labels=productivity_data.keys(),
           patch_artist=False, notch=True, medianprops=dict(color='black'))

# Set the axis titles
ax.set_xlabel('Productivity Score (1-10)', fontsize=14)
ax.set_ylabel('Day of the Week', fontsize=14)

# Automatically adjust layout
plt.tight_layout()

# Display plot
plt.show()