import numpy as np
import matplotlib.pyplot as plt

cities = ['City A', 'City B', 'City C']
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']

data = {
    'Aerobics': [50, 60, 65, 70, 90, 100, 110, 120],
    'Yoga': [40, 50, 55, 60, 70, 85, 95, 100],
    'Cardio': [60, 70, 75, 80, 85, 95, 105, 115]
}

fig, ax = plt.subplots(figsize=(10, 6))

x = np.arange(len(years))
width = 0.25

colors = ['green', 'blue', 'orange']  # Manually shuffled colors

for i, (program, counts) in enumerate(data.items()):
    ax.bar(x + i * width, counts, width, label=program, color=colors[i])

ax.set_xlabel('Years')
ax.set_ylabel('Participants')
ax.set_title('Impact of Fitness Programs Over Years in Cities')
ax.set_xticks(x + width)
ax.set_xticklabels(years)

ax2 = ax.twinx()
retention_rate = [85, 82, 80, 78, 76, 75, 73, 71]
ax2.plot(years, retention_rate, color='red', marker='o', label='Retention Rate')
ax2.set_ylabel('Retention Rate (%)', color='red')

fig.legend(loc='upper center', ncol=4, bbox_to_anchor=(0.5, 1.1))
fig.tight_layout(pad=3)

plt.show()