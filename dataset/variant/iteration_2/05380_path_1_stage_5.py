import matplotlib.pyplot as plt
import numpy as np

sunlight_hours = np.array([5, 7, 9, 11, 6, 8, 10, 12, 7, 9, 11, 13])
temperatures = np.array([15, 18, 20, 23, 16, 19, 21, 24, 17, 20, 22, 25])
efficiency_scores_A1 = np.array([75, 80, 85, 90, 77, 82, 87, 92, 79, 84, 89, 94])
efficiency_scores_A2 = np.array([70, 78, 84, 88, 72, 80, 86, 90, 74, 82, 88, 92])

efficiency_scores = {
    "A1": efficiency_scores_A1,
    "A2": efficiency_scores_A2
}

colors = {
    "A1": 'orange',
    "A2": 'green'
}

fig, axs = plt.subplots(2, 2, figsize=(14, 10), sharex=True, sharey=True)

axs = axs.flat[:2]  # Use only two of the axes for the remaining subplots

for ax, (algo, scores) in zip(axs, efficiency_scores.items()):
    ax.scatter(sunlight_hours, temperatures, s=scores, c=colors[algo], alpha=0.6, edgecolors='w', linewidth=0.8)
    ax.set_facecolor('#f9f9f9')

plt.tight_layout()
plt.show()