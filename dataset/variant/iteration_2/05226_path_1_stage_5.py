import matplotlib.pyplot as plt
import numpy as np

# Original data
subjects = ["Sports", "Music", "Art", "Sci Club", "Comp Club", "Dance", "Drama", "Chess", "Photography"]
hours_spent = np.array([120, 90, 80, 110, 95, 85, 100, 70, 75])

# Sort the data based on hours_spent in descending order
sorted_indices = np.argsort(-hours_spent)
sorted_subjects = [subjects[i] for i in sorted_indices]
sorted_hours_spent = hours_spent[sorted_indices]

fig, ax = plt.subplots(figsize=(12, 7))

bar_positions = np.arange(len(sorted_subjects))
bars = ax.bar(bar_positions, sorted_hours_spent, color=['#5f9ea0', '#8a2be2', '#deb887', '#ff1493', '#7fff00', '#dc143c', '#00ced1', '#4169e1', '#add8e6'])

ax.set_title("2023 Student Extracurricular Hours", fontsize=16, fontweight='bold')
ax.set_xlabel("Activities", fontsize=14)
ax.set_ylabel("Hours", fontsize=14)

ax.set_xticks(bar_positions)
ax.set_xticklabels(sorted_subjects, rotation=30, ha='right', fontsize=12)

for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}', 
                xy=(bar.get_x() + bar.get_width() / 2, height), 
                xytext=(0, 3), 
                textcoords="offset points",
                ha='center', va='bottom', fontsize=11, color='black')

plt.tight_layout()

plt.show()