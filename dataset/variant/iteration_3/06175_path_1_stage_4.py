import matplotlib.pyplot as plt
import numpy as np

weekend_activities = ['Cooking', 'Others', 'Traveling', 'Gaming', 'Socializing', 'Reading', 'Outdoor Sports', 'Watching TV']
weekend_percentages = [7, 3, 8, 12, 10, 15, 20, 25]
weekday_percentages = [5, 10, 5, 10, 15, 20, 5, 30]

# Use a single color consistently
single_color = '#69b3a2'

fig, ax2 = plt.subplots(figsize=(7, 7))  # Reduced the figure size since one subplot is removed

# Bar chart comparison
x = np.arange(len(weekend_activities))  
width = 0.4  

bars1 = ax2.bar(x - width/2, weekend_percentages, width, label='Weekend', color=single_color, edgecolor='black', linestyle='-')
bars2 = ax2.bar(x + width/2, weekday_percentages, width, label='Weekday', color=single_color, alpha=0.7, edgecolor='black', linestyle='--')

ax2.set_xlabel('Activities', fontsize=12)
ax2.set_ylabel('Percentage', fontsize=12)
ax2.set_title('Leisure Activities: Weekdays vs Weekends', fontsize=14, weight='bold', pad=25)
ax2.set_xticks(x)
ax2.set_xticklabels(weekend_activities, rotation=45, ha='right')
ax2.grid(True, axis='y', linestyle=':', linewidth=0.7)
ax2.legend()

for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax2.annotate(f'{height}%', 
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3), 
                     textcoords="offset points",
                     ha='center', va='bottom')

plt.tight_layout()
plt.show()