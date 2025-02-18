import matplotlib.pyplot as plt
import numpy as np

# Data for activities (percentage)
weekend_activities = ['Outdoor Sports', 'Reading', 'Watching TV', 'Socializing', 
                      'Gaming', 'Traveling', 'Cooking', 'Others']
weekend_percentages = [20, 15, 25, 10, 12, 8, 7, 3]
weekday_percentages = [5, 20, 30, 15, 10, 5, 5, 10]

fig, ax = plt.subplots(figsize=(7,7))

x = np.arange(len(weekend_activities))  # Label locations
width = 0.35

ax.bar(x - width/2, weekend_percentages, width, color=['#a0c4ff', '#9bf6ff', '#caffbf', '#ffadad', '#bdb2ff', 
                                                       '#ffc6ff', '#fdffb6', '#ffd6a5'])
ax.bar(x + width/2, weekday_percentages, width, color='#ffadad')

ax.set_xlabel('Activities')
ax.set_ylabel('Percentage')
ax.set_title('Comparison of Leisure Activities\nBetween Weekdays and Weekends', fontsize=14, weight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(weekend_activities)

for bars in ax.containers:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}%',
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3),
                     textcoords="offset points",
                     ha='center', va='bottom')

plt.tight_layout()
plt.show()