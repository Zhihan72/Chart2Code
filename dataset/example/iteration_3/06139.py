import matplotlib.pyplot as plt
import numpy as np

# Backstory: The chart shows the average amount of time spent on various social media platforms by age group, over a month period.

# Define age groups and social media platforms
age_groups = ["13-17", "18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
platforms = ["Facebook", "Instagram", "Snapchat", "Twitter", "TikTok", "Youtube", "LinkedIn"]

# Average monthly usage in hours for each platform by age group
usage_data = np.array([
    [15, 20, 10, 5, 25, 30, 2],   # 13-17
    [20, 25, 15, 10, 30, 35, 5],  # 18-24
    [18, 20, 12, 8, 20, 28, 10],  # 25-34
    [15, 18, 8, 7, 10, 25, 12],   # 35-44
    [10, 12, 5, 6, 5, 18, 15],    # 45-54
    [5, 8, 2, 5, 2, 12, 10],      # 55-64
    [2, 3, 1, 4, 1, 8, 5]         # 65+
])

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.1  # Width of each bar

positions = np.arange(len(age_groups))
for i, platform in enumerate(platforms):
    bars = ax.bar(positions + i * bar_width, usage_data[:, i], bar_width, label=platform)

    # Adding data labels above each bar
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.5, f'{height}', ha='center', va='bottom', fontsize=9)

# Customizing the chart
ax.set_title("Average Monthly Time Spent on Social Media Platforms by Age Group", fontsize=18, fontweight='bold')
ax.set_xlabel("Age Group", fontsize=14)
ax.set_ylabel("Average Monthly Hours", fontsize=14)
ax.set_xticks(positions + (len(platforms) - 1) * bar_width / 2)
ax.set_xticklabels(age_groups, fontsize=12, rotation=45, ha='right')
ax.legend(title="Platforms")

# Adding a grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()