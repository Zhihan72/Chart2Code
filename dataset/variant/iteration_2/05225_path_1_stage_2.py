import matplotlib.pyplot as plt

ride_names = ['Dragon Coaster', 'Pirate Ship', 'Haunted Mansion', 'Safari Adventure', 'Water Rapids', 'Sky Drop', 'Bumper Cars']
visitor_percentage = [20, 15, 10, 25, 8, 12, 10]
colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0']

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    visitor_percentage,
    labels=ride_names,
    autopct='%1.0f%%',
    startangle=90,
    colors=colors,
    wedgeprops=dict(edgecolor='gray', linestyle='--'),
    explode=(0, 0.2, 0, 0.2, 0, 0, 0.2),
    shadow=False
)

plt.setp(autotexts, size=10, weight="normal", color="black")
plt.setp(texts, size=11)

plt.title('AdventureLand Ride Popularity', fontsize=15, fontweight='normal', color='darkgreen', pad=20)

ax.legend(
    wedges, 
    ride_names, 
    title="Ride Names", 
    loc="upper right", 
    bbox_to_anchor=(1, 1),
    fontsize=12,
    title_fontsize=13
)

ax.set_aspect('equal')

plt.show()