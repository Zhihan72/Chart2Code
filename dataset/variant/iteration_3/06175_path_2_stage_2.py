import matplotlib.pyplot as plt
import numpy as np

# Data for weekend activities (percentage)
weekend_activities = ['Outdoor Sports', 'Reading', 'Watching TV', 'Socializing', 
                      'Gaming', 'Traveling', 'Cooking', 'Others']
weekend_percentages = [20, 15, 25, 10, 12, 8, 7, 3]

# Data for weekday activities (percentage)
weekday_percentages = [5, 20, 30, 15, 10, 5, 5, 10]

# Manually shuffled colors
colors = ['#a0c4ff', '#9bf6ff', '#caffbf', '#ffadad', '#bdb2ff', 
          '#ffc6ff', '#fdffb6', '#ffd6a5']

explode_weekend = [0.1 if activity == 'Watching TV' else 0 for activity in weekend_activities]

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14,7))

# Plotting the weekend activities pie chart
ax1.pie(
    weekend_percentages, labels=weekend_activities, colors=colors, autopct='%1.1f%%',
    startangle=140, explode=explode_weekend, shadow=False, textprops={'fontsize': 10, 'weight': 'bold'}
)
ax1.set_title("Weekend Leisure Activities\nDiverse Ways to Spend Your Free Time", fontsize=14, weight='bold', pad=20)

# Bar chart comparison
x = np.arange(len(weekend_activities))  # Label locations
width = 0.35

# Assigning shuffled colors for bar chart
bar_colors_weekend = ['#a0c4ff', '#9bf6ff', '#caffbf', '#ffadad', '#bdb2ff', 
                      '#ffc6ff', '#fdffb6', '#ffd6a5']

ax2.bar(x - width/2, weekend_percentages, width, color=bar_colors_weekend)
ax2.bar(x + width/2, weekday_percentages, width, color='#ffadad')

ax2.set_xlabel('Activities')
ax2.set_ylabel('Percentage')
ax2.set_title('Comparison of Leisure Activities\nBetween Weekdays and Weekends', fontsize=14, weight='bold', pad=20)
ax2.set_xticks(x)
ax2.set_xticklabels(weekend_activities)

for bars in ax2.containers:
    for bar in bars:
        height = bar.get_height()
        ax2.annotate(f'{height}%',
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3),
                     textcoords="offset points",
                     ha='center', va='bottom')

plt.tight_layout()
plt.show()