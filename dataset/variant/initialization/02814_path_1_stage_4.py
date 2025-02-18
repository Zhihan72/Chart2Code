import matplotlib.pyplot as plt
import numpy as np

decades = ['1970s', '1980s', '1990s', '2000s', '2010s']
solar_energy = np.array([5, 10, 15, 20, 25])
hydro_energy = np.array([8, 10, 13, 16, 20])

fig, ax = plt.subplots(figsize=(12, 8))

# Randomly altering stylistic elements
solar_color = '#FF4500'
hydro_color = '#1E90FF'

ax.fill_between(decades, solar_energy, color=solar_color, alpha=0.5, label='Solar Energy')
ax.fill_between(decades, hydro_energy, color=hydro_color, alpha=0.7, label='Hydro Energy')

ax.plot(decades, solar_energy, color=solar_color, linestyle='-.', marker='^', linewidth=2)
ax.plot(decades, hydro_energy, color=hydro_color, linestyle='-', marker='o', linewidth=2)

ax.set_xticks(decades)
ax.grid(linestyle='-', linewidth=1, alpha=0.5)

ax.legend(loc='upper left', title='Energy Sources')

plt.tight_layout()
plt.show()