import matplotlib.pyplot as plt

# Data for the bar chart (number of students)
activities = ['Art Club', 'Science Club', 'Sports', 'Music Band', 'Drama Club', 'Debate']
participation_counts = [34, 45, 56, 40, 30, 20]

# Create a figure with a single subplot
fig, ax1 = plt.subplots(figsize=(8, 8))

# New set of colors
colors = ['coral', 'lightgreen', 'lightcoral', 'lightblue', 'orchid', 'khaki']

# Plotting the bar chart with new colors
bars = ax1.bar(activities, participation_counts, color=colors, edgecolor='black', width=0.6)
ax1.set_ylim(0, 60)

plt.tight_layout()
plt.show()