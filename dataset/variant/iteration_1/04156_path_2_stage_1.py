import matplotlib.pyplot as plt
import numpy as np

# Define school names including the new school
schools = ["Greenwood High", "Riverdale Academy", "Hillside Institute", "Sunnyvale School", "Brookshire College"]
methods = ["Traditional", "Interactive", "Online", "Hybrid"]

# Defined exam score data, adding Brookshire College
greenwood_scores = [
    [65, 67, 70, 72],  # Traditional
    [75, 77, 80, 82],  # Interactive
    [55, 58, 60, 63],  # Online
    [70, 72, 75, 77]   # Hybrid
]

riverdale_scores = [
    [60, 62, 64, 66],  # Traditional
    [80, 82, 84, 86],  # Interactive
    [50, 52, 54, 56],  # Online
    [68, 70, 72, 74]   # Hybrid
]

hillside_scores = [
    [68, 70, 72, 74],  # Traditional
    [78, 80, 82, 84],  # Interactive
    [60, 62, 64, 66],  # Online
    [72, 74, 76, 78]   # Hybrid
]

sunnyvale_scores = [
    [64, 66, 68, 70],  # Traditional
    [86, 88, 90, 92],  # Interactive
    [54, 56, 58, 60],  # Online
    [74, 76, 78, 80]   # Hybrid
]

brookshire_scores = [
    [62, 65, 68, 70],  # Traditional
    [79, 81, 83, 85],  # Interactive
    [53, 55, 57, 59],  # Online
    [71, 73, 75, 77]   # Hybrid
]

# Group data by teaching method for boxplot
traditional_scores = greenwood_scores[0] + riverdale_scores[0] + hillside_scores[0] + sunnyvale_scores[0] + brookshire_scores[0]
interactive_scores = greenwood_scores[1] + riverdale_scores[1] + hillside_scores[1] + sunnyvale_scores[1] + brookshire_scores[1]
online_scores = greenwood_scores[2] + riverdale_scores[2] + hillside_scores[2] + sunnyvale_scores[2] + brookshire_scores[2]
hybrid_scores = greenwood_scores[3] + riverdale_scores[3] + hillside_scores[3] + sunnyvale_scores[3] + brookshire_scores[3]

# Set up the plot with multiple subplots
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(16, 12))

# Subplot 1: Distribution of scores by teaching methods
ax1 = axes[0]
data = [traditional_scores, interactive_scores, online_scores, hybrid_scores]
method_labels = ["Traditional", "Interactive", "Online", "Hybrid"]

bp = ax1.boxplot(data, patch_artist=True, showmeans=True, notch=True,
                 boxprops=dict(facecolor="#DDA0DD", color="#9400D3", linewidth=1.2), 
                 medianprops=dict(color="#8B0000", linewidth=1.5),
                 meanprops=dict(marker='o', markeredgecolor='black', markerfacecolor='#FFD700'),
                 whiskerprops=dict(color="#9400D3"), capprops=dict(color="#9400D3"))

ax1.set_title("Impact of Teaching Methods on Student Performance", fontsize=16, fontweight='bold', pad=15)
ax1.set_xlabel("Teaching Method", fontsize=14)
ax1.set_ylabel("Exam Scores", fontsize=14)
ax1.set_xticklabels(method_labels, fontsize=12)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Subplot 2: Comparison of mean scores by school for each method
ax2 = axes[1]
mean_scores = [
    [np.mean(greenwood_scores[0]), np.mean(riverdale_scores[0]), np.mean(hillside_scores[0]), np.mean(sunnyvale_scores[0]), np.mean(brookshire_scores[0])],
    [np.mean(greenwood_scores[1]), np.mean(riverdale_scores[1]), np.mean(hillside_scores[1]), np.mean(sunnyvale_scores[1]), np.mean(brookshire_scores[1])],
    [np.mean(greenwood_scores[2]), np.mean(riverdale_scores[2]), np.mean(hillside_scores[2]), np.mean(sunnyvale_scores[2]), np.mean(brookshire_scores[2])],
    [np.mean(greenwood_scores[3]), np.mean(riverdale_scores[3]), np.mean(hillside_scores[3]), np.mean(sunnyvale_scores[3]), np.mean(brookshire_scores[3])]
]

x = np.arange(len(schools))  # label locations
width = 0.2  # width of the bars

ax2.bar(x - 1.5*width, mean_scores[0], width, label='Traditional', color='#87CEFA')
ax2.bar(x - 0.5*width, mean_scores[1], width, label='Interactive', color='#32CD32')
ax2.bar(x + 0.5*width, mean_scores[2], width, label='Online', color='#FFA07A')
ax2.bar(x + 1.5*width, mean_scores[3], width, label='Hybrid', color='#FF69B4')

ax2.set_title("Mean Exam Scores by Teaching Method\nfor Each School", fontsize=16, fontweight='bold', pad=15)
ax2.set_xlabel('Schools', fontsize=14)
ax2.set_ylabel('Mean Exam Scores', fontsize=14)
ax2.set_xticks(x)
ax2.set_xticklabels(schools, fontsize=12)
ax2.legend(title='Teaching Method', fontsize=10, title_fontsize=12)
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()