import matplotlib.pyplot as plt
import numpy as np

decades = np.array(['1920s', '1930s', '1940s', '1950s', '1960s', 
                    '1970s', '1980s', '1990s', '2000s', '2010s'])

fiction_attendees = np.array([5, 6, 8, 10, 12, 14, 15, 16, 20, 25])
non_fiction_attendees = np.array([4, 5, 7, 9, 11, 13, 13, 14, 15, 18])

fiction_seminars = np.array([2, 3, 4, 5, 6, 7, 8, 9, 11, 13])
non_fiction_seminars = np.array([3, 3, 4, 5, 6, 7, 8, 8, 10, 11])

plt.figure(figsize=(12, 8))

plt.scatter(fiction_attendees, fiction_seminars, c='navy', marker='o', s=100, alpha=0.7)
plt.scatter(non_fiction_attendees, non_fiction_seminars, c='navy', marker='^', s=100, alpha=0.7)

for i, decade in enumerate(decades):
    plt.annotate(decade, (fiction_attendees[i], fiction_seminars[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    plt.annotate(decade, (non_fiction_attendees[i], non_fiction_seminars[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

plt.title('Century of Author Cons.', fontsize=16, fontweight='bold')
plt.xlabel('Attendees (hundreds)', fontsize=14)
plt.ylabel('Avg. Seminars Offered', fontsize=14)
plt.tight_layout()
plt.show()