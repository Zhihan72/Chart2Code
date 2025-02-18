import matplotlib.pyplot as plt

# Altered activity names and title
activities = [
    "Person Dev",
    "Travel Fun",
    "Social Buzz",
    "Learn & Grow",
    "Fitness Time",
    "Career Path",
    "Fun & Games"
]

activity_proportions = [10, 10, 12, 15, 10, 15, 20]

colors = ['#DEB887', '#FF6347', '#40E0D0', '#4B0082', '#ADFF2F', '#4682B4', '#FFD700']

explode = (0, 0.1, 0, 0, 0.1, 0, 0.1)

fig, ax = plt.subplots(figsize=(8, 10))

wedges, texts, autotexts = ax.pie(
    activity_proportions, labels=activities, colors=colors, explode=explode,
    autopct='%1.1f%%', startangle=180, pctdistance=0.75, shadow=True
)

plt.setp(texts, size=11, weight='bold', color='darkred')
plt.setp(autotexts, size=11, color='black', weight='bold')

ax.axis('equal')
ax.set_title("Fun Activity Preferences 2222", fontsize=18, fontweight='bold', color='slategray', pad=20)

ax.legend(wedges, activities, title="Type of Activities", loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

plt.grid(False)
plt.tight_layout()
plt.show()