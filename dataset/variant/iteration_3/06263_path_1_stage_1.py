import matplotlib.pyplot as plt
import numpy as np

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
ax1.set_ylim(0, 60)

# Plotting the line chart on the second subplot
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A1FF33', '#5733FF']
for idx, (club, counts) in enumerate(seasonal_trends.items()):
    ax2.plot(seasons, counts, color=colors[idx], marker='o', linestyle='--', linewidth=2, markersize=8)

ax2.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to fit and show the plot
plt.tight_layout()
plt.show()