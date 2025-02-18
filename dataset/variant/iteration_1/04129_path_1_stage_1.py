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
fig, ax = plt.subplots(figsize=(12, 7))

# Bar width
bar_width = 0.3  

# X positions for groups
x = np.arange(len(years))

# Plot each language's data as separate bars stacked horizontally for each year
for i, language in enumerate(languages):
    ax.bar(x + i * bar_width, participants[:, i], width=bar_width, label=language, edgecolor='black', linestyle=':', hatch='/')

# Add data annotations
for i, year_data in enumerate(participants):
    for j, value in enumerate(year_data):
        ax.text(i + j * bar_width, value + 10, str(value), ha='center', va='bottom', fontsize=8, color='blue')

# Set labels, title, and legend
ax.set_xlabel('Year', fontsize=11, labelpad=8)
ax.set_ylabel('Number of Participants', fontsize=11, labelpad=8)
ax.set_title('Public Coding Workshop Participation\nIn Techville (2015-2022)', fontsize=15, fontweight='bold', pad=18)
ax.set_xticks(x + bar_width * 1.5)
ax.set_xticklabels(years, rotation=25)
ax.legend(title='Languages', loc='center left', bbox_to_anchor=(1, 0.5))

# Add grid lines with style alterations
ax.yaxis.grid(True, linewidth=0.5, alpha=0.5)
ax.set_axisbelow(True)

# Adjust layout for clarity
plt.tight_layout()

# Display the plot
plt.show()