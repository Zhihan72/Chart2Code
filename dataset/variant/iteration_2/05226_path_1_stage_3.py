import matplotlib.pyplot as plt
import numpy as np

subjects = ["Sports", "Music", "Art", "Sci Club", "Comp Club", "Dance", "Drama", "Chess", "Photography"]
hours_spent = np.array([120, 90, 80, 110, 95, 85, 100, 70, 75])

fig, ax = plt.subplots(figsize=(12, 7))

bar_positions = np.arange(len(subjects))
bars = ax.bar(bar_positions, hours_spent, color=['#6a0dad', '#ff6347', '#4682b4', '#3cb371', '#ff69b4', '#ffa500', '#9370db', '#ff4500', '#ffd700'])

ax.set_title("2023 Student Extracurricular Hours", fontsize=16, fontweight='bold')
ax.set_xlabel("Activities", fontsize=14)
ax.set_ylabel("Hours", fontsize=14)

ax.set_xticks(bar_positions)
ax.set_xticklabels(subjects, rotation=30, ha='right', fontsize=12)

for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}', 
                xy=(bar.get_x() + bar.get_width() / 2, height), 
                xytext=(0, 3), 
                textcoords="offset points",
                ha='center', va='bottom', fontsize=11, color='black')

plt.tight_layout()

plt.show()