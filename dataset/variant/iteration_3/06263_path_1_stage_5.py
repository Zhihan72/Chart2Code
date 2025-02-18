import matplotlib.pyplot as plt

# Original data
activities = ['Art Club', 'Science Club', 'Sports', 'Music Band', 'Drama Club', 'Debate']
participation_counts = [34, 45, 56, 40, 30, 20]

# Additional data series
activities.extend(['Chess Club', 'Robotics Club', 'Photography Club'])
participation_counts.extend([25, 48, 37])

fig, ax1 = plt.subplots(figsize=(8, 8))

colors = ['coral', 'lightgreen', 'lightcoral', 'lightblue', 'orchid', 'khaki', 'slateblue', 'lightgoldenrodyellow', 'mediumseagreen']

# Updated horizontal bar chart with additional data
bars = ax1.barh(activities, participation_counts, color=colors, edgecolor='black')
ax1.set_xlim(0, 60)

plt.tight_layout()
plt.show()