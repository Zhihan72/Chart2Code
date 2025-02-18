import numpy as np
import matplotlib.pyplot as plt

cities = ['City A', 'City B', 'City C']
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']

data = {
    'Aerobics': [90, 70, 120, 130, 50, 65, 100, 110],
    'Yoga': [80, 60, 100, 110, 40, 55, 85, 95],
    'Cardio': [110, 80, 130, 135, 60, 75, 95, 105]
}

fig, ax = plt.subplots(figsize=(10, 6))

x = np.arange(len(years))
width = 0.25

colors = ['cyan', 'yellow', 'magenta']

line_styles = ['--', '-.', '-']
markers = ['D', 's', 'o']

for i, (program, counts) in enumerate(data.items()):
    ax.bar(x + i * width, counts, width, color=colors[i], label=program)

ax.set_xlabel('Years')
ax.set_ylabel('Participants')
ax.set_title('Impact of Fitness Programs Over Years in Cities')
ax.set_xticks(x + width)
ax.set_xticklabels(years)

ax2 = ax.twinx()

retention_rate = [73, 71, 85, 82, 75, 78, 76, 80]
ax2.plot(years, retention_rate, color='darkblue', linestyle='-.', marker='D', label='Retention Rate')
ax2.set_ylabel('Retention Rate (%)', color='darkblue')

fig.legend(loc='upper right', ncol=1, bbox_to_anchor=(0.85, 0.95))
ax.grid(True, which='major', linestyle='-')

fig.tight_layout(pad=3)

plt.show()