import matplotlib.pyplot as plt

activities = [
    "Personal Development",
    "Travel & Exploration",
    "Socializing",
    "Education & Learning",
    "Health & Fitness",
    "Work & Career",
    "Leisure & Entertainment"
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
ax.set_title("Zeropolis Activity Preferences 2123", fontsize=18, fontweight='bold', color='slategray', pad=20)

ax.legend(wedges, activities, title="Activity Types", loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

plt.grid(False)  # Explicitly stating that grid is not used in a pie chart context
plt.tight_layout()
plt.show()