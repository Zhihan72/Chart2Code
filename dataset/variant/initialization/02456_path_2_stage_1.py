import matplotlib.pyplot as plt

focus_areas = ['Planetary Exploration', 'Asteroid Mining', 'Interstellar Probes', 'Lunar Bases', 'Space Tourism']
mission_distribution = [30, 15, 20, 25, 10]

colors = ['#66b3ff', '#ff9999', '#ffcc99', '#c2c2f0', '#99ff99']

fig, ax = plt.subplots(figsize=(9, 9))

explode = (0, 0.1, 0, 0, 0)

wedges, texts, autotexts = ax.pie(
    mission_distribution,
    labels=focus_areas,
    autopct='%1.1f%%',
    startangle=45,
    colors=colors,
    explode=explode,
    textprops={'fontsize': 11, 'weight': 'normal', 'color': 'darkblue'},
    pctdistance=0.7
)

centre_circle = plt.Circle((0, 0), 0.75, fc='lightgrey')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

ax.set_title("Space Exploration Missions - 2050", fontsize=14, fontweight='medium')

plt.grid(True, linestyle='--', linewidth=0.5)

plt.show()