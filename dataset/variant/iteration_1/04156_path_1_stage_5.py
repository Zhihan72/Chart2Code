import matplotlib.pyplot as plt
import numpy as np

schools = ["Highland Greens", "Brookvale Institute", "Crestwood Academy", "Waterside School"]

highland_scores = [
    [65, 67, 70, 72],
    [75, 77, 80, 82],
    [70, 72, 75, 77]
]

brookvale_scores = [
    [60, 62, 64, 66],
    [80, 82, 84, 86],
    [68, 70, 72, 74]
]

crestwood_scores = [
    [68, 70, 72, 74],
    [78, 80, 82, 84],
    [72, 74, 76, 78]
]

waterside_scores = [
    [64, 66, 68, 70],
    [86, 88, 90, 92],
    [74, 76, 78, 80]
]

fig, ax2 = plt.subplots(figsize=(16, 6))

conventional_scores = [highland_scores[0], brookvale_scores[0], crestwood_scores[0], waterside_scores[0]]
hands_on_scores = [highland_scores[1], brookvale_scores[1], crestwood_scores[1], waterside_scores[1]]
mix_mode_scores = [highland_scores[2], brookvale_scores[2], crestwood_scores[2], waterside_scores[2]]

positions = np.arange(len(schools))

ax2.boxplot(conventional_scores, positions=positions - 1, vert=False, patch_artist=True,
            boxprops=dict(facecolor='#FFD700', alpha=0.7), labels=schools,
            flierprops=dict(marker='d', color='red'), medianprops=dict(color='darkred', linewidth=2))
ax2.boxplot(hands_on_scores, positions=positions, vert=False, patch_artist=True,
            boxprops=dict(facecolor='#4682B4', alpha=0.7),
            flierprops=dict(marker='o', color='blue'), medianprops=dict(color='navy', linewidth=2))
ax2.boxplot(mix_mode_scores, positions=positions + 1, vert=False, patch_artist=True,
            boxprops=dict(facecolor='#8A2BE2', alpha=0.7),
            flierprops=dict(marker='^', color='purple'), medianprops=dict(color='indigo', linewidth=2))

ax2.set_title("Score Distributions per Teaching Style\nat Each Institution", fontsize=14, fontweight='light', pad=10)
ax2.set_xlabel('Scores', fontsize=12)
ax2.set_yticks(positions)
ax2.set_yticklabels(schools, fontsize=10)
ax2.legend(['Conventional', 'Hands-On', 'Mix-Mode'], title='Teaching Style', fontsize=11, title_fontsize=13, loc='upper left')
ax2.xaxis.grid(True, linestyle='-', alpha=0.4)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()