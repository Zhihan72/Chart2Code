import matplotlib.pyplot as plt
import numpy as np

# Age groups (Including additional 'Young Adults (20-29)' for more granularity)
age_groups = [
    'Children (5-12)', 
    'Teens (13-19)', 
    'Young Adults (20-29)', 
    'Adults (30-39)', 
    'Middle-aged (40-59)', 
    'Seniors (60+)'
]

# Days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Average daily step counts for each age group over a week
step_counts = np.array([
    [12000, 15000, 13000, 14000, 14500, 20000, 18000],  # Children
    [10000, 11000, 12000, 11500, 11000, 13500, 12500],  # Teens
    [9500, 10000, 10500, 11000, 10700, 12000, 11700],   # Young Adults
    [8000, 8500, 9000, 9500, 9000, 10000, 9500],        # Adults
    [7500, 7000, 7200, 7100, 7300, 8000, 7800],         # Middle-aged
    [5000, 5200, 5100, 4900, 4800, 6000, 5900]          # Seniors
])

# Setting up the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.13
index = np.arange(len(days))

# Create the bars for each age group
bars = []
for i, group in enumerate(age_groups):
    bars.append(
        ax.bar(index + i * bar_width, step_counts[i], bar_width, label=group)
    )

# Add title, labels, and legend
plt.title("Comparative Analysis of Average Daily Step Counts Over a Week\nAmong Different Age Groups", 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Days of the Week", fontsize=14)
plt.ylabel("Average Step Count", fontsize=14)
plt.xticks(index + bar_width * 2.5, days)  # Adjusting position for added group
plt.legend(title="Age Groups", fontsize=12)

# Annotate each bar with its value
for bar_group in bars:
    for bar in bar_group:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', 
                ha='center', va='bottom', fontsize=10)

# Tight layout for preventing overlap
plt.tight_layout()

# Display the plot
plt.show()