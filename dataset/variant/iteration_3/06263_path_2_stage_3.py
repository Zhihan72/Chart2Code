import matplotlib.pyplot as plt

activities = ['Art Club', 'Science Club', 'Sports', 'Music Band', 'Drama Club', 'Debate']
participation_counts = [34, 45, 56, 40, 30, 20]

fig, ax1 = plt.subplots(figsize=(8, 8))

# Create a horizontal bar chart
bars = ax1.barh(activities, participation_counts, color='teal', edgecolor='black')
ax1.set_title("Student Participation in Extracurricular Activities\n2023", fontsize=16, fontweight='bold')
ax1.set_xlabel("Number of Students", fontsize=14)
ax1.set_ylabel("Activities", fontsize=14)
ax1.set_xlim(0, 60)

for bar in bars:
    xval = bar.get_width()
    ax1.text(xval + 1, bar.get_y() + bar.get_height() / 2, f'{xval}', ha='left', va='center', fontsize=12)

plt.tight_layout()
plt.show()