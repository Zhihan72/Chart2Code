import matplotlib.pyplot as plt
import numpy as np

age_groups = ['18-25', '26-35', '36-45', '46-55', '56-65', '66+']
ai_assistants = [120, 150, 130, 100, 60, 30]
smart_homes = [80, 140, 120, 110, 70, 40]

fig, ax = plt.subplots(figsize=(12, 8))

height = 0.3

bar1 = np.arange(len(age_groups))
bar2 = [x + height for x in bar1]

ax.barh(bar1, ai_assistants, height, color='lightgreen', edgecolor='gray', linestyle='-')
ax.barh(bar2, smart_homes, height, color='salmon', edgecolor='gray', linestyle='-.')

ax.set_yticks([])
ax.set_xticks([])

def add_value_labels(bars, values):
    for bar, value in zip(bars, values):
        ax.text(value + 3, bar, str(value), va='center', color='blue', fontsize=10)

add_value_labels(ai_assistants, bar1)
add_value_labels(smart_homes, bar2)

ax.xaxis.grid(True, linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()