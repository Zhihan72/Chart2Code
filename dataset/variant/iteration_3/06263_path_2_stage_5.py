import matplotlib.pyplot as plt

activities = ['Art Club', 'Science Club', 'Sports', 'Music Band', 'Drama Club']
participation_counts = [34, 45, 56, 40, 30]

fig, ax1 = plt.subplots(figsize=(8, 8))

# Changed the bar color and edge color
bars = ax1.barh(activities, participation_counts, color='salmon', edgecolor='navy')
# Altered the title and font size
ax1.set_title("Extracurricular Activities Participation\nYear 2023", fontsize=14, fontweight='light')
# Changed the x-axis label font size
ax1.set_xlabel("Students Enrolled", fontsize=12)
ax1.set_ylabel("Activities", fontsize=14)  # Keep the same
# Adjusted axis limits
ax1.set_xlim(10, 70)

# Included grid lines
ax1.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.7)

# Adding text at the end of each bar
for bar in bars:
    xval = bar.get_width()
    ax1.text(xval + 1, bar.get_y() + bar.get_height() / 2, f'{xval}', ha='left', va='center', fontsize=10)

plt.tight_layout()  # Ensures the layout is compact
plt.show()