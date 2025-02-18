import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# A school is evaluating the participation of its students in various extracurricular activities over the past year.
# The data showcases the number of students participating in each activity, and the trend over the seasons.

# Data for the bar chart (number of students)
activities = ['Art Club', 'Science Club', 'Sports', 'Music Band', 'Drama Club', 'Debate']
participation_counts = [34, 45, 56, 40, 30, 20]

# Additional data for the line chart (seasonal participation trends)
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
seasonal_trends = {
    'Art Club': [30, 25, 40, 42],
    'Science Club': [38, 48, 45, 50],
    'Sports': [50, 60, 55, 58],
    'Music Band': [35, 40, 42, 38],
    'Drama Club': [25, 20, 30, 35],
    'Debate': [20, 18, 22, 20]
}

# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Plotting the bar chart on the first subplot
bars = ax1.bar(activities, participation_counts, color='skyblue', edgecolor='black', width=0.6)
ax1.set_title("Student Participation in Extracurricular Activities\n2023", fontsize=16, fontweight='bold')
ax1.set_xlabel("Activities", fontsize=14)
ax1.set_ylabel("Number of Students", fontsize=14)
ax1.set_ylim(0, 60)

# Annotating the bar chart
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 1, f'{yval}', ha='center', va='bottom', fontsize=12)

# Plotting the line chart on the second subplot
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A1FF33', '#5733FF']
for idx, (club, counts) in enumerate(seasonal_trends.items()):
    ax2.plot(seasons, counts, label=club, color=colors[idx], marker='o', linestyle='--', linewidth=2, markersize=8)

ax2.set_title("Seasonal Trends of Extracurricular Participation\n2023", fontsize=16, fontweight='bold')
ax2.set_xlabel("Seasons", fontsize=14)
ax2.set_ylabel("Number of Students", fontsize=14)
ax2.legend(title="Activities", fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to fit and show the plot
plt.tight_layout()
plt.show()