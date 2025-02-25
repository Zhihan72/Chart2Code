import matplotlib.pyplot as plt

ride_names = ['Mystery Mountain', 'Cursed Ship', 'Ghostly Manor', 'Splash Lagoon']
visitor_percentage = [25, 20, 15, 10]

fig, ax = plt.subplots(figsize=(10, 7))

single_color = '#66b3ff'

wedges, texts, autotexts = ax.pie(
    visitor_percentage,
    labels=ride_names,
    autopct='%1.1f%%',
    startangle=140,
    colors=[single_color] * len(visitor_percentage),
    wedgeprops=dict(edgecolor='black', width=0.3),
    explode=(0.1, 0, 0, 0),
    shadow=True
)

plt.setp(autotexts, size=12, weight="bold", color="white")
plt.setp(texts, size=10)

plt.title('Exciting Rides for Thrill Land Visitors\nAnniversary Edition', fontsize=16, fontweight='bold', color='navy', pad=20)

ax.legend(
    wedges,
    [f"{ride}: {percentage}%" for ride, percentage in zip(ride_names, visitor_percentage)],
    title="Attractions",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=10,
    title_fontsize=12
)

ax.set_aspect('equal')

plt.tight_layout()
plt.show()