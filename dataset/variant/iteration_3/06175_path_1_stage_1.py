import matplotlib.pyplot as plt
import numpy as np

# Data for weekend activities and percentages, sorted in descending order
weekend_activities = ['Cooking', 'Others', 'Traveling', 'Gaming', 'Socializing', 'Reading', 'Outdoor Sports', 'Watching TV']
weekend_percentages = [7, 3, 8, 12, 10, 15, 20, 25]

# Data for weekday percentages aligned with sorted weekend activities
weekday_percentages = [5, 10, 5, 10, 15, 20, 5, 30]

colors = ['#ffadad', '#ffd6a5', '#fdffb6', '#caffbf', '#9bf6ff', 
          '#a0c4ff', '#bdb2ff', '#ffc6ff']

# Create a subplot grid
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14,7))

# Plotting the weekend activities pie chart
wedges, texts, autotexts = ax1.pie(
    weekend_percentages, labels=weekend_activities, colors=colors, autopct='%1.1f%%',
    startangle=140, shadow=True, textprops={'fontsize': 10, 'weight': 'bold'}
)
ax1.set_title("Weekend Leisure Activities\nDiverse Ways to Spend Your Free Time", fontsize=14, weight='bold', pad=20)
ax1.legend(wedges, weekend_activities, title="Activities", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Sorted bar chart comparison
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