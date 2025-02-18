import matplotlib.pyplot as plt

activities = ['Art Club', 'Science Club', 'Sports', 'Music Band', 'Drama Club', 'Debate']
participation_counts = [34, 45, 56, 40, 30, 20]

fig, ax1 = plt.subplots(figsize=(8, 8))

colors = ['coral', 'lightgreen', 'lightcoral', 'lightblue', 'orchid', 'khaki']

# Convert bar chart to horizontal bar chart
bars = ax1.barh(activities, participation_counts, color=colors, edgecolor='black')
ax1.set_xlim(0, 60)  # Adjust the x-limits for horizontal bar chart

plt.tight_layout()
plt.show()