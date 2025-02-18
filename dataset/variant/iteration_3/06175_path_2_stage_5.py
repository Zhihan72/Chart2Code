import matplotlib.pyplot as plt

weekend_activities = ['Outdoor Sports', 'Reading', 'Watching TV', 'Socializing', 
                      'Gaming', 'Traveling', 'Cooking', 'Others']
weekend_percentages = [10, 25, 15, 12, 20, 8, 7, 3]
weekday_percentages = [5, 10, 30, 20, 15, 5, 10, 5]

fig, axes = plt.subplots(1, 2, figsize=(14, 7))

# Weekend activities donut pie chart
axes[0].pie(weekend_percentages, labels=weekend_activities, autopct='%1.1f%%', startangle=90, pctdistance=0.85,
            wedgeprops=dict(width=0.3))
axes[0].set_title('Weekend Activities', fontsize=14, weight='bold')

# Weekday activities donut pie chart
axes[1].pie(weekday_percentages, labels=weekend_activities, autopct='%1.1f%%', startangle=90, pctdistance=0.85,
            wedgeprops=dict(width=0.3))
axes[1].set_title('Weekday Activities', fontsize=14, weight='bold')

plt.tight_layout()
plt.show()