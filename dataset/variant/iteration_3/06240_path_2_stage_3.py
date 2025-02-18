import matplotlib.pyplot as plt
import numpy as np

missions = [
    'Moon Landing - Apollo 11',
    'Mars Rover - Curiosity',
    'International Space Station (ISS)',
    'Voyager Probes',
    'Hubble Space Telescope',
    'SpaceX Falcon 9 Launch',
    'Rosetta Comet Mission',
    'New Horizons Pluto Flyby',
    'Galileo Jupiter Mission',
    'James Webb Space Telescope',
    'Imaginary Mission - Alpha Centauri',
    'Fictional Endeavor - Andromeda Galaxy'
]

votes = np.array([850, 760, 900, 650, 715, 680, 620, 690, 640, 780, 500, 450])

# Create a pie chart as a donut chart (ring)
fig, ax = plt.subplots(figsize=(10, 10))
ax.pie(votes, labels=missions, colors=['#e6194b', '#3cb44b', '#ffe119', '#f58231', '#911eb4', 
                                        '#46f0f0', '#f032e6', '#d2f53c', '#fabebe', '#008080', 
                                        '#e6beff', '#9a6324'], autopct='%1.1f%%', startangle=140, counterclock=False, wedgeprops=dict(width=0.3))

ax.set_title("Global Popularity of Space Exploration Missions\n(Votes in Thousands)", fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()