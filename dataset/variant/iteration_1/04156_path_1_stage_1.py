import matplotlib.pyplot as plt
import numpy as np

# Define school names and teaching methods with manually altered labels
schools = ["Highland Greens", "Brookvale Institute", "Crestwood Academy", "Waterside School"]
methods = ["Conventional", "Hands-On", "Remote", "Mix-Mode"]

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

# Group data by teaching method for boxplot
conventional_scores = list(zip(*[highland_scores[0], brookvale_scores[0], crestwood_scores[0], waterside_scores[0]]))
hands_on_scores = list(zip(*[highland_scores[1], brookvale_scores[1], crestwood_scores[1], waterside_scores[1]]))
remote_scores = list(zip(*[highland_scores[2], brookvale_scores[2], crestwood_scores[2], waterside_scores[2]]))
mix_mode_scores = list(zip(*[highland_scores[3], brookvale_scores[3], crestwood_scores[3], waterside_scores[3]]))

# Set up the plot with subplots
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(16, 12))

# Subplot 1: Distribution of scores by teaching methods
ax1 = axes[0]
data = conventional_scores + hands_on_scores + remote_scores + mix_mode_scores
method_labels = ["Conventional\n(Highland)", "Conventional\n(Brookvale)", "Conventional\n(Crestwood)", "Conventional\n(Waterside)", 
                 "Hands-On\n(Highland)", "Hands-On\n(Brookvale)", "Hands-On\n(Crestwood)", "Hands-On\n(Waterside)",
                 "Remote\n(Highland)", "Remote\n(Brookvale)", "Remote\n(Crestwood)", "Remote\n(Waterside)",
                 "Mix-Mode\n(Highland)", "Mix-Mode\n(Brookvale)", "Mix-Mode\n(Crestwood)", "Mix-Mode\n(Waterside)"]

bp = ax1.boxplot(data, patch_artist=True, showmeans=True, notch=True,
                 boxprops=dict(facecolor="#DDA0DD", color="#9400D3", linewidth=1.2), 
                 medianprops=dict(color="#8B0000", linewidth=1.5),
                 meanprops=dict(marker='o', markeredgecolor='black', markerfacecolor='#FFD700'),
                 whiskerprops=dict(color="#9400D3"), capprops=dict(color="#9400D3"))

ax1.set_title("Analyzing Student Exam Outcomes\nvia Teaching Styles", fontsize=16, fontweight='bold', pad=15)
ax1.set_xlabel("Style & Institution", fontsize=14)
ax1.set_ylabel("Score Metrics", fontsize=14)
ax1.set_xticklabels(method_labels, fontsize=11, rotation=45, ha='right')
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Subplot 2: Comparison of mean scores by school for each method
ax2 = axes[1]
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