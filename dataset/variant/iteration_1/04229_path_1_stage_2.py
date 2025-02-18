import matplotlib.pyplot as plt
import numpy as np

festival_types = ['Music', 'Food', 'Art', 'Technology']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

attendance_data = [
    [8, 6, 5, 9, 12, 10, 8, 6, 7, 10, 11, 9], 
    [5, 7, 8, 6, 9, 12, 10, 8, 9, 7, 6, 5],  
    [4, 5, 9, 7, 8, 10, 11, 9, 8, 7, 5, 4],  
    [7, 9, 6, 5, 8, 9, 8, 10, 7, 6, 5, 7]    
]

avg_ratings = [8.5, 8.0, 7.5, 9.0]

bar_width = 0.18
index = np.arange(len(months))

plt.figure(figsize=(15, 9))

colors = ['#8A2BE2', '#32CD32', '#FF6347', '#FFD700']
patterns = ["\\", "", ".", "/"]

for i, (festival, color, pattern) in enumerate(zip(festival_types, colors, patterns)):
    plt.bar(index + i * bar_width, attendance_data[i], bar_width, label=festival, color=color, hatch=pattern)

ax2 = plt.gca().twinx()
ax2.plot([index.mean() + 1.5 * bar_width] * len(avg_ratings), avg_ratings, color='red', marker='s', linestyle='-', linewidth=2.5, label='Avg Rating')

plt.title('Cultural Festivals in Metropolus: Attendance & Ratings - 2023', fontsize=18, fontweight='bold')
plt.xlabel('Months', fontsize=14)
plt.ylabel('Number of Attendees (Thousands)', fontsize=14)
ax2.set_ylabel('Average Rating (out of 10)', fontsize=14)

plt.xticks(index + bar_width * 1.5, months, fontsize=12, rotation=45)

for i, monthly_data in enumerate(attendance_data):
    for j, count in enumerate(monthly_data):
        plt.text(index[j] + i * bar_width, count + 0.2, str(count), ha='center', va='bottom', fontsize=9)

for i, rating in enumerate(avg_ratings):
    ax2.text(index.mean() + 1.5 * bar_width, rating + 0.2, f'{rating}', ha='center', va='bottom', fontsize=11, color='green')

plt.legend(title="Festival Type", fontsize=12, loc='upper right', bbox_to_anchor=(1.1, 0.9))
ax2.legend(loc='upper left', fontsize=12)

plt.grid(axis='both', linestyle='-', alpha=0.5)

plt.tight_layout()
plt.show()