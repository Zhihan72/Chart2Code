import numpy as np
import matplotlib.pyplot as plt

# Define space agencies, years, and their success rates
agencies = ['NASA', 'ESA', 'Roscosmos']
years = ['2010', '2015', '2020']
success_rates = np.array([
    [85, 90, 95],
    [75, 85, 88],
    [80, 83, 89]
])

# Setup the figure
fig, ax = plt.subplots(figsize=(12, 8))

# Set colors for each year
colors = ['navy', 'royalblue', 'deepskyblue']

# Plot horizontal bar charts for each agency
bar_width = 0.2
for i, year in enumerate(years):
    ax.barh(np.arange(len(agencies)) + i * bar_width, success_rates[:, i], height=bar_width, 
            color=colors[i], alpha=0.7, label=f"{year}")

# Set labels and ticks
ax.set_yticks(np.arange(len(agencies)) + bar_width)
ax.set_yticklabels(agencies, fontsize=10)
ax.set_xlim(0, 100)
ax.set_xlabel('Success Rate (%)', fontsize=10)
ax.set_title("Space Exploration Success Rates (2010-2020)\nMission Outcomes by Leading Space Agencies",
             fontsize=14, weight='bold')

# Add legend
ax.legend(loc='upper right', title='Years', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()