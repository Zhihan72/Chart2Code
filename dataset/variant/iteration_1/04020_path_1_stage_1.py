import matplotlib.pyplot as plt
import numpy as np

# Years from 2023 to 2028
years = np.arange(2023, 2029)

# Subjects and their engagement levels over the years (in percentage)
math_engagement = np.array([70, 72, 75, 78, 80, 82])
science_engagement = np.array([65, 67, 70, 73, 75, 78])
literature_engagement = np.array([55, 58, 60, 62, 65, 67])

# Creating a 1x1 figure for line plots with differentiated lines and legends
fig, ax = plt.subplots(figsize=(12, 6))

# Plotting the engagement data for each subject
ax.plot(years, math_engagement, marker='o', linestyle='-', color='#1f77b4', label='Math')
ax.plot(years, science_engagement, marker='s', linestyle='--', color='#ff7f0e', label='Science')
ax.plot(years, literature_engagement, marker='^', linestyle='-.', color='#2ca02c', label='Literature')

# Titles and Labels
ax.set_title("Virtual Learning Engagement in Schools (2023-2028)\nMonitoring Student Engagement in Various Subjects", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Student Engagement (%)", fontsize=14)

# Adding legends
ax.legend(title="Subjects", loc='lower right', fontsize=12)

# Grid lines for easier readability
ax.grid(True, linestyle='--', alpha=0.7)

# Ensuring no overlapping of the text in the chart
plt.tight_layout()

# Display the plot
plt.show()