import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2025, 2051)

solar_energy = np.array([50, 65, 80, 95, 112, 130, 150, 175, 200, 230, 260, 295, 330, 370, 410, 455, 500, 550, 600, 655, 710, 770, 830, 895, 960, 1030])

fig, ax1 = plt.subplots(figsize=(12, 8))

ax1.plot(years, solar_energy, marker='o', linestyle='-', linewidth=2, color='blue')  # Applied single color

ax1.set_xlim(2024, 2051)
ax1.set_ylim(0, 1100)

plt.show()