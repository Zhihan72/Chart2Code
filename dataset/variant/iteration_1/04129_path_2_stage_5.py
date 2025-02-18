import matplotlib.pyplot as plt
import numpy as np

years = np.array(['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])
languages = ['Python', 'JavaScript', 'C++']
participants = np.array([
    [200, 150, 30],
    [220, 160, 35],
    [250, 170, 40],
    [280, 180, 45],
    [320, 200, 50],
    [400, 220, 60],
    [450, 240, 70],
    [500, 260, 80],
])

mean_participants = np.mean(participants)
participants_delta = participants - mean_participants

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.35
x = np.arange(len(years))

# Define new colors for the bars
colors = ['skyblue', 'lightgreen', 'salmon']

for i, language in enumerate(languages):
    ax.bar(x, participants_delta[:, i], width=bar_width, label=language, alpha=0.7, edgecolor='black', 
           color=colors[i], align='center', bottom=participants_delta[:, i - 1] if i != 0 else 0)

ax.set_xticks(x)
ax.set_xticklabels(years, rotation=45)
ax.axhline(0, color='black', linewidth=0.8)

ax.legend()
plt.tight_layout()
plt.show()