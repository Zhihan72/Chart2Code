import matplotlib.pyplot as plt

ride_names = ['Sky Drop', 'Bumper Cars', 'Safari Adventure', 'Haunted Mansion', 'Water Rapids', 'Pirate Ship', 'Dragon Coaster']
visitor_percentage = [12, 10, 25, 10, 8, 15, 20]
single_color = ['#911eb4']  # Use a single color consistently for all pie slices

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    visitor_percentage,
    labels=ride_names,
    autopct='%1.0f%%',
    startangle=90,
    colors=single_color * len(ride_names),  # Apply the same color to all slices
    wedgeprops=dict(edgecolor='gray', linestyle='--'),
    explode=(0, 0.2, 0, 0.2, 0, 0, 0.2),
    shadow=False
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

plt.setp(autotexts, size=10, weight="normal", color="black")
plt.setp(texts, size=11)

plt.title('Popular Rides at Theme Park', fontsize=15, fontweight='normal', color='darkgreen', pad=20)

ax.legend(
    wedges, 
    ride_names, 
    title="Attraction Names", 
    loc="upper right", 
    bbox_to_anchor=(1, 1),
    fontsize=12,
    title_fontsize=13
)

ax.set_aspect('equal')

plt.show()