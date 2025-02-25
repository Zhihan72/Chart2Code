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
              colors=['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231'], alpha=0.8)

plt.title("Decade of Learning: Evolving Study Tools (2010-2020)", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Year of Study", fontsize=12)
plt.ylabel("Hours Spent Weekly", fontsize=12)

plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0., title='Tools for Learning')

plt.grid(linestyle='--', alpha=0.7)

plt.annotate('Surge in App Use', xy=(2015, 20), xytext=(2012, 60),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, backgroundcolor='w')

plt.annotate('Books Falling Out', xy=(2016, 16), xytext=(2013, 50),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, backgroundcolor='w')

plt.tight_layout()
plt.show()