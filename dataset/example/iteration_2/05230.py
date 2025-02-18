import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analyzing the performance of different programming languages in terms of popularity and projected job demand growth
# Data for popularity (percentage)
languages = ['Python', 'JavaScript', 'Java', 'C++', 'Ruby']
popularity = [30, 25, 20, 15, 10]  # Percentage values

# Data for projected job demand growth (in thousands)
years = np.array([2023, 2024, 2025, 2026, 2027])
projected_jobs_growth = {
    'Python': [150, 155, 160, 165, 170],
    'JavaScript': [130, 135, 140, 145, 150],
    'Java': [120, 122, 124, 126, 128],
    'C++': [100, 102, 104, 106, 108],
    'Ruby': [80, 82, 84, 86, 88]
}

# Colors and line styles
colors = ['#3776AB', '#F0DB4F', '#B07219', '#00599C', '#701516']
line_styles = ['-', '--', '-.', ':', '-']

# Create the figure and axis objects
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the bar chart for popularity
bars = ax1.barh(languages, popularity, color=colors, edgecolor='grey', height=0.6)

# Adding percentage labels to each bar
for bar, percentage in zip(bars, popularity):
    ax1.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
            f'{percentage}%', va='center', ha='left', fontsize=10, fontweight='bold', color='black')

# Add a secondary y-axis for the line plot
ax2 = ax1.twinx()

# Plot the line charts for projected job demand growth
for idx, (language, growth) in enumerate(projected_jobs_growth.items()):
    ax2.plot(growth, years, label=f'Projected {language}', color=colors[idx], linestyle=line_styles[idx], marker='o')

# Title and labels
ax1.set_title("Programming Languages Popularity (2023) and Projected Job Demand Growth", fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel("Popularity (%)", fontsize=12)
ax1.set_ylabel("Programming Languages", fontsize=12)
ax2.set_ylabel("Year", fontsize=12)
ax2.set_yticks(years)

# Set axis limits to improve visualization
ax1.set_xlim(0, 35)
ax2.set_ylim(2022, 2028)

# Add gridlines to the x-axis of the bar chart
ax1.xaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust y-ticks for the programming languages
ax1.set_yticks(np.arange(len(languages)))
ax1.set_yticklabels(languages, fontsize=12, fontweight='bold')

# Add legend for the line plot
fig.legend(loc='upper right', bbox_to_anchor=(0.85, 0.85), fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()