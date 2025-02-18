import matplotlib.pyplot as plt
import numpy as np

# Data for average daily physical activity levels (in minutes)
age_groups = ["Children", "Teenagers", "Adults", "Seniors"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
activity_data = np.array([
    [70, 60, 80, 40, 50, 55, 45],  # Children (shuffle)
    [60, 30, 65, 50, 45, 35, 40],  # Teenagers (shuffle)
    [35, 25, 40, 50, 30, 45, 35],  # Adults (shuffle)
    [15, 25, 20, 30, 35, 25, 20]   # Seniors (shuffle)
])

stacking_order = [activity_data[0], -activity_data[1], activity_data[2], -activity_data[3]]

fig, ax = plt.subplots(figsize=(14, 8))

for i, data in enumerate(stacking_order):
    ax.bar(days_of_week, data, label=age_groups[i],
           bottom=np.sum(stacking_order[:i], axis=0) if i % 2 == 0 else -np.sum(np.abs(stacking_order[:i]), axis=0), 
           color='blue')

ax.set_xlabel('Day of the Week', fontsize=14)
ax.set_ylabel('Diverging Average Daily Activity (Minutes)', fontsize=14)
ax.set_title('Diverging Physical Activity Levels Across Different Age Groups', fontsize=16, fontweight='bold')
ax.legend(title='Age Groups', fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig("diverging_weekly_activity_levels.png")
plt.show()