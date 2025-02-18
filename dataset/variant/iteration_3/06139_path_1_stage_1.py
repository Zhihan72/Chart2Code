import matplotlib.pyplot as plt
import numpy as np

# Define age groups and social media platforms
age_groups = ["13-17", "18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
platforms = ["Facebook", "Instagram", "Snapchat", "Twitter", "TikTok", "Youtube", "LinkedIn"]

# Average monthly usage in hours for each platform by age group
usage_data = np.array([
    [15, 20, 10, 5, 25, 30, 2],   
    [20, 25, 15, 10, 30, 35, 5],  
    [18, 20, 12, 8, 20, 28, 10],  
    [15, 18, 8, 7, 10, 25, 12],   
    [10, 12, 5, 6, 5, 18, 15],    
    [5, 8, 2, 5, 2, 12, 10],      
    [2, 3, 1, 4, 1, 8, 5]         
])

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.1

positions = np.arange(len(age_groups))
marker_styles = ['^', 'o', 's', 'd', 'x', '*', 'p'] 
line_styles = ['-', '--', '-.', ':', '-', '--', '-.']

for i, platform in enumerate(platforms):
    bars = ax.bar(positions + i * bar_width, usage_data[:, i], bar_width, label=platform, 
                  hatch=marker_styles[i])

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 0.5, f'{height}', ha='center', va='bottom', fontsize=9)

ax.set_title("Average Monthly Time Spent on Social Media Platforms by Age Group", fontsize=18, fontweight='bold', color='darkblue')
ax.set_xlabel("Age Group", fontsize=14, color='brown')
ax.set_ylabel("Average Monthly Hours", fontsize=14, color='brown')
ax.set_xticks(positions + (len(platforms) - 1) * bar_width / 2)
ax.set_xticklabels(age_groups, fontsize=12, rotation=45, ha='right')
ax.legend(title="Platforms", ncol=3, frameon=False)

ax.yaxis.grid(False)  # Removed grid lines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()