import matplotlib.pyplot as plt

focus_areas = ['Planetary Exploration', 'Asteroid Mining', 'Interstellar Probes', 'Lunar Bases', 'Space Tourism']
mission_distribution = [30, 15, 20, 25, 10]

fig, ax = plt.subplots(figsize=(9, 9))

# Using a single color for all wedges
single_color = '#66b3ff'  # Chose one of the existing colors for uniformity

wedges, texts, autotexts = ax.pie(
    mission_distribution, 
    labels=focus_areas, 
    autopct='%1.1f%%', 
    startangle=90,
    colors=[single_color] * len(focus_areas),  # Apply the single color consistently
    textprops={'fontsize': 10, 'weight': 'bold'}
)

ax.axis('equal')
ax.set_title("Space Exploration Missions:\nFocus Areas in 2050", fontsize=15, fontweight='bold', ha='center')

plt.show()