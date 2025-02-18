import matplotlib.pyplot as plt
import numpy as np

# Define school names
schools = ["Highland Greens", "Brookvale Institute", "Crestwood Academy", "Waterside School"]

# Define exam score data for three teaching styles only
highland_scores = [
    [65, 67, 70, 72],  # Conventional
    [75, 77, 80, 82],  # Hands-On
    [70, 72, 75, 77]   # Mix-Mode
]

brookvale_scores = [
    [60, 62, 64, 66],  # Conventional
    [80, 82, 84, 86],  # Hands-On
    [68, 70, 72, 74]   # Mix-Mode
]

crestwood_scores = [
    [68, 70, 72, 74],  # Conventional
    [78, 80, 82, 84],  # Hands-On
    [72, 74, 76, 78]   # Mix-Mode
]

waterside_scores = [
    [64, 66, 68, 70],  # Conventional
    [86, 88, 90, 92],  # Hands-On
    [74, 76, 78, 80]   # Mix-Mode
]

# Comparison of score distributions without 'Remote' method
fig, ax2 = plt.subplots(figsize=(16, 6))

# Create a list of score data for remaining teaching styles across all schools
conventional_scores = [highland_scores[0], brookvale_scores[0], crestwood_scores[0], waterside_scores[0]]
hands_on_scores = [highland_scores[1], brookvale_scores[1], crestwood_scores[1], waterside_scores[1]]
mix_mode_scores = [highland_scores[2], brookvale_scores[2], crestwood_scores[2], waterside_scores[2]]

positions = np.arange(len(schools))

# Plot horizontal box plots without 'Remote'
ax2.boxplot(conventional_scores, positions=positions - 1, vert=False, patch_artist=True,
            boxprops=dict(facecolor='#87CEFA', alpha=0.5), labels=schools)
ax2.boxplot(hands_on_scores, positions=positions, vert=False, patch_artist=True,
            boxprops=dict(facecolor='#32CD32', alpha=0.5))
ax2.boxplot(mix_mode_scores, positions=positions + 1, vert=False, patch_artist=True,
            boxprops=dict(facecolor='#FF69B4', alpha=0.5))

ax2.set_title("Score Distributions per Teaching Style\nat Each Institution", fontsize=16, fontweight='bold', pad=15)
ax2.set_xlabel('Scores', fontsize=14)
ax2.set_yticks(positions)
ax2.set_yticklabels(schools, fontsize=12)
ax2.legend(['Conventional', 'Hands-On', 'Mix-Mode'], title='Teaching Style', fontsize=10, title_fontsize=12)
ax2.xaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()