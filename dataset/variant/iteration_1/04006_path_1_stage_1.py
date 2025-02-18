import matplotlib.pyplot as plt
import numpy as np

years = np.array([2017, 2018, 2019, 2020, 2021])

running = np.array([150, 175, 200, 180, 220])
cycling = np.array([100, 120, 130, 110, 140])
picnicking = np.array([80, 85, 95, 90, 100])
swimming = np.array([60, 75, 80, 60, 85])
yoga = np.array([30, 40, 50, 45, 60])

total_participation = running + cycling + picnicking + swimming + yoga

fig, ax1 = plt.subplots(figsize=(12, 7))

activity_labels = ['Running', 'Cycling', 'Picnicking', 'Swimming', 'Yoga']
activities = [running, cycling, picnicking, swimming, yoga]
colors = ['#d62728', '#2ca02c', '#1f77b4', '#ff7f0e', '#9467bd']  # Colors shuffled

bottom = np.zeros(len(years))

for i, (activity, color) in enumerate(zip(activities, colors)):
    bars = ax1.bar(years, activity, bottom=bottom, label=activity_labels[i], color=color, alpha=0.7, edgecolor='black', hatch='/')  # Change in edgecolor and adding hatch styles
    bottom += activity

ax2 = ax1.twinx()
ax2.plot(years, total_participation, color='purple', marker='s', linestyle='-.', linewidth=2.5, label='Total Participation')  # Different color, marker, and linestyle

ax1.set_title("Popular Activities in MetroPark\n(2017-2021)", fontsize=18, weight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Number of Participants', fontsize=14)
ax2.set_ylabel('Total Participation', fontsize=14, color='black')

ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.set_yticks(np.arange(0, 351, 50))

lines_labels = [ax.get_legend_handles_labels() for ax in [ax1, ax2]]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
ax1.legend(lines, labels, loc='upper right', fontsize=11, bbox_to_anchor=(1.2, 1.05), shadow=True, borderaxespad=1.)  # Changed legend position, fontsize, shadow

ax1.grid(axis='y', linestyle=':', alpha=0.4)  # Changed grid line style and alpha

plt.tight_layout(rect=[0, 0, 0.85, 1])

plt.show()