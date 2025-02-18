import matplotlib.pyplot as plt
import numpy as np

disciplines = ['Sciences', 'Engineering', 'Humanities', 'Social Sciences']
funding_data = np.array([
    [20, 60, 10, 30],
    [30, 15, 70, 20],
    [30, 20, 10, 40],
    [15, 20, 40, 25],
])

bar_width = 0.2
colors = ['#ff7f0e', '#2ca02c', '#d62728', '#1f77b4']

fig, ax = plt.subplots(figsize=(10, 7))
index = np.arange(len(disciplines))

for i in range(len(funding_data[0])):
    ax.bar(index + i * bar_width, funding_data[:, i], width=bar_width, color=colors[i], alpha=0.85)

plt.tight_layout()
plt.show()