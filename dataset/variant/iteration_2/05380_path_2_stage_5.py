import matplotlib.pyplot as plt
import numpy as np

sunlight_hours = np.array([5, 7, 9, 11, 6, 8, 10, 12, 7, 9, 11, 13])
temperatures = np.array([15, 18, 20, 23, 16, 19, 21, 24, 17, 20, 22, 25])
efficiency_scores_A1 = np.array([75, 80, 85, 90, 77, 82, 87, 92, 79, 84, 89, 94])
efficiency_scores_A2 = np.array([70, 78, 84, 88, 72, 80, 86, 90, 74, 82, 88, 92])
efficiency_scores_A3 = np.array([65, 76, 82, 87, 67, 78, 84, 89, 69, 80, 86, 91])
efficiency_scores_A4 = np.array([68, 77, 83, 89, 70, 79, 85, 91, 72, 81, 87, 93])
efficiency_scores_A5 = np.array([60, 74, 81, 86, 63, 76, 83, 88, 66, 78, 85, 90])
efficiency_scores_A6 = np.array([72, 79, 85, 91, 75, 80, 87, 93, 77, 83, 88, 94])

efficiency_scores = {
    "A1": efficiency_scores_A1,
    "A2": efficiency_scores_A2,
    "A3": efficiency_scores_A3,
    "A4": efficiency_scores_A4,
    "A5": efficiency_scores_A5,
    "A6": efficiency_scores_A6
}

fig, axs = plt.subplots(2, 3, figsize=(18, 10), sharex=True, sharey=True)

# List of marker types and line styles
markers = ['o', 's', 'D', '^', 'v', '<', '>']
line_styles = ['-', '--', '-.', ':']

for i, (ax, (algo, scores)) in enumerate(zip(axs.flat, efficiency_scores.items())):
    marker = markers[i % len(markers)]
    line_style = line_styles[i % len(line_styles)]
    
    ax.scatter(sunlight_hours, temperatures, s=scores, c='green', alpha=0.5, edgecolors='black', marker=marker)
    
    ax.grid(i % 2 == 0, linestyle=line_style, linewidth=0.75, alpha=0.5)
    ax.set_facecolor('#f5f5f5' if i % 2 == 0 else '#e0e0e0')

plt.tight_layout()
plt.show()