import matplotlib.pyplot as plt
import numpy as np

age_groups = np.array([10, 20, 30, 40, 50, 60, 70, 80])
average_steps = np.array([12000, 15500, 14500, 13000, 11000, 9000, 7000, 4000])

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(age_groups, average_steps, 's--', color='green', linestyle='--', linewidth=2.5, markersize=10,
        markerfacecolor='yellow', markeredgewidth=1.5, markeredgecolor='darkgreen', label='Average Steps')
ax.set_title("Average Daily Steps by Age", fontsize=18, fontweight='bold', pad=15)
ax.set_xlabel("Age", fontsize=14)
ax.set_ylabel("Average Steps", fontsize=14)

for i in range(age_groups.size):
    ax.annotate(f'{average_steps[i]:,.0f}', xy=(age_groups[i], average_steps[i]), xytext=(-15, 5),
                textcoords='offset points', fontsize=9, color='purple', bbox=dict(facecolor='lightblue', edgecolor='purple', pad=2))

ax.grid(False)
ax.tick_params(axis='both', which='major', labelsize=12)
ax.legend(loc='lower left', fontsize=12, frameon=False)

plt.tight_layout()
plt.show()