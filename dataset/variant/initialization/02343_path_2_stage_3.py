import matplotlib.pyplot as plt
import numpy as np

fiction_attendees = np.array([5, 6, 8, 10, 12, 14, 15, 16, 20, 25])
non_fiction_attendees = np.array([4, 5, 7, 9, 11, 13, 13, 14, 15, 18])

fiction_seminars = np.array([2, 3, 4, 5, 6, 7, 8, 9, 11, 13])
non_fiction_seminars = np.array([3, 3, 4, 5, 6, 7, 8, 8, 10, 11])

plt.figure(figsize=(12, 8))

plt.scatter(fiction_attendees, fiction_seminars, c='purple', marker='x', s=120, alpha=0.6)
plt.scatter(non_fiction_attendees, non_fiction_seminars, c='orange', marker='d', s=80, alpha=0.8)

plt.grid(False)

plt.tight_layout()
plt.show()