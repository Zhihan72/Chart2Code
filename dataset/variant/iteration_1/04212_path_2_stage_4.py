import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2100, 2115)

red_dwarf = np.array([10, 15, 25, 35, 50, 70, 90, 110, 130, 150, 170, 200, 230, 260, 300])
yellow_dwarf = np.array([20, 28, 35, 45, 60, 80, 105, 130, 160, 190, 220, 250, 285, 320, 360])
blue_giant = np.array([5, 10, 17, 25, 35, 50, 65, 80, 95, 110, 130, 150, 170, 190, 210])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, red_dwarf, yellow_dwarf, blue_giant,
             colors=['#e6194b', '#3cb44b', '#ffe119'])

ax.set_frame_on(False)
ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout()
plt.show()