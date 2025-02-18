import matplotlib.pyplot as plt
import numpy as np

# Updated subjects with additional activities
subjects = ["Sports", "Music", "Art", "Sci Club", "Comp Club", "Dance", "Drama", "Chess", "Photography"]
# Updated hours_spent to include the new activities
hours_spent = np.array([120, 90, 80, 110, 95, 85, 100, 70, 75])

fig, ax = plt.subplots(figsize=(12, 7))

bar_positions = np.arange(len(subjects))
bars = ax.bar(bar_positions, hours_spent, color=['#6a0dad', '#ff6347', '#4682b4', '#3cb371', '#ff69b4', '#ffa500', '#9370db', '#ff4500', '#ffd700'], edgecolor='black', linewidth=1)

# Adjusted title and axis labels
ax.set_title("2023 Student Extracurricular Hours", fontsize=16, fontweight='bold')
ax.set_xlabel("Activities", fontsize=14)
ax.set_ylabel("Hours", fontsize=14)

ax.set_xticks(bar_positions)
ax.set_xticklabels(subjects, rotation=30, ha='right', fontsize=12)

# Annotating with hours
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}', 
                xy=(bar.get_x() + bar.get_width() / 2, height), 
                xytext=(0, 3), 
                textcoords="offset points",
                ha='center', va='bottom', fontsize=11, color='black')

# Updated legend to include new activities
ax.legend(bars, [
    'Sports',
    'Music',
    'Art',
    'Sci Experiments',
    'Coding & Tech',
    'Dance',
    'Drama',
    'Chess',
    'Photography'
], title='Activities', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10, title_fontsize=12)

ax.yaxis.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()

plt.show()