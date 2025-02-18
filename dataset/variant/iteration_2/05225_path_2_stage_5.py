import matplotlib.pyplot as plt

ride_names = ['Mystery Mountain', 'Cursed Ship', 'Ghostly Manor', 'Splash Lagoon']
visitor_percentage = [25, 20, 15, 10]

fig, ax = plt.subplots(figsize=(10, 7))

# Use different colors for variety
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Change wedge properties and styles
wedges, texts, autotexts = ax.pie(
    visitor_percentage,
    labels=ride_names,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    wedgeprops=dict(edgecolor='navy', linestyle='dashed', linewidth=1.5, width=0.35),
    explode=(0.05, 0.1, 0, 0),
    shadow=True
)

plt.setp(autotexts, size=14, weight="bold", color="darkblue")
plt.setp(texts, size=11, color='darkred')

plt.title('Exciting Rides for Thrill Land Visitors\nAnniversary Edition', fontsize=18, fontweight='bold', color='maroon', pad=15)

# Alter legend placement and styling
ax.legend(
    wedges,
    [f"{ride}: {percentage}%" for ride, percentage in zip(ride_names, visitor_percentage)],
    title="Top Attractions",
    loc="upper right",
    fontsize=11,
    title_fontsize=13,
    shadow=True
)

ax.set_aspect('equal')

plt.grid(linestyle=':', linewidth=0.7)

plt.tight_layout()
plt.show()