import matplotlib.pyplot as plt
import numpy as np

# Data Setup
years = np.array(['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])
languages = ['Py', 'JS', 'Ruby', 'C++']
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

# Setup the figure
fig, ax = plt.subplots(figsize=(12, 7))
bar_width = 0.3  

x = np.arange(len(years))
for i, language in enumerate(languages):
    ax.bar(x + i * bar_width, participants[:, i], width=bar_width, label=language, edgecolor='black', linestyle=':', hatch='/')

for i, year_data in enumerate(participants):
    for j, value in enumerate(year_data):
        ax.text(i + j * bar_width, value + 10, str(value), ha='center', va='bottom', fontsize=8, color='blue')

# Set labels, title, and legend
ax.set_xlabel('Yr', fontsize=11, labelpad=8)
ax.set_ylabel('# Participants', fontsize=11, labelpad=8)
ax.set_title('Coding Workshop Attendance\n(2015-22)', fontsize=15, fontweight='bold', pad=18)
ax.set_xticks(x + bar_width * 1.5)
ax.set_xticklabels(years, rotation=25)
ax.legend(title='Lang:', loc='center left', bbox_to_anchor=(1, 0.5))

ax.yaxis.grid(True, linewidth=0.5, alpha=0.5)
ax.set_axisbelow(True)

plt.tight_layout()
plt.show()