import matplotlib.pyplot as plt

activities = ['Social Media', 'Entertainment', 'Online Shopping', 'Education', 'Work', 'News Reading', 'Other', 'Cloud Storage']
percentages = [28, 18, 14, 9, 9, 9, 4, 9]
colors = ['#87ceeb', '#c7f0c2', '#ffcc99', '#99ff99', '#66b3ff', '#ff9999', '#c2c2f0', '#ffb3e6']
explode = (0, 0, 0.1, 0, 0.05, 0, 0, 0)

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    percentages, 
    colors=colors, 
    explode=explode, 
    labels=activities, 
    autopct='%1.1f%%', 
    startangle=180, 
    pctdistance=0.9,
    wedgeprops=dict(width=0.4, edgecolor='white'),
    shadow=False
)

plt.setp(autotexts, size=12, weight="normal", color='black')
plt.setp(texts, size=11, weight='normal')
ax.legend(wedges, activities, title="Activities", loc="upper right")

# Add gridlines to the secondary chart
mean_hours = [7.0, 4.5, 3.0, 2.0, 3.5, 1.5, 1.0, 3.5]
ax2 = fig.add_axes([0.75, 0.1, 0.2, 0.3])
ax2.barh(activities, mean_hours, color=colors, height=0.35, linestyle='dotted')
ax2.set_xlim(0, max(mean_hours) + 1)
ax2.invert_yaxis()
ax2.set_xticks(range(0, 9, 2))
ax2.grid(True, axis='x', linestyle='--', linewidth=0.7)

ax.axis('equal')

plt.show()