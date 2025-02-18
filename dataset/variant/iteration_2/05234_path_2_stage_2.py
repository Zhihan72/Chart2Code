import matplotlib.pyplot as plt
import numpy as np

hobbies = ['Exercise', 'Cook', 'Read', 'Travel', 'Game']
hours_spent = np.array([5, 15, 7, 10, 12])
happiness_levels = np.array([70, 50, 85, 75, 90])

fig, ax = plt.subplots(figsize=(12, 8))

# Applying single color across all data groups
scatter = ax.scatter(hours_spent, happiness_levels, c='blue', s=300, edgecolor='k')

for i, hobby in enumerate(hobbies):
    ax.annotate(hobby, (hours_spent[i], happiness_levels[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=12, fontweight='bold')

m, b = np.polyfit(hours_spent, happiness_levels, 1)
ax.plot(hours_spent, m*hours_spent + b, color='gray', linewidth=2, linestyle='--', label='Trend Line')

ax.set_title('Exploring Happiness Vs. Hobby Time', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Hours per Week Engaged', fontsize=14)
ax.set_ylabel('Happiness (max 100)', fontsize=14)

ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='lower right', fontsize=12)

plt.tight_layout()
plt.show()