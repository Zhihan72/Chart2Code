import matplotlib.pyplot as plt
import numpy as np

subjects = ["Art", "Dance", "Drama", "Music", "Computer Club", "Science Club", "Sports"]
hours_spent = np.array([80, 85, 100, 90, 95, 110, 120])

fig, ax = plt.subplots(figsize=(12, 7))

bar_positions = np.arange(len(subjects))
bars = ax.bar(bar_positions, hours_spent, color='#4682b4', edgecolor='black', linewidth=1)

ax.set_xlabel('Extracurricular Activities', fontsize=14)
ax.set_ylabel('Total Hours Spent', fontsize=14)

ax.set_xticks(bar_positions)
ax.set_xticklabels(subjects, rotation=30, ha='right', fontsize=12)

for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height} hours', 
                xy=(bar.get_x() + bar.get_width() / 2, height), 
                xytext=(0, 3), 
                textcoords="offset points",
                ha='center', va='bottom', fontsize=11, color='black')

plt.tight_layout()
plt.show()