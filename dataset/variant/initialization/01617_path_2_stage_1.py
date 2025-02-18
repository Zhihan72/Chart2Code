import matplotlib.pyplot as plt
import numpy as np
import itertools

years = np.arange(2010, 2021)
enrollments = {
    "Anthropology": [300, 320, 340, 360, 380, 400, 450, 470, 480, 490, 500],
    "Sociology": [280, 290, 310, 330, 350, 370, 390, 420, 450, 460, 470],
    "History": [260, 270, 280, 300, 320, 340, 360, 370, 380, 400, 410],
    "Philosophy": [240, 250, 260, 280, 300, 320, 330, 340, 350, 360, 370],
    "Literature": [220, 230, 240, 250, 270, 290, 310, 320, 330, 340, 350],
}

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

fig, ax = plt.subplots(figsize=(16, 10))
x = np.arange(len(years))
bar_width = 0.15
hatches = itertools.cycle(['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*'])

for i, (discipline, counts) in enumerate(enrollments.items()):
    ax.bar(x + i * bar_width, counts, width=bar_width, color=colors[i],
           edgecolor='grey', hatch=next(hatches))
    ax.plot(x + i * bar_width + bar_width / 2, counts, linestyle='--', color='black', marker='o')

ax.set_xticks(x + 2 * bar_width)
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)
plt.tight_layout()
plt.show()