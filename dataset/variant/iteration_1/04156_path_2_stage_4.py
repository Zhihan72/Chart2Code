import matplotlib.pyplot as plt
import numpy as np

methods = ["Trad", "Inter", "Online", "Hybrid"]

greenwood_scores = [
    [65, 67, 70, 72],
    [75, 77, 80, 82],
    [55, 58, 60, 63],
    [70, 72, 75, 77]
]

riverdale_scores = [
    [60, 62, 64, 66],
    [80, 82, 84, 86],
    [50, 52, 54, 56],
    [68, 70, 72, 74]
]

hillside_scores = [
    [68, 70, 72, 74],
    [78, 80, 82, 84],
    [60, 62, 64, 66],
    [72, 74, 76, 78]
]

sunnyvale_scores = [
    [64, 66, 68, 70],
    [86, 88, 90, 92],
    [54, 56, 58, 60],
    [74, 76, 78, 80]
]

brookshire_scores = [
    [62, 65, 68, 70],
    [79, 81, 83, 85],
    [53, 55, 57, 59],
    [71, 73, 75, 77]
]

traditional_scores = greenwood_scores[0] + riverdale_scores[0] + hillside_scores[0] + sunnyvale_scores[0] + brookshire_scores[0]
interactive_scores = greenwood_scores[1] + riverdale_scores[1] + hillside_scores[1] + sunnyvale_scores[1] + brookshire_scores[1]
online_scores = greenwood_scores[2] + riverdale_scores[2] + hillside_scores[2] + sunnyvale_scores[2] + brookshire_scores[2]
hybrid_scores = greenwood_scores[3] + riverdale_scores[3] + hillside_scores[3] + sunnyvale_scores[3] + brookshire_scores[3]

fig, ax1 = plt.subplots(figsize=(8, 6))

data = [traditional_scores, interactive_scores, online_scores, hybrid_scores]

bp = ax1.boxplot(data, patch_artist=True, showmeans=True, notch=True,
                 boxprops=dict(facecolor="#32CD32", color="#9400D3", linewidth=1.2), 
                 medianprops=dict(color="#8B0000", linewidth=1.5),
                 meanprops=dict(marker='o', markeredgecolor='black', markerfacecolor='#FF69B4'),
                 whiskerprops=dict(color="#9400D3"), capprops=dict(color="#9400D3"))

ax1.set_title("Teaching Methods vs. Scores", fontsize=16, fontweight='bold', pad=15)
ax1.set_xlabel("Methods", fontsize=14)
ax1.set_ylabel("Scores", fontsize=14)
ax1.set_xticklabels(methods, fontsize=12)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()