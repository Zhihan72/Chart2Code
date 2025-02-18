import matplotlib.pyplot as plt
import numpy as np

# Define the scenarios and the categories
scenarios = ['Business', 'Education', 'Entertainment', 'Health', 'Research']
categories = ['Excel', 'Python', 'Graphics', 'Statistics']

# Data for the usage of each tool in different scenarios
usage_data = np.array([
    [40, 30, 20, 50],   # Business
    [25, 50, 15, 40],   # Education
    [10, 20, 80, 25],   # Entertainment
    [30, 40, 10, 70],   # Health
    [20, 60, 30, 90]    # Research
])

# Create a plot with subplots for diversity of visual representation
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

# Parameters for the bar chart
bar_width = 0.2
positions = np.arange(len(scenarios))
colors = ['#4daf4a', '#377eb8', '#ff7f00', '#984ea3']

# Create the bar chart on the first axis
for i, (category, color) in enumerate(zip(categories, colors)):
    bars = ax1.bar(positions + i * bar_width, usage_data[:, i], bar_width, label=category, color=color, edgecolor='gray', alpha=0.85)

    # Annotate each bar with the usage value
    for bar in bars:
        height = bar.get_height()
        ax1.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, color='black')

# Styling for the first plot
ax1.set_xlabel('Scenarios', fontsize=12)
ax1.set_ylabel('Usage of Tools (%)', fontsize=12)
ax1.set_title('Tool Usage Across Different Scenarios', fontsize=14, fontweight='bold', pad=15)
ax1.set_xticks(positions + 1.5 * bar_width)
ax1.set_xticklabels(scenarios, fontsize=11)
ax1.legend(title="Tools", fontsize=10, loc='upper right')
ax1.yaxis.grid(True, linestyle='--', alpha=0.6)

# Prepare secondary data for the second subplot
usage_growth = np.array([
    [5, 3, 2, 7],   # Business
    [2, 4, 1, 6],   # Education
    [1, 2, 9, 3],   # Entertainment
    [4, 5, 1, 8],   # Health
    [3, 6, 2, 10]   # Research
])

# Create a cumulative bar chart for tool usage growth
cumulative_data = np.cumsum(usage_growth, axis=0)
for i, (category, color) in enumerate(zip(categories, colors)):
    ax2.barh(positions, cumulative_data[:, i], bar_width, label=category, color=color, edgecolor='gray', alpha=0.85)

# Styling for the second plot
ax2.set_xlabel('Cumulative Growth (%)', fontsize=12)
ax2.set_ylabel('Scenarios', fontsize=12)
ax2.set_title('Tool Usage Growth Across Different Scenarios', fontsize=14, fontweight='bold', pad=15)
ax2.set_yticks(positions)
ax2.set_yticklabels(scenarios, fontsize=11)
ax2.legend(title="Tools", fontsize=10, loc='lower right')
ax2.xaxis.grid(True, linestyle='--', alpha=0.6)
ax2.invert_yaxis()

# Automatically adjust the layout
plt.tight_layout()

# Show the plot
plt.show()