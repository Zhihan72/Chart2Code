import matplotlib.pyplot as plt
import numpy as np

# Backstory: Comparing Productivity Levels Throughout the Week
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

# Plot setup
fig, ax = plt.subplots(figsize=(14, 10))

# Create the boxplot
boxprops = dict(linestyle='-', linewidth=2, color='darkblue', facecolor='skyblue')
medianprops = dict(linestyle='-', linewidth=2, color='blue')
whiskerprops = dict(linestyle='--', linewidth=1.5, color='darkblue')
capprops = dict(linestyle='-', linewidth=2, color='darkblue')

ax.boxplot(box_plot_data, labels=productivity_data.keys(), patch_artist=True,
           boxprops=boxprops, medianprops=medianprops,
           whiskerprops=whiskerprops, capprops=capprops,
           flierprops=dict(marker='o', color='red', markersize=5, alpha=0.5),
           notch=True)

# Adding the overall title and axis titles
ax.set_title("Weekly Productivity Levels: Analyzing Daily Trends in Work Output", fontsize=18, fontweight='bold', loc='center', pad=20)
ax.set_ylabel('Productivity Score (1-10)', fontsize=14)
ax.set_xlabel('Day of the Week', fontsize=14)

# Adding annotations
ax.annotate('Highest Productivity', xy=(3, 9), xytext=(2.5, 9.5), fontsize=12, color='green',
             arrowprops=dict(facecolor='green', shrink=0.05))
ax.annotate('Weekend Effect', xy=(7, 2.5), xytext=(6.5, 3.5), fontsize=12, color='orange',
             arrowprops=dict(facecolor='orange', shrink=0.05))

# Adding grid lines for readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Enhance readability of x-axis labels by rotating them
plt.xticks(rotation=45)

# Automatically adjust the layout for better appearance
plt.tight_layout()

# Display the plot
plt.show()