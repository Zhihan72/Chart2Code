import matplotlib.pyplot as plt
import numpy as np

# Backstory
# This chart represents the distribution of different types of activities people engage in during their leisure time, specifically on weekends. Additionally, it offers a comparison with the types of activities on weekdays. We want to ensure people know what they might be missing out on when not effectively planning their leisure time.

# Data for weekend activities (percentage)
weekend_activities = ['Outdoor Sports', 'Reading', 'Watching TV', 'Socializing', 
                      'Gaming', 'Traveling', 'Cooking', 'Others']
weekend_percentages = [20, 15, 25, 10, 12, 8, 7, 3]

# Data for weekday activities (percentage)
weekday_percentages = [5, 20, 30, 15, 10, 5, 5, 10]

colors = ['#ffadad', '#ffd6a5', '#fdffb6', '#caffbf', '#9bf6ff', 
          '#a0c4ff', '#bdb2ff', '#ffc6ff']

explode_weekend = [0.1 if activity == 'Watching TV' else 0 for activity in weekend_activities]

# Create a subplot grid
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14,7))

# Plotting the weekend activities pie chart
wedges, texts, autotexts = ax1.pie(
    weekend_percentages, labels=weekend_activities, colors=colors, autopct='%1.1f%%',
    startangle=140, explode=explode_weekend, shadow=True, textprops={'fontsize': 10, 'weight': 'bold'}
)
ax1.set_title("Weekend Leisure Activities\nDiverse Ways to Spend Your Free Time", fontsize=14, weight='bold', pad=20)
ax1.legend(wedges, weekend_activities, title="Activities", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Bar chart comparison
x = np.arange(len(weekend_activities))  # Label locations
width = 0.35  # Width of bars

bars1 = ax2.bar(x - width/2, weekend_percentages, width, label='Weekend', color=['#ffadad'])
bars2 = ax2.bar(x + width/2, weekday_percentages, width, label='Weekday', color=['#9bf6ff'])

# Add some text for labels, title and custom x-axis tick labels, etc.
ax2.set_xlabel('Activities')
ax2.set_ylabel('Percentage')
ax2.set_title('Comparison of Leisure Activities\nBetween Weekdays and Weekends', fontsize=14, weight='bold', pad=20)
ax2.set_xticks(x)
ax2.set_xticklabels(weekend_activities)
ax2.legend()

# Attach a text label above each bar in the bar chart, displaying its height.
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax2.annotate(f'{height}%',
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3),  # 3 points vertical offset
                     textcoords="offset points",
                     ha='center', va='bottom')

# Adjust layout to be tidy
plt.tight_layout()

# Show the plot
plt.show()