import matplotlib.pyplot as plt
import numpy as np

decades = ['1970s', '1980s', '1990s', '2000s', '2010s']
solar_energy = np.array([5, 10, 15, 20, 25])
hydro_energy = np.array([8, 10, 13, 16, 20])

fig, ax = plt.subplots(figsize=(12, 8))
consistent_color = '#FFD700'

ax.fill_between(decades, solar_energy, color=consistent_color, alpha=0.6)
ax.fill_between(decades, hydro_energy, color=consistent_color, alpha=0.6)

ax.plot(decades, solar_energy, color=consistent_color, linewidth=2)
ax.plot(decades, hydro_energy, color=consistent_color, linewidth=2)

ax.set_xticks(decades)
ax.grid(linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()