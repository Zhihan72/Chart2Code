import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The fictional city of "Techville" has introduced various public coding workshops over the years.
# We have data showing the number of participants in these workshops from 2015 to 2022.
# The goal is to visualize the trend over the years and breakdown between different coding languages.

# Data Setup:
years = np.array(['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])
languages = ['Python', 'JavaScript', 'Ruby', 'C++']
participants = np.array([
    [200, 150, 50, 30],   # 2015
    [220, 160, 55, 35],   # 2016
    [250, 170, 60, 40],   # 2017
    [280, 180, 65, 45],   # 2018
    [320, 200, 70, 50],   # 2019
    [400, 220, 80, 60],   # 2020
    [450, 240, 90, 70],   # 2021
    [500, 260, 100, 80],  # 2022
])

# Setup the figure and subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Bar width
bar_width = 0.2

# X positions for groups
x = np.arange(len(years))

# Plot each language's data as separate bars stacked horizontally for each year
for i, language in enumerate(languages):
    ax.bar(x + i * bar_width, participants[:, i], width=bar_width, label=language)

# Add data annotations
for i, year_data in enumerate(participants):
    for j, value in enumerate(year_data):
        ax.text(i + j * bar_width, value + 10, str(value), ha='center', va='bottom', fontsize=9, color='black')

# Set labels, title, and legend
ax.set_xlabel('Year', fontsize=12, labelpad=10)
ax.set_ylabel('Number of Participants', fontsize=12, labelpad=10)
ax.set_title('Participation in Public Coding Workshops\nTechville (2015-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x + bar_width * 1.5)
ax.set_xticklabels(years)
ax.legend(title='Programming Languages', loc='upper left', bbox_to_anchor=(1, 1))

# Rotate x-axis labels for better readability
plt.xticks(rotation=20)

# Add grid lines
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Automatically adjust layout for clarity
plt.tight_layout()

# Display the plot
plt.show()