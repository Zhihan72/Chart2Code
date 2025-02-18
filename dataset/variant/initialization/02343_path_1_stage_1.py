import matplotlib.pyplot as plt
import numpy as np

decades = np.array(['1920s', '1930s', '1940s', '1950s', '1960s', 
                    '1970s', '1980s', '1990s', '2000s', '2010s'])

fiction_attendees = np.array([5, 6, 8, 10, 12, 14, 15, 16, 20, 25])
non_fiction_attendees = np.array([4, 5, 7, 9, 11, 13, 13, 14, 15, 18])
poetry_attendees = np.array([3, 4, 4, 5, 6, 7, 8, 9, 11, 12])

fiction_seminars = np.array([2, 3, 4, 5, 6, 7, 8, 9, 11, 13])
non_fiction_seminars = np.array([3, 3, 4, 5, 6, 7, 8, 8, 10, 11])
poetry_seminars = np.array([1, 2, 2, 3, 3, 4, 5, 6, 7, 8])

plt.figure(figsize=(12, 8))

# Use 'navy' color for all genres
plt.scatter(fiction_attendees, fiction_seminars, c='navy', label='Fiction', marker='o', s=100, alpha=0.7)
plt.scatter(non_fiction_attendees, non_fiction_seminars, c='navy', label='Non-fiction', marker='^', s=100, alpha=0.7)
plt.scatter(poetry_attendees, poetry_seminars, c='navy', label='Poetry', marker='s', s=100, alpha=0.7)

for i, decade in enumerate(decades):
    plt.annotate(decade, (fiction_attendees[i], fiction_seminars[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    plt.annotate(decade, (non_fiction_attendees[i], non_fiction_seminars[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    plt.annotate(decade, (poetry_attendees[i], poetry_seminars[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

plt.title('Ink and Insights: A Century of Famous Author Conventions', fontsize=16, fontweight='bold')
plt.xlabel('Number of Attendees (in hundreds)', fontsize=14)
plt.ylabel('Average Number of Seminars Offered', fontsize=14)
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(title='Literary Genres', title_fontsize='12', loc='upper left', fontsize=10)
plt.tight_layout()
plt.show()