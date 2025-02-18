import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

books = [21, 18, 17, 20, 16, 15, 15, 13, 13, 9, 7]
online_courses = [3, 5, 2, 4, 8, 7, 9, 14, 10, 16, 18]
educational_apps = [2, 1, 3, 6, 7, 11, 5, 13, 15, 20, 17]
videos = [6, 5, 7, 9, 8, 11, 10, 12, 13, 15, 17]
tutoring = [9, 10, 8, 8, 9, 7, 6, 7, 5, 4, 6]

plt.figure(figsize=(14, 8))

plt.stackplot(years, books, online_courses, educational_apps, videos, tutoring,
              labels=['Paperbacks', 'Web Courses', 'App Sessions', 'Multimedia', 'Private Lessons'],
              colors=['#4363d8', '#3cb44b', '#e6194b', '#f58231', '#ffe119'], alpha=0.8)

plt.title("Decade of Learning: Evolving Study Tools (2010-2020)", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Year of Study", fontsize=13)
plt.ylabel("Weekly Study Hours", fontsize=11)

plt.legend(loc='upper right', bbox_to_anchor=(0.95, 0.95), shadow=True, fontsize='large', title='Learning Tools')

plt.grid(linestyle='-.', linewidth=0.5)

plt.annotate('Significant App Growth', xy=(2015, 20), xytext=(2012, 45),
             arrowprops=dict(facecolor='green', shrink=0.1),
             fontsize=9, fontstyle='italic', backgroundcolor='lightgrey')

plt.annotate('Decline of Books', xy=(2016, 16), xytext=(2014, 35),
             arrowprops=dict(facecolor='red', arrowstyle='->'),
             fontsize=9, fontweight='bold', backgroundcolor='lightyellow')

plt.xticks(np.arange(2010, 2021, 2))

plt.tight_layout()
plt.show()