import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the shift in educational tool usage across a decade
# This chart shows the transition in the types of educational tools used by students from 2010 to 2020
# Emphasis has shifted from traditional books to digital tools

# Define the years
years = np.arange(2010, 2021)

# Define the use of different educational tools in hours of usage per week
books = [20, 19, 18, 18, 17, 16, 15, 14, 12, 10, 8]
online_courses = [2, 3, 4, 5, 7, 8, 10, 12, 14, 16, 18]
educational_apps = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 20]
videos = [5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17]
tutoring = [10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 4]

# Plotting the stacked area chart
plt.figure(figsize=(14, 8))

# Create stacked area plot
plt.stackplot(years, books, online_courses, educational_apps, videos, tutoring,
              labels=['Books', 'Online Courses', 'Educational Apps', 'Videos', 'Tutoring'],
              colors=['#ff9999', '#66b2ff', '#99ff99', '#ffcc99', '#c2c2f0'], alpha=0.8)

# Add title and labels
plt.title("Shift in Educational Tool Usage by Students (2010 to 2020)", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Weekly Hours of Usage", fontsize=12)

# Add legend
plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0., title='Educational Tools')

# Add grid for better readability
plt.grid(linestyle='--', alpha=0.7)

# Annotate significant trends
plt.annotate('Rise of Educational Apps', xy=(2015, 20), xytext=(2012, 60),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, backgroundcolor='w')

plt.annotate('Decline of Books', xy=(2016, 16), xytext=(2013, 50),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, backgroundcolor='w')

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()