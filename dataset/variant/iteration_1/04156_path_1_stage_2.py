import matplotlib.pyplot as plt
import numpy as np

# Define school names
schools = ["Highland Greens", "Brookvale Institute", "Crestwood Academy", "Waterside School"]

# Define exam score data
highland_scores = [
    [65, 67, 70, 72],  # Conventional
    [75, 77, 80, 82],  # Hands-On
    [55, 58, 60, 63],  # Remote
    [70, 72, 75, 77]   # Mix-Mode
]

brookvale_scores = [
    [60, 62, 64, 66],  # Conventional
    [80, 82, 84, 86],  # Hands-On
    [50, 52, 54, 56],  # Remote
    [68, 70, 72, 74]   # Mix-Mode
]

crestwood_scores = [
    [68, 70, 72, 74],  # Conventional
    [78, 80, 82, 84],  # Hands-On
    [60, 62, 64, 66],  # Remote
    [72, 74, 76, 78]   # Mix-Mode
]

waterside_scores = [
    [64, 66, 68, 70],  # Conventional
    [86, 88, 90, 92],  # Hands-On
    [54, 56, 58, 60],  # Remote
    [74, 76, 78, 80]   # Mix-Mode
]

# Comparison of mean scores by school for each method
fig, ax2 = plt.subplots(figsize=(16, 6))

mean_scores = [
    [np.mean(highland_scores[0]), np.mean(brookvale_scores[0]), np.mean(crestwood_scores[0]), np.mean(waterside_scores[0])],
    [np.mean(highland_scores[1]), np.mean(brookvale_scores[1]), np.mean(crestwood_scores[1]), np.mean(waterside_scores[1])],
    [np.mean(highland_scores[2]), np.mean(brookvale_scores[2]), np.mean(crestwood_scores[2]), np.mean(waterside_scores[2])],
    [np.mean(highland_scores[3]), np.mean(brookvale_scores[3]), np.mean(crestwood_scores[3]), np.mean(waterside_scores[3])]
]

x = np.arange(len(schools))
width = 0.2

ax2.bar(x - 1.5*width, mean_scores[0], width, label='Conventional', color='#87CEFA')
ax2.bar(x - 0.5*width, mean_scores[1], width, label='Hands-On', color='#32CD32')
ax2.bar(x + 0.5*width, mean_scores[2], width, label='Remote', color='#FFA07A')
ax2.bar(x + 1.5*width, mean_scores[3], width, label='Mix-Mode', color='#FF69B4')

ax2.set_title("Average Scores per Teaching Style\nat Each Institution", fontsize=16, fontweight='bold', pad=15)
ax2.set_xlabel('Institutes', fontsize=14)
ax2.set_ylabel('Average Score', fontsize=14)
ax2.set_xticks(x)
ax2.set_xticklabels(schools, fontsize=12)
ax2.legend(title='Teaching Style', fontsize=10, title_fontsize=12)
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()