import matplotlib.pyplot as plt
import numpy as np

age_groups = np.array(['20-30', '31-40', '41-50', '51-60', '10-20'])
physical_activity_level = np.array([45, 60, 55, 40, 30])
happiness_index = np.array([80, 50, 70, 85, 65])

# Sort indices based on the physical activity level in ascending order
sorted_indices = physical_activity_level.argsort()

sorted_age_groups = age_groups[sorted_indices]
sorted_physical_activity_level = physical_activity_level[sorted_indices]
sorted_happiness_index = happiness_index[sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.bar(sorted_age_groups, sorted_physical_activity_level, color='c', edgecolor='black', alpha=0.8)

ax.set_xlabel('Age Groups', fontsize=14, fontweight='semibold')
ax.set_ylabel('Activity Minutes Per Day', fontsize=14, fontweight='semibold')
ax.set_title('Sorted Analysis of Activity by Age Groups', fontsize=16, fontweight='bold', pad=20)

# Adding data labels on top of each bar
for bar, height in zip(bars, sorted_physical_activity_level):
    ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points", ha='center', fontsize=9)

plt.tight_layout()
plt.show()