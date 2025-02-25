import matplotlib.pyplot as plt

# Randomly altered textual elements
activities = [
    "Wellness Pursuits", 
    "Professional Journey", 
    "Physical Wellbeing", 
    "Knowledge Expansion", 
    "Connecting with People", 
    "Journey & Adventure", 
    "Self Growth"
]

activity_proportions = [20, 15, 10, 15, 12, 10, 10]

single_color = ['#66b3ff'] * len(activities)

fig, ax = plt.subplots(figsize=(10, 8))

ax.pie(
    activity_proportions, labels=activities, colors=single_color,
    autopct='%1.1f%%', startangle=90
)

plt.setp(ax.texts, size=10, weight='bold', color='navy')
plt.setp(ax.texts, size=10, color='white', weight='bold')

ax.axis('equal')
ax.set_title("Popular Pastimes in Futurama, 2123", fontsize=16, fontweight='bold', pad=40)

plt.tight_layout()
plt.show()