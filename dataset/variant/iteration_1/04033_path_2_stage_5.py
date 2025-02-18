import matplotlib.pyplot as plt
import numpy as np

activities = ["Exercise", "Reading", "Watching TV", "Socializing", "Traveling", "Cooking"]
frequencies = np.array([55, 90, 45, 70, 65, 80])
well_being_impact = np.array([40, 70, 80, 55, 75, 85])

sorted_indices = frequencies.argsort()
activities_sorted = [activities[i] for i in sorted_indices]
frequencies_sorted = frequencies[sorted_indices]
well_being_impact_sorted = well_being_impact[sorted_indices]

fig, ax1 = plt.subplots(figsize=(14, 8))

# Create bar chart with sorted data
bars = ax1.bar(activities_sorted, frequencies_sorted, color='skyblue', alpha=0.8)

ax1.set_ylim(0, 100)
ax1.yaxis.label.set_color('skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')
ax1.grid(True, linestyle=':', alpha=0.5)

ax2 = ax1.twinx()
ax2.plot(activities_sorted, well_being_impact_sorted, color='red', marker='s', linestyle='--', linewidth=2, markersize=8)
ax2.set_ylim(0, 100)
ax2.yaxis.label.set_color('red')
ax2.tick_params(axis='y', labelcolor='red')

fig.tight_layout()
plt.show()