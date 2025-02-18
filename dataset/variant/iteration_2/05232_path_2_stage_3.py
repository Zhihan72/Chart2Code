import matplotlib.pyplot as plt
import numpy as np

engineering_hours = [19, 15, 24, 21, 17, 18, 20, 16, 23, 22, 21, 24, 18, 19, 20]  # Altered
arts_hours = [12, 7, 10, 11, 14, 9, 13, 8, 10, 12, 9, 15, 8, 10, 11]  # Altered
science_hours = [22, 21, 23, 25, 18, 19, 24, 20, 22, 21, 24, 19, 23, 22, 20]  # Altered
business_hours = [8, 7, 8, 5, 9, 7, 6, 10, 6, 8, 10, 7, 9, 8, 6]  # Altered
law_hours = [30, 27, 29, 28, 25, 28, 26, 29, 32, 25, 28, 27, 30, 26, 29]  # Altered

data = [engineering_hours, arts_hours, science_hours, business_hours, law_hours]

fig, ax = plt.subplots(figsize=(14, 8))

box = ax.boxplot(data, vert=False, patch_artist=True, notch=False, whis=1.5,
                 boxprops=dict(facecolor="lightgreen", color="blue", linestyle='--'),
                 whiskerprops=dict(color="magenta", linestyle='-.'),
                 capprops=dict(color="cyan"),
                 flierprops=dict(marker="s", color="red", alpha=0.7),
                 medianprops=dict(color="purple"))

colors = ['lightblue', 'lightpink', 'lightgray', 'lightyellow', 'lightcoral']
for patch, color in zip(box['boxes'], colors[::-1]):
    patch.set_facecolor(color)

ax.set_yticklabels([])
ax.set_xticklabels([])

ax.grid(True, linestyle='-', linewidth=1, alpha=0.3)

ax_hist = ax.twiny()
ax_hist.set_xticks([])
for i, data_series in enumerate(data):
    hist_data = np.histogram(data_series, bins=np.arange(min(data_series) - 1, max(data_series) + 2))
    ax_hist.barh([i + 1] * len(hist_data[0]), hist_data[0], left=hist_data[1][:-1], color=colors[i],
                 alpha=0.5, height=0.3)

plt.tight_layout()

plt.show()