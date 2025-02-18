import matplotlib.pyplot as plt

exploration_areas = ['Asteroid Mining', 'Lunar Bases', 'Space Tourism', 'Interstellar Probes', 'Planetary Exploration']
mission_distribution = [15, 25, 10, 20, 30]

colors = ['#ff9999', '#c2c2f0', '#99ff99', '#ffcc99', '#66b3ff']

fig, ax = plt.subplots(figsize=(9, 9))

# Base pie chart without the exploded section and the center circle
ax.pie(
    mission_distribution,
    labels=exploration_areas,
    autopct='%1.1f%%',
    startangle=45,
    colors=colors,
    textprops={'fontsize': 11, 'weight': 'normal', 'color': 'darkblue'}
)

ax.set_title("Futuristic Space Projects - 2071", fontsize=14, fontweight='medium')

plt.show()