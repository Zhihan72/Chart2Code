import matplotlib.pyplot as plt

ride_names = ['Dragon Coaster', 'Pirate Ship', 'Haunted Mansion', 'Water Rapids']
visitor_percentage = [25, 20, 15, 10]

fig, ax = plt.subplots(figsize=(10, 7))

# All slices will use the same color
single_color = '#66b3ff'

wedges, texts, autotexts = ax.pie(
    visitor_percentage,
    labels=ride_names,
    autopct='%1.1f%%',
    startangle=140,
    colors=[single_color] * len(visitor_percentage),  # Apply the single color to all slices
    wedgeprops=dict(edgecolor='black'),
    explode=(0.1, 0, 0, 0),
    shadow=True
)

plt.setp(autotexts, size=12, weight="bold", color="white")
plt.setp(texts, size=10)

plt.title('Visitor Preferences for AdventureLand Rides\n10th Anniversary Special', fontsize=16, fontweight='bold', color='navy', pad=20)

ax.legend(
    wedges,
    [f"{ride}: {percentage}%" for ride, percentage in zip(ride_names, visitor_percentage)],
    title="Rides",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=10,
    title_fontsize=12
)

ax.set_aspect('equal')

plt.tight_layout()
plt.show()