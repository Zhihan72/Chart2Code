import matplotlib.pyplot as plt

activities = ['Art Club', 'Science Club', 'Sports', 'Music Band', 'Drama Club', 'Debate']
participation_counts = [34, 45, 56, 40, 30, 20]

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
seasonal_trends = {
    'Art Club': [30, 25, 40, 42],
    'Science Club': [38, 48, 45, 50],
    'Sports': [50, 60, 55, 58],
    'Music Band': [35, 40, 42, 38],
    'Drama Club': [25, 20, 30, 35],
    'Debate': [20, 18, 22, 20]
}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Use a single color for bars
bars = ax1.bar(activities, participation_counts, color='teal', edgecolor='black', width=0.6)
ax1.set_title("Student Participation in Extracurricular Activities\n2023", fontsize=16, fontweight='bold')
ax1.set_xlabel("Activities", fontsize=14)
ax1.set_ylabel("Number of Students", fontsize=14)
ax1.set_ylim(0, 60)

for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 1, f'{yval}', ha='center', va='bottom', fontsize=12)

# Use a single color for lines
for club, counts in seasonal_trends.items():
    ax2.plot(seasons, counts, label=club, color='teal', marker='o', linestyle='--', linewidth=2, markersize=8)

ax2.set_title("Seasonal Trends of Extracurricular Participation\n2023", fontsize=16, fontweight='bold')
ax2.set_xlabel("Seasons", fontsize=14)
ax2.set_ylabel("Number of Students", fontsize=14)
ax2.legend(title="Activities", fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()