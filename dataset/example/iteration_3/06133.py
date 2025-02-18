import matplotlib.pyplot as plt
import numpy as np

# Backstory: We are tracking the annual change in total revenue and employee satisfaction scores across different stores of a retail chain over a five-year period.
# Title: "Retail Chain Performance Analysis: Revenue vs Employee Satisfaction (2018-2022)"

# Data: Revenue in millions and Employee Satisfaction Scores (out of 10)
years = np.array([2018, 2019, 2020, 2021, 2022])
stores = ["Store A", "Store B", "Store C", "Store D", "Store E"]

# Revenue data (in millions)
revenue = np.array([
    [10, 12, 11, 15, 14],  # Store A
    [8, 9, 10, 12, 13],    # Store B
    [15, 16, 14, 18, 20],  # Store C
    [13, 14, 15, 17, 16],  # Store D
    [9, 10, 12, 14, 13],   # Store E
])

# Employee satisfaction scores (out of 10)
satisfaction_scores = np.array([
    [7, 7.5, 8, 8.5, 9],   # Store A
    [6, 6.5, 7, 7.5, 7.8], # Store B
    [7.5, 8, 8.5, 8.8, 9.1], # Store C
    [6.8, 7, 7.5, 8, 8.5], # Store D
    [7, 7.2, 7.5, 7.8, 8], # Store E
])

# Setup the figure and axis for the combined chart
fig, ax1 = plt.subplots(figsize=(14, 8))

# Define color palette for the bars
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF']

# Plotting revenue data as bars in the chart
bar_width = 0.15
for idx, store in enumerate(stores):
    ax1.bar(years + idx*bar_width, revenue[idx], width=bar_width, color=colors[idx], alpha=0.7, label=f'{store} Revenue')

# Adding the title and labels
ax1.set_title('Retail Chain Performance Analysis:\nRevenue vs Employee Satisfaction (2018-2022)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Revenue (in millions)', fontsize=12)
ax1.set_xticks(years + bar_width*(len(stores)-1)/2)
ax1.set_xticklabels(years)

# Adding a second y-axis for employee satisfaction scores
ax2 = ax1.twinx()
ax2.set_ylabel('Employee Satisfaction (out of 10)', fontsize=12)

# Plotting satisfaction scores as lines
for idx, store in enumerate(stores):
    ax2.plot(years, satisfaction_scores[idx], marker='o', linestyle='-', linewidth=2, color=colors[idx], label=f"{store} Satisfaction")
    for x, y in zip(years, satisfaction_scores[idx]):
        ax2.annotate(f'{y}', xy=(x, y), xytext=(0, 5), textcoords='offset points', fontsize=9, color=colors[idx], ha='center')

# Combine legends for both bar and line plots
bars, bar_labels = ax1.get_legend_handles_labels()
lines, line_labels = ax2.get_legend_handles_labels()
ax1.legend(bars + lines, bar_labels + line_labels, title='Stores', loc='upper left', fontsize=10, frameon=True)

# Adding a grid for better readability
ax1.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Optimize layout to ensure nothing is clipped
plt.tight_layout()

# Display the plot
plt.show()