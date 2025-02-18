import matplotlib.pyplot as plt
import numpy as np

festival_types = ['Art', 'Film', 'Food', 'Music']  # Manually shuffled festival types
months = ['Aug', 'Feb', 'May', 'Oct', 'Jan', 'Mar', 'Sep', 'Nov', 'Jul', 'Apr', 'Jun', 'Dec']  # Manually shuffled months

attendance_data = [
    [11, 12, 10, 9, 8, 7, 6, 6, 5, 5, 4, 4],  # Adjusted for shuffled month labels
    [8, 9, 7, 12, 10, 6, 7, 8, 5, 8, 5, 9],   # Adjusted for shuffled month labels
    [12, 10, 9, 8, 7, 6, 6, 5, 5, 4, 8, 4],   # Adjusted for shuffled month labels
    [11, 9, 10, 7, 8, 6, 5, 9, 6, 5, 8, 7]    # Adjusted for shuffled month labels
]

avg_ratings = [8.0, 7.5, 8.8, 8.5]  # Manually shuffled ratings to match shuffled festival types

sorted_attendance_data = [sorted(data) for data in attendance_data]

bar_width = 0.18
index = np.arange(len(months))

plt.figure(figsize=(15, 9))
single_color = '#FF6347'
pattern = ''

for i, festival in enumerate(festival_types):
    plt.bar(index + i * bar_width, sorted_attendance_data[i], bar_width, color=single_color, hatch=pattern)

ax2 = plt.gca().twinx()
ax2.plot([index.mean() + 1.5 * bar_width] * len(avg_ratings), avg_ratings, color='black', marker='o', linestyle='--', linewidth=2.5)

plt.title('Festival Vibes & Experiences in Metropolus (2023)', fontsize=18, fontweight='bold')  # Changed title
plt.xlabel('Event Calendar', fontsize=14)  # Changed x-axis label
plt.ylabel('Crowd Count (K)', fontsize=14)  # Changed y-axis label for left side
ax2.set_ylabel('Experience Score (max 10)', fontsize=14)  # Changed y-axis label for right side
plt.xticks(index + bar_width * 1.5, months, fontsize=12, rotation=45)

for i, monthly_data in enumerate(sorted_attendance_data):
    for j, count in enumerate(monthly_data):
        plt.text(index[j] + i * bar_width, count + 0.2, str(count), ha='center', va='bottom', fontsize=9)

for i, rating in enumerate(avg_ratings):
    ax2.text(index.mean() + 1.5 * bar_width, rating + 0.2, f'{rating}', ha='center', va='bottom', fontsize=11, color='black')

plt.tight_layout()
plt.show()