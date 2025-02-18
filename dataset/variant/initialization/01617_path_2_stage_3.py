import matplotlib.pyplot as plt
import numpy as np
import itertools

years = np.arange(2010, 2021)
enrollments = {
    "Anthropology": [300, 320, 340, 360, 380, 400, 450, 470, 480, 490, 500],
    "Sociology": [280, 290, 310, 330, 350, 370, 390, 420, 450, 460, 470],
    "History": [260, 270, 280, 300, 320, 340, 360, 370, 380, 400, 410],
}

colors = ['#ff9999', '#66b3ff', '#99ff99']

fig, ax = plt.subplots(figsize=(16, 10))
x = np.arange(len(years))
bar_width = 0.2
hatches = itertools.cycle(['o', '-', '+'])   # Changed hatches to different patterns

# Iterate through each enrollment data with stylistic changes
for i, (discipline, counts) in enumerate(enrollments.items()):
    ax.bar(x + i * bar_width, counts, width=bar_width, color=colors[i],
           edgecolor='black', hatch=next(hatches))   # Changed edge color to black
    ax.plot(x + i * bar_width + bar_width / 2, counts, linestyle='-', color='green', marker='x')  # Line style to solid and marker changed to 'x'

ax.set_xticks(x + bar_width)
ax.yaxis.grid(True, linestyle='-', which='major', color='blue', alpha=0.3)  # Grid line style and color changed
ax.legend(enrollments.keys(), loc='upper left')  # Moved legend position
plt.tight_layout()
plt.show()