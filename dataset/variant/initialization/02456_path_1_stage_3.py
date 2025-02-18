import matplotlib.pyplot as plt

# Shortened focus area labels
focus_areas = ['Exploration', 'Mining', 'Probes', 'Bases', 'Tourism']
mission_distribution = [30, 15, 20, 25, 10]

fig, ax = plt.subplots(figsize=(9, 9))

single_color = '#66b3ff'

wedges, texts, autotexts = ax.pie(
    mission_distribution, 
    labels=focus_areas, 
    autopct='%1.1f%%', 
    startangle=90,
    colors=[single_color] * len(focus_areas),
    textprops={'fontsize': 10, 'weight': 'bold'}
)

ax.axis('equal')
ax.set_title("Missions: Focus in 2050", fontsize=15, fontweight='bold', ha='center')

plt.show()