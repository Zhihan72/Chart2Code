import matplotlib.pyplot as plt

# Altered textual elements
exploration_areas = ['Asteroid Mining', 'Lunar Bases', 'Space Tourism', 'Interstellar Probes', 'Planetary Exploration']
mission_distribution = [15, 25, 10, 20, 30]

colors = ['#ff9999', '#c2c2f0', '#99ff99', '#ffcc99', '#66b3ff']

fig, ax = plt.subplots(figsize=(9, 9))

explode = (0.1, 0, 0, 0, 0)

# Randomized textual elements: labels, percentage positions, and title
wedges, texts, autotexts = ax.pie(
    mission_distribution,
    labels=exploration_areas,
    autopct='%1.1f%%',
    startangle=45,
    colors=colors,
    explode=explode,
    textprops={'fontsize': 11, 'weight': 'normal', 'color': 'darkblue'},
    pctdistance=0.6
)

centre_circle = plt.Circle((0, 0), 0.75, fc='lightgrey')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

ax.set_title("Futuristic Space Projects - 2071", fontsize=14, fontweight='medium')

plt.grid(True, linestyle='--', linewidth=0.5)

plt.show()