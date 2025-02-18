import matplotlib.pyplot as plt
import numpy as np

preferences = [
    [30, 25, 20, 15, 10],
    [10, 10, 40, 30, 10],
    [15, 20, 30, 20, 15],
    [20, 30, 20, 10, 20],
    [25, 15, 25, 20, 15],
    [20, 25, 25, 15, 15],
]
colors = ['#FFD700', '#32CD32', '#FF6347', '#87CEFA', '#D2B48C']

fig, axes = plt.subplots(1, 6, figsize=(24, 6), subplot_kw=dict(aspect="equal"))

for i, ax in enumerate(axes.flat):
    wedges, texts, autotexts = ax.pie(
        preferences[i], autopct='%1.1f%%',
        startangle=140, colors=colors, pctdistance=0.85,
        wedgeprops=dict(width=0.3), shadow=True
    )

    for text in texts:
        text.set_fontsize(0)  # Make these text elements invisible

    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(0)  # Make these auto-text elements invisible

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.show()