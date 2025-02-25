import matplotlib.pyplot as plt

activities = [
    "Leisure & Entertainment", 
    "Work & Career", 
    "Health & Fitness", 
    "Education & Learning", 
    "Socializing", 
    "Travel & Exploration", 
    "Environmental Activities", 
    "Personal Development"
]

activity_proportions = [20, 15, 10, 15, 12, 10, 8, 10]

single_color = ['#66b3ff'] * len(activities)

fig, ax = plt.subplots(figsize=(10, 8))

ax.pie(
    activity_proportions, labels=activities, colors=single_color,
    autopct='%1.1f%%', startangle=90
)

plt.setp(ax.texts, size=10, weight='bold', color='navy')
plt.setp(ax.texts, size=10, color='white', weight='bold')

ax.axis('equal')
ax.set_title("Favorite Activities in Zeropolis, 2123", fontsize=16, fontweight='bold', pad=40)

plt.tight_layout()
plt.show()