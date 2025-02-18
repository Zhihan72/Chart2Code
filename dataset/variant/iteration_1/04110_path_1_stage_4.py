import matplotlib.pyplot as plt
import numpy as np

years = ['2017', '2018', '2019', '2020']
categories = ['Adventure', 'Culture', 'Food', 'Nature']
data = np.array([
    [15, 18, 22, 26],
    [20, 22, 24, 30],
    [30, 32, 34, 38],
    [25, 28, 30, 35],
])

fig, ax = plt.subplots(figsize=(12, 8))

bar_height = 0.15
y = np.arange(len(years))
color = 'blue'

for i in range(len(categories)):
    ax.barh(y + i * bar_height, data[i], height=bar_height, color=color)

for i in range(len(years)):
    for j in range(len(categories)):
        plt.text(data[j][i] + 0.5, i + j * bar_height, str(data[j][i]), va='center', ha='left', fontsize=8, fontweight='bold')

ax.set_ylabel('Year', fontsize=14, fontweight='bold')
ax.set_xlabel('Number of Travelers (in thousands)', fontsize=14, fontweight='bold')
ax.set_title('Global Travel Interests (2017-2020)\nDistribution of Travelers by Activity', fontsize=16, fontweight='bold')
ax.set_yticks(y + 1.5 * bar_height)
ax.set_yticklabels(years)

plt.tight_layout()
plt.show()