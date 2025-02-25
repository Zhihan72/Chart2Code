import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

books = [20, 19, 18, 18, 17, 16, 15, 14, 12, 10, 8]
online_courses = [2, 3, 4, 5, 7, 8, 10, 12, 14, 16, 18]
educational_apps = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 20]
videos = [5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17]
tutoring = [10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 4]
podcasts = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.figure(figsize=(14, 8))

plt.stackplot(years, books, online_courses, educational_apps, videos, tutoring, podcasts,
              colors=['#66b2ff', '#ff9999', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6'], alpha=0.8)

plt.title("Evolution in Learner Tool Engagement (2010 to 2020)", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Timeline Span", fontsize=12)
plt.ylabel("Hours Spent Weekly", fontsize=12)

plt.tight_layout()

plt.show()