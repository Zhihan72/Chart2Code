import matplotlib.pyplot as plt
import numpy as np

# Data Setup
years = np.array(['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])
languages = ['Python', 'JavaScript', 'Ruby', 'C++']
participants = np.array([
    [200, 150, 50, 30],
    [220, 160, 55, 35],
    [250, 170, 60, 40],
    [280, 180, 65, 45],
    [320, 200, 70, 50],
    [400, 220, 80, 60],
    [450, 240, 90, 70],
    [500, 260, 100, 80],
])

# Setup the figure and subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Bar width
bar_width = 0.15

# X positions for groups
x = np.arange(len(years))

# Plot each language's data with different patterns and marker styles
patterns = ['/', '\\', '|', '-']
marker_styles = ['o', 's', 'D', '*']

for i, language in enumerate(languages):
    ax.bar(x + i * bar_width, participants[:, i], width=bar_width, 
           label=language, hatch=patterns[i % len(patterns)], edgecolor='black', linestyle='dotted')

# Add data annotations with an altered font style
for i, year_data in enumerate(participants):
    for j, value in enumerate(year_data):
        ax.text(i + j * bar_width, value + 5, str(value), ha='center', va='bottom', fontsize=9, color='darkblue', fontstyle='italic')

# Set labels, title, and legend
ax.set_xlabel('Year', fontsize=12, labelpad=10, fontweight='bold', color='purple')
ax.set_ylabel('Participants', fontsize=12, labelpad=10, fontweight='bold', color='purple')
ax.set_title('Public Coding Workshops in Techville (2015-2022)', fontsize=16, fontweight='bold', color='darkred', pad=20)

# Set custom ticks and rotate them for better readability
ax.set_xticks(x + bar_width * 1.5)
ax.set_xticklabels(years, rotation=45, fontstyle='italic')

# Modify legend's position and border
ax.legend(title='Languages', loc='upper right', bbox_to_anchor=(1.15, 1), frameon=False)

# Add custom grid lines
ax.yaxis.grid(True, linestyle='-', linewidth=0.5, color='gray', alpha=0.9)
ax.set_axisbelow(True)

# Suppress the top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Automatically adjust layout for clarity
plt.tight_layout()

# Display the plot
plt.show()