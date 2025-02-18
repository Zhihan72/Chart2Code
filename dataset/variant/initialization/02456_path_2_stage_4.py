import matplotlib.pyplot as plt

exploration_areas = ['Asteroid Mining', 'Lunar Bases', 'Space Tourism', 'Interstellar Probes', 'Planetary Exploration']
mission_distribution = [15, 25, 10, 20, 30]

# Updated color scheme
new_colors = ['#ff6666', '#ffccf2', '#66ff66', '#ffb266', '#3399ff']

fig, ax = plt.subplots(figsize=(9, 9))

ax.pie(
    mission_distribution,
    labels=exploration_areas,
    autopct='%1.1f%%',
    startangle=45,
    colors=new_colors,
    textprops={'fontsize': 11, 'weight': 'normal', 'color': 'darkblue'}
)

ax.set_title("Futuristic Space Projects - 2071", fontsize=14, fontweight='medium')

plt.show()