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

bar_height = 0.18
index = np.arange(len(months))

plt.figure(figsize=(15, 9))

single_color = '#8A2BE2'

for i, festival in enumerate(festival_types):
    plt.barh(index + i * bar_height, attendance_data[i], bar_height, label=festival, color=single_color)

ax2 = plt.gca().twiny()
ax2.plot(avg_ratings, [index.mean() + 1.5 * bar_height] * len(avg_ratings), color='red', marker='s', linestyle='-', linewidth=2.5, label='Avg Rating')

plt.title('Cultural Festivals in Metropolus: Attendance & Ratings - 2023', fontsize=18, fontweight='bold')
plt.ylabel('Months', fontsize=14)
plt.xlabel('Number of Attendees (Thousands)', fontsize=14)
ax2.set_xlabel('Average Rating (out of 10)', fontsize=14)

plt.yticks(index + bar_height * 1.5, months, fontsize=12)

for i, monthly_data in enumerate(attendance_data):
    for j, count in enumerate(monthly_data):
        plt.text(count + 0.5, index[j] + i * bar_height, str(count), va='center', ha='left', fontsize=9)

for i, rating in enumerate(avg_ratings):
    ax2.text(rating + 0.1, index.mean() + 1.5 * bar_height, f'{rating}', va='center', ha='left', fontsize=11, color='green')

plt.legend(title="Festival Type", fontsize=12, loc='upper right', bbox_to_anchor=(1.1, 1))
ax2.legend(loc='lower right', fontsize=12)

plt.grid(axis='both', linestyle='-', alpha=0.5)

plt.tight_layout()
plt.show()