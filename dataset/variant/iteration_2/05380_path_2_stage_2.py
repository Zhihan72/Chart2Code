import matplotlib.pyplot as plt
import numpy as np

sunlight_hours = np.array([5, 7, 9, 11, 6, 8, 10, 12, 7, 9, 11, 13])
temperatures = np.array([15, 18, 20, 23, 16, 19, 21, 24, 17, 20, 22, 25])
efficiency_scores_A1 = np.array([75, 80, 85, 90, 77, 82, 87, 92, 79, 84, 89, 94])
efficiency_scores_A2 = np.array([70, 78, 84, 88, 72, 80, 86, 90, 74, 82, 88, 92])
efficiency_scores_A3 = np.array([65, 76, 82, 87, 67, 78, 84, 89, 69, 80, 86, 91])
efficiency_scores_A4 = np.array([68, 77, 83, 89, 70, 79, 85, 91, 72, 81, 87, 93])

efficiency_scores = {
    "A1": efficiency_scores_A1,
    "A4": efficiency_scores_A4,
    "A3": efficiency_scores_A3,
    "A2": efficiency_scores_A2
}

fig, axs = plt.subplots(2, 2, figsize=(14, 10), sharex=True, sharey=True)

titles = ["Algorithm A4 Efficiency", "Algorithm A3 Efficiency", "Algorithm A2 Efficiency", "Algorithm A1 Efficiency"]

for i, (ax, (algo, scores)) in enumerate(zip(axs.flat, efficiency_scores.items())):
    scatter = ax.scatter(sunlight_hours, temperatures, s=scores, c='blue', alpha=0.6, edgecolors='w', linewidth=0.8)
    ax.set_title(titles[i], fontsize=14, fontweight='bold')
    ax.set_xlabel('Sunlight Hours', fontsize=10)
    ax.set_ylabel('Temperature (°C)', fontsize=10)
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)
    ax.set_facecolor('#f9f9f9')
    for j in range(len(sunlight_hours)):
        ax.annotate(f'{scores[j]}%', (sunlight_hours[j], temperatures[j]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

plt.suptitle('Artificial Intelligence Efficiency in Solar Generation: Sunlight vs Temperature Correlation', fontsize=16, fontweight='bold', y=1.03)

plt.tight_layout()

plt.show()