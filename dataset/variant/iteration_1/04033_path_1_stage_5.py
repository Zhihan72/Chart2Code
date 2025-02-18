import matplotlib.pyplot as plt
import numpy as np

activities = ["Exercise", "Reading", "Watching TV", "Socializing", "Traveling", "Cooking"]
frequencies = np.array([55, 70, 45, 90, 65, 80])  # Manually shuffled
well_being_impact = np.array([70, 55, 80, 40, 75, 85])  # Manually shuffled

fig, ax1 = plt.subplots(figsize=(14, 8))

bars = ax1.barh(activities, frequencies, color='cornflowerblue', alpha=0.7)

# Remove bar annotation
# for bar in bars:
#     width = bar.get_width()
#     ax1.annotate(f'{width}',
#                 xy=(width, bar.get_y() + bar.get_height() / 2),
#                 xytext=(3, 0),
#                 textcoords="offset points",
#                 ha='left', va='center')

ax1.set_xlim(0, 100)
ax1.tick_params(axis='x', colors='cornflowerblue')
ax1.tick_params(axis='y', left=False)  # Removes y-axis ticks

ax2 = ax1.twiny()
ax2.plot(well_being_impact, activities, color='cornflowerblue', marker='o', linestyle='-', linewidth=2, markersize=10)
ax2.set_xlim(0, 100)
ax2.tick_params(axis='x', colors='cornflowerblue')

fig.tight_layout()
plt.show()