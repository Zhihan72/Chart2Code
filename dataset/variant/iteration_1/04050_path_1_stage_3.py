import numpy as np
import matplotlib.pyplot as plt

years = np.array([2017, 2018, 2019, 2020, 2021])
group_a_scores = np.array([76, 78, 82, 85, 87])
group_b_scores = np.array([65, 68, 70, 75, 78])
group_c_scores = np.array([70, 72, 74, 78, 80])

fig, ax = plt.subplots(figsize=(10, 6))

# Plot lines without stylistic elements
ax.plot(years, group_a_scores, marker='o', linestyle='-', linewidth=2, markersize=6, color='blue')
ax.plot(years, group_b_scores, marker='s', linestyle='--', linewidth=2, markersize=6, color='blue')
ax.plot(years, group_c_scores, marker='^', linestyle='-.', linewidth=2, markersize=6, color='blue')

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Avg Score', fontsize=12)

ax.set_xticks(years)
ax.set_yticks(np.arange(60, 90, 5))

# Remove grids and legend
for i in range(len(years)):
    ax.annotate(f'{group_a_scores[i]}', xy=(years[i], group_a_scores[i]), textcoords="offset points", xytext=(0, 10), ha='center', color='blue')
    ax.annotate(f'{group_b_scores[i]}', xy=(years[i], group_b_scores[i]), textcoords="offset points", xytext=(0, 10), ha='center', color='blue')
    ax.annotate(f'{group_c_scores[i]}', xy=(years[i], group_c_scores[i]), textcoords="offset points", xytext=(0, 10), ha='center', color='blue')

# Remove borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()