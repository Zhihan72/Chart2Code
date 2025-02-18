import matplotlib.pyplot as plt

activities = [
    "Leisure & Entertainment", 
    "Work & Career", 
    "Health & Fitness", 
    "Education & Learning", 
    "Socializing", 
    "Travel & Exploration", 
    "Personal Development"
]

activity_proportions = [20, 15, 10, 15, 12, 10, 10]

colors = ['#4B0082', '#FF6347', '#4682B4', '#FFD700', '#ADFF2F', '#DEB887', '#40E0D0']

explode = (0.1, 0, 0.1, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 8))

wedges, texts, autotexts = ax.pie(
    activity_proportions, labels=activities, colors=colors, explode=explode,
    autopct='%1.1f%%', startangle=90, pctdistance=0.85, shadow=True
)

plt.setp(texts, size=10, weight='bold', color='navy')
plt.setp(autotexts, size=10, color='white', weight='bold')

ax.axis('equal')
ax.set_title("Favorite Activities in Zeropolis, 2123", fontsize=16, fontweight='bold', pad=40)

ax.legend(wedges, activities, title="Activities", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)

plt.tight_layout()
plt.show()