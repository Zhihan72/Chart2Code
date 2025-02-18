import matplotlib.pyplot as plt
import numpy as np

years = np.array(['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])

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
# Removing Py+JS data
participants_pro = participants[:, 2]
# Participants for the removed group should not contribute to values anymore
#participants_anti = -participants[:, [0, 1]].sum(axis=1)

fig, ax = plt.subplots(figsize=(12, 7))
half_bar_width = 0.35  

x = np.arange(len(years))

ax.bar(x, participants_pro, width=half_bar_width, label='Ruby+C++', edgecolor='black', linestyle=':', hatch='\\')

for i, pro in enumerate(participants_pro):
    ax.text(i, pro + 10, f"{pro}", ha='center', va='bottom', fontsize=8, color='green')

ax.axhline(0, color='black', linewidth=0.8)

ax.set_xlabel('Year', fontsize=11, labelpad=8)
ax.set_ylabel('Participation', fontsize=11, labelpad=8)
ax.set_title('Coding Workshop Attendance (Ruby+C++)\n(2015-22)', fontsize=15, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(years, rotation=25)
ax.legend(title='Language Group', loc='upper left')

ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)
ax.set_axisbelow(True)

plt.tight_layout()
plt.show()