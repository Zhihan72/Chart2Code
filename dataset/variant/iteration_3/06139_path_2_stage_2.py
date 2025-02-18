import matplotlib.pyplot as plt
import numpy as np

age_groups = ["18-24", "25-34", "35-44", "45-54", "55-64", "65+", "13-17"]
platforms = ["TikTok", "Instagram", "Youtube", "Facebook", "Snapchat", "Twitter"]

# Average monthly usage in hours for each platform by age group
usage_data = np.array([
    [15, 20, 10, 5, 25, 30],   # 13-17
    [20, 25, 15, 10, 30, 35],  # 18-24
    [18, 20, 12, 8, 20, 28],   # 25-34
    [15, 18, 8, 7, 10, 25],    # 35-44
    [10, 12, 5, 6, 5, 18],     # 45-54
    [5, 8, 2, 5, 2, 12],       # 55-64
    [2, 3, 1, 4, 1, 8]         # 65+
])

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.1

positions = np.arange(len(age_groups))
for i, platform in enumerate(platforms):
    bars = ax.bar(positions + i * bar_width, usage_data[:, i], bar_width, label=platform)

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.5, f'{height}', ha='center', va='bottom', fontsize=9)

ax.set_title("Social Media Use by Various Ages", fontsize=18, fontweight='bold')
ax.set_xlabel("User Age Categories", fontsize=14)
ax.set_ylabel("Monthly Use in Hours", fontsize=14)
ax.set_xticks(positions + (len(platforms) - 1) * bar_width / 2)
ax.set_xticklabels(age_groups, fontsize=12, rotation=45, ha='right')
ax.legend(title="Service Platforms")
ax.yaxis.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()