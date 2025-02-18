import matplotlib.pyplot as plt
import numpy as np

# Festival types and months
festival_types = ['Music', 'Food', 'Art', 'Film', 'Technology']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Attendance data (number of attendees in thousands)
attendance_data = [
    [8, 6, 5, 9, 12, 10, 8, 6, 7, 10, 11, 9],
    [5, 7, 8, 6, 9, 12, 10, 8, 9, 7, 6, 5],
    [4, 5, 9, 7, 8, 10, 11, 9, 8, 7, 5, 4],
    [6, 8, 7, 5, 6, 11, 12, 10, 9, 8, 7, 6],
    [7, 9, 6, 5, 8, 9, 8, 10, 7, 6, 5, 7]
]

# Average rating data (out of 10)
avg_ratings = [8.5, 8.0, 7.5, 8.8, 9.0]

bar_width = 0.18
index = np.arange(len(months))

plt.figure(figsize=(15, 9))
colors = ['#FF6347', '#FFD700', '#8A2BE2', '#00BFFF', '#32CD32']
patterns = ["", ".", "x", "/", "\\"]

for i, (festival, color, pattern) in enumerate(zip(festival_types, colors, patterns)):
    plt.bar(index + i * bar_width, attendance_data[i], bar_width, color=color, hatch=pattern)

ax2 = plt.gca().twinx()
ax2.plot([index.mean() + 2 * bar_width] * len(avg_ratings), avg_ratings, color='black', marker='o', linestyle='--', linewidth=2.5)

plt.title('Attendance and Ratings of Cultural Festivals in Metropolus (2023)', fontsize=18, fontweight='bold')
plt.xlabel('Months', fontsize=14)
plt.ylabel('Number of Attendees (Thousands)', fontsize=14)
ax2.set_ylabel('Average Rating (out of 10)', fontsize=14)
plt.xticks(index + bar_width * 2, months, fontsize=12, rotation=45)

for i, monthly_data in enumerate(attendance_data):
    for j, count in enumerate(monthly_data):
        plt.text(index[j] + i * bar_width, count + 0.2, str(count), ha='center', va='bottom', fontsize=9)

for i, rating in enumerate(avg_ratings):
    ax2.text(index.mean() + 2 * bar_width, rating + 0.2, f'{rating}', ha='center', va='bottom', fontsize=11, color='black')

plt.tight_layout()
plt.show()