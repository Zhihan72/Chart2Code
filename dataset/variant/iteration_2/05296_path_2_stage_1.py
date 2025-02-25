import matplotlib.pyplot as plt
import numpy as np

# Age groups
age_groups = ['Children (5-12)', 'Teens (13-19)', 'Adults (20-39)', 'Middle-aged (40-59)', 'Seniors (60+)']

# Days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Average daily step counts for each age group over a week
step_counts = np.array([
    [12000, 15000, 13000, 14000, 14500, 20000, 18000],  # Children
    [10000, 11000, 12000, 11500, 11000, 13500, 12500],  # Teens
    [8000, 8500, 9000, 9500, 9000, 10000, 9500],        # Adults
    [7500, 7000, 7200, 7100, 7300, 8000, 7800],        # Middle-aged
    [5000, 5200, 5100, 4900, 4800, 6000, 5900]         # Seniors
])

# Setting up the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Determine the width of each bar
bar_width = 0.12
index = np.arange(len(days))

# Create the bars for each age group
bars = []
for i, group in enumerate(age_groups):
    bar = ax.bar(index + i * bar_width, step_counts[i], bar_width, label=group)
    bars.append(bar)

# Add title with different font size and style
plt.title("Step Counts Analysis", fontsize=18, fontweight='light', pad=25)

# Altering axis labels and grid style
plt.xlabel("Days", fontsize=13, color='darkblue')
plt.ylabel("Avg Steps", fontsize=13, color='darkblue')

# Modify x-ticks to center labels correctly
plt.xticks(index + bar_width * (len(age_groups) / 2), days)

# Add grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Modify legend styling
plt.legend(title="Age Brackets", fontsize=11, loc='upper left')

# Remove borders to emphasize the chart area
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Annotate each bar with its value
for bar_group in bars:
    for bar in bar_group:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}',
                ha='center', va='bottom', fontsize=10)

# Tight layout
plt.tight_layout()

# Display the plot
plt.show()
