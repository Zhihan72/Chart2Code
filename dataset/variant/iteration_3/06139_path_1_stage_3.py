import matplotlib.pyplot as plt
import numpy as np

age_groups = ["13-17", "18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
platforms = ["Facebook", "Instagram", "Twitter", "TikTok", "Youtube", "LinkedIn"]

usage_data = np.array([
    [15, 20, 5, 25, 30, 2],   
    [20, 25, 10, 30, 35, 5],  
    [18, 20, 8, 20, 28, 10],  
    [15, 18, 7, 10, 25, 12],   
    [10, 12, 6, 5, 18, 15],    
    [5, 8, 5, 2, 12, 10],      
    [2, 3, 4, 1, 8, 5]         
])

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.12

positions = np.arange(len(age_groups))

consistent_color = 'skyblue'

for i, platform in enumerate(platforms):
    bars = ax.bar(positions + i * bar_width, usage_data[:, i], bar_width, label=platform, color=consistent_color)

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 0.5, f'{height}', ha='center', va='bottom', fontsize=9)

ax.set_title("Average Monthly Time Spent on Social Media Platforms by Age Group", fontsize=18, fontweight='bold', color='darkblue')
ax.set_xlabel("Age Group", fontsize=14, color='brown')
ax.set_ylabel("Average Monthly Hours", fontsize=14, color='brown')
ax.set_xticks(positions + (len(platforms) - 1) * bar_width / 2)
ax.set_xticklabels(age_groups, fontsize=12, rotation=45, ha='right')
ax.legend(title="Platforms", ncol=3, frameon=False)

ax.yaxis.grid(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()