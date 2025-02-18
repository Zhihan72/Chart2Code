import matplotlib.pyplot as plt

activities = ['Social Media', 'Entertainment', 'Online Shopping', 'Education', 'Work', 'News Reading', 'Other', 'Cloud Storage']
percentages = [28, 18, 14, 9, 9, 9, 4, 9]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#c7f0c2', '#87ceeb']
explode = (0.05, 0, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    percentages, 
    colors=colors, 
    explode=explode, 
    labels=activities, 
    autopct='%1.1f%%', 
    startangle=90, 
    pctdistance=0.85,
    wedgeprops=dict(width=0.3),  # Create a hole by adjusting the width
    shadow=True
)

plt.setp(autotexts, size=10, weight="bold", color='white')
plt.setp(texts, size=10, weight='bold')
ax.legend(wedges, activities, title="Internet Activities", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
ax.set_title("2023 Global Internet Users' Activity Distribution", fontsize=14, weight='bold', pad=20)

# Secondary subplot
mean_hours = [7.0, 4.5, 3.0, 2.0, 3.5, 1.5, 1.0, 3.5]
ax2 = fig.add_axes([0.8, 0.1, 0.15, 0.3])
ax2.barh(activities, mean_hours, color=colors, edgecolor='black', height=0.5)
ax2.set_title('Mean Time (hrs/week)', fontsize=10)
ax2.set_xlim(0, max(mean_hours) + 1)
ax2.invert_yaxis()
ax2.set_xticks([])

ax.axis('equal')

plt.show()