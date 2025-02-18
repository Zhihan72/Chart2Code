import matplotlib.pyplot as plt

activities = ['Art Club', 'Science Club', 'Sports', 'Music Band', 'Drama Club', 'Debate']
participation_counts = [34, 45, 56, 40, 30, 20]

fig, ax1 = plt.subplots(figsize=(8, 8))

# Use a single color for bars
bars = ax1.bar(activities, participation_counts, color='teal', edgecolor='black', width=0.6)
ax1.set_title("Student Participation in Extracurricular Activities\n2023", fontsize=16, fontweight='bold')
ax1.set_xlabel("Activities", fontsize=14)
ax1.set_ylabel("Number of Students", fontsize=14)
ax1.set_ylim(0, 60)

for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 1, f'{yval}', ha='center', va='bottom', fontsize=12)

plt.tight_layout()
plt.show()