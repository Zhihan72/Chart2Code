import matplotlib.pyplot as plt
import numpy as np

# Years series from 2010 to 2020
years = np.arange(2010, 2021)

# Weekly usage data for various educational tools
books = [20, 19, 18, 18, 17, 16, 15, 14, 12, 10, 8]
online_courses = [2, 3, 4, 5, 7, 8, 10, 12, 14, 16, 18]
educational_apps = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 20]
videos = [5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17]
tutoring = [10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 4]

plt.figure(figsize=(14, 8))

plt.stackplot(years, books, online_courses, educational_apps, videos, tutoring,
              labels=['Paperbacks', 'Web Courses', 'App Sessions', 'Multimedia', 'Private Lessons'],
              colors=['#ff9999', '#66b2ff', '#99ff99', '#ffcc99', '#c2c2f0'], alpha=0.8)

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