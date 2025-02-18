import matplotlib.pyplot as plt
import numpy as np

years = np.array([2017, 2018, 2019, 2020, 2021])

running = np.array([150, 175, 200, 180, 220])
cycling = np.array([100, 120, 130, 110, 140])
picnicking = np.array([80, 85, 95, 90, 100])
swimming = np.array([60, 75, 80, 60, 85])
yoga = np.array([30, 40, 50, 45, 60])

# New data series for 'Hiking' and 'Surfing'
hiking = np.array([70, 90, 100, 110, 130])
surfing = np.array([40, 55, 60, 65, 70])

# Update total participation with the new activities
total_participation = running + cycling + picnicking + swimming + yoga + hiking + surfing

fig, ax1 = plt.subplots(figsize=(12, 7))

# Updated labels including new activities
activity_labels = ['Jogging', 'Biking', 'Leisure', 'Water Sports', 'Meditation', 'Hiking', 'Surfing']
activities = [running, cycling, picnicking, swimming, yoga, hiking, surfing]
colors = ['#d62728', '#2ca02c', '#1f77b4', '#ff7f0e', '#9467bd', '#8c564b', '#e377c2']

bottom = np.zeros(len(years))

for i, (activity, color) in enumerate(zip(activities, colors)):
    ax1.bar(years, activity, bottom=bottom, label=activity_labels[i], color=color, alpha=0.7, edgecolor='black', hatch='/')
    bottom += activity

ax2 = ax1.twinx()
ax2.plot(years, total_participation, color='purple', marker='s', linestyle='-.', linewidth=2.5, label='Aggregate Participation')

ax1.set_title("Outdoor Activity Trends\n(2017-2021)", fontsize=18, weight='bold', pad=20)
ax1.set_xlabel('Calendar Year', fontsize=14)
ax1.set_ylabel('Participant Count', fontsize=14)
ax2.set_ylabel('Total Sum', fontsize=14, color='black')

ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.set_yticks(np.arange(0, 501, 50))  # Adjust range for y-axis to accommodate new data

lines_labels = [ax.get_legend_handles_labels() for ax in [ax1, ax2]]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
ax1.legend(lines, labels, loc='upper right', fontsize=11, bbox_to_anchor=(1.2, 1.05), shadow=True, borderaxespad=1.)

ax1.grid(axis='y', linestyle=':', alpha=0.4)

plt.tight_layout(rect=[0, 0, 0.85, 1])

plt.show()