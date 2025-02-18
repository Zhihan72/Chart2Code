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

# Randomly altered stylistic elements
plt.scatter(fiction_attendees, fiction_seminars, c='purple', label='Fiction', marker='x', s=120, alpha=0.6)
plt.scatter(non_fiction_attendees, non_fiction_seminars, c='orange', label='Non-fiction', marker='d', s=80, alpha=0.8)
plt.scatter(poetry_attendees, poetry_seminars, c='green', label='Poetry', marker='*', s=140, alpha=0.7)

for i, decade in enumerate(decades):
    plt.annotate(decade, (fiction_attendees[i], fiction_seminars[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    plt.annotate(decade, (non_fiction_attendees[i], non_fiction_seminars[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    plt.annotate(decade, (poetry_attendees[i], poetry_seminars[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

# Adjusted titles and labels
plt.title('Ink and Insights: A Century of Famous Author Conventions', fontsize=18, fontweight='bold')
plt.xlabel('Number of Attendees (in hundreds)', fontsize=12)
plt.ylabel('Average Number of Seminars Offered', fontsize=12)

# Modified grid and legend options
plt.grid(False)
plt.legend(title='Literary Genres', title_fontsize='12', loc='lower right', fontsize=10)

plt.tight_layout()
plt.show()