import matplotlib.pyplot as plt

methods = ["Trad", "Inter", "Online", "Hybrid"]

traditional_scores = [65, 67, 70, 72, 60, 62, 64, 66, 68, 70, 72, 74, 64, 66, 68, 70, 62, 65, 68, 70]
interactive_scores = [75, 77, 80, 82, 80, 82, 84, 86, 78, 80, 82, 84, 86, 88, 90, 92, 79, 81, 83, 85]
online_scores = [55, 58, 60, 63, 50, 52, 54, 56, 60, 62, 64, 66, 54, 56, 58, 60, 53, 55, 57, 59]
hybrid_scores = [70, 72, 75, 77, 68, 70, 72, 74, 72, 74, 76, 78, 74, 76, 78, 80, 71, 73, 75, 77]

fig, ax1 = plt.subplots(figsize=(8, 6))

data = [traditional_scores, interactive_scores, online_scores, hybrid_scores]

bp = ax1.boxplot(data, patch_artist=True, showmeans=True, notch=True,
                 boxprops=dict(facecolor="#8B008B", color="#00CED1", linewidth=1.5), 
                 medianprops=dict(color="#FF4500", linewidth=2),
                 meanprops=dict(marker='^', markeredgecolor='black', markerfacecolor='#FFD700'),
                 whiskerprops=dict(color="#1E90FF", linestyle='-.'), capprops=dict(color="#1E90FF"))

ax1.set_title("Teaching Methods vs. Scores", fontsize=16, fontweight='bold', pad=15, color='#2F4F4F')
ax1.set_xlabel("Methods", fontsize=14, color='#8B0000')
ax1.set_ylabel("Scores", fontsize=14, color='#8B0000')
ax1.set_xticklabels(methods, fontsize=12)
ax1.yaxis.grid(True, linestyle=':', alpha=0.5)

# Adding legend with a different style
ax1.legend([bp["boxes"][0], bp["medians"][0], bp["means"][0]], ['Box', 'Median', 'Mean'], loc='upper right', fontsize=10, frameon=True, framealpha=0.5, shadow=True, edgecolor='#FF4500')

plt.tight_layout()
plt.show()