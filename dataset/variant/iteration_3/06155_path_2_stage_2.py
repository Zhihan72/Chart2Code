import numpy as np
import matplotlib.pyplot as plt

cities = ['Town Y', 'Metro X', 'Village Z']
years = ['Year One', 'Year Two', 'Year Three', 'Year Four', 'Year Five', 'Year Six', 'Year Seven', 'Year Eight']

data = {
    'Dance': [50, 60, 65, 70, 90, 100, 110, 120],
    'Meditation': [40, 50, 55, 60, 70, 85, 95, 100],
    'Jogging': [60, 70, 75, 80, 85, 95, 105, 115]
}

fig, ax = plt.subplots(figsize=(10, 6))

x = np.arange(len(years))
width = 0.25

colors = ['green', 'blue', 'orange']

for i, (program, counts) in enumerate(data.items()):
    ax.bar(x + i * width, counts, width, label=program, color=colors[i])

ax.set_xlabel('Annual Cycle')
ax.set_ylabel('Enrollees')
ax.set_title('Participation Trends in Health Activities Over Periods')
ax.set_xticks(x + width)
ax.set_xticklabels(years)

ax2 = ax.twinx()
retention_rate = [85, 82, 80, 78, 76, 75, 73, 71]
ax2.plot(years, retention_rate, color='red', marker='o', label='Staying Power (%)')
ax2.set_ylabel('Staying Power (%)', color='red')

fig.legend(loc='upper center', ncol=4, bbox_to_anchor=(0.5, 1.1))
fig.tight_layout(pad=3)

plt.show()