import matplotlib.pyplot as plt

activities = ['Social Media', 'Entertainment', 'Online Shopping', 'Education', 'Work', 'News Reading', 'Other', 'Cloud Storage']
percentages = [28, 18, 14, 9, 9, 9, 4, 9]
new_colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6']
explode = (0, 0, 0.1, 0, 0.05, 0, 0, 0)

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    percentages, 
    colors=new_colors, 
    explode=explode, 
    autopct='%1.1f%%', 
    startangle=180, 
    pctdistance=0.9,
    wedgeprops=dict(width=0.4, edgecolor='white')
)

plt.setp(autotexts, size=12, weight="normal", color='black')
ax.legend().remove()

mean_hours = [7.0, 4.5, 3.0, 2.0, 3.5, 1.5, 1.0, 3.5]
ax2 = fig.add_axes([0.75, 0.1, 0.2, 0.3])
ax2.barh(activities, mean_hours, color=new_colors, height=0.35, linestyle='dotted')
ax2.set_xlim(0, max(mean_hours) + 1)
ax2.invert_yaxis()
ax2.set_xticks(range(0, 9, 2))
ax2.grid(True, axis='x', linestyle='--', linewidth=0.7)

ax.axis('equal')

plt.show()