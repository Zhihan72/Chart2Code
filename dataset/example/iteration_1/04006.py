import matplotlib.pyplot as plt
import numpy as np

# Backstory: A fictional urban park with various recreational activities over the years has seen different levels of popularity. This script showcases the trends in these activities from 2017 to 2021 through a bar chart.

# Define years
years = np.array([2017, 2018, 2019, 2020, 2021])

# Activities in the park (Number of participants)
running = np.array([150, 175, 200, 180, 220])
cycling = np.array([100, 120, 130, 110, 140])
picnicking = np.array([80, 85, 95, 90, 100])
swimming = np.array([60, 75, 80, 60, 85])
yoga = np.array([30, 40, 50, 45, 60])

# Calculate total participation per year
total_participation = running + cycling + picnicking + swimming + yoga

# Create figure and axis
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot stacked bar chart
activity_labels = ['Running', 'Cycling', 'Picnicking', 'Swimming', 'Yoga']
activities = [running, cycling, picnicking, swimming, yoga]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

bottom = np.zeros(len(years))

for i, (activity, color) in enumerate(zip(activities, colors)):
    bars = ax1.bar(years, activity, bottom=bottom, label=activity_labels[i], color=color, alpha=0.8, edgecolor='grey')
    bottom += activity

# Create a secondary axis for total participation line plot
ax2 = ax1.twinx()
ax2.plot(years, total_participation, color='black', marker='o', linestyle='-', linewidth=2, label='Total Participation')

# Title and labels
ax1.set_title("Popular Activities in MetroPark\n(2017-2021)", fontsize=18, weight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Number of Participants', fontsize=14)
ax2.set_ylabel('Total Participation', fontsize=14, color='black')

# Customize ticks
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.set_yticks(np.arange(0, 351, 50))

# Add legend
lines_labels = [ax.get_legend_handles_labels() for ax in [ax1, ax2]]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
ax1.legend(lines, labels, loc='upper left', fontsize=12, bbox_to_anchor=(1.05, 1), borderaxespad=0.)

# Adding grid for clarity
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Tight layout to prevent overlay clashing
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Show plot
plt.show()