import numpy as np
import matplotlib.pyplot as plt

years = np.array([2017, 2018, 2019, 2020, 2021])
group_a_scores = np.array([76, 78, 82, 85, 87])
group_c_scores = np.array([70, 72, 74, 78, 80])

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(years, group_a_scores, marker='o', linestyle='-', linewidth=2, markersize=6, color='green')
ax.plot(years, group_c_scores, marker='^', linestyle='-.', linewidth=2, markersize=6, color='green')

ax.set_title('Performance Trend of Groups (2017-2021)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=12)
ax.set_ylabel('Score Average', fontsize=12)

ax.set_xticks(years)
ax.set_yticks(np.arange(60, 90, 5))

# Remove grid
# ax.grid(True, linestyle='--', alpha=0.7)

# Remove legend
# ax.legend(loc='lower right', title='Participants')

# Remove annotations
# for i in range(len(years)):
#     ax.annotate(f'{group_a_scores[i]}%', xy=(years[i], group_a_scores[i]), textcoords="offset points", xytext=(0, 10), ha='center', color='green')
#     ax.annotate(f'{group_c_scores[i]}%', xy=(years[i], group_c_scores[i]), textcoords="offset points", xytext=(0, 10), ha='center', color='green')

plt.tight_layout()
plt.show()