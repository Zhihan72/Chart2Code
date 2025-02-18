import matplotlib.pyplot as plt
import numpy as np

subjects = ["Art", "Dance", "Drama", "Music", "Computer Club", "Science Club", "Sports"]
hours_spent = np.array([80, 85, 100, 90, 95, 110, 120])

fig, ax = plt.subplots(figsize=(12, 7))

# Using a single color for all bars
bar_positions = np.arange(len(subjects))
bars = ax.bar(bar_positions, hours_spent, color='#4682b4', edgecolor='black', linewidth=1)

ax.set_title('2023 Secondary School Students\' Time Spent on Extracurricular Activities', fontsize=16, fontweight='bold')
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

# Update legend to reflect single color
ax.legend([bars[0]], [
    'Time spent on various extracurricular activities'
], title='Activity Description', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10, title_fontsize=12)

ax.yaxis.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()