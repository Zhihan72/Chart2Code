import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Noachis', 'Hellas', 'Solis', 'Tharsis', 'Amazonis', 'Elysium', 'Planum', 'Arcadia', 'Acidalia', 'Arabia', 'Elysium II', 'Thaumasia'])
mars_day = np.linspace(1, 12, num=12)

north_temp = np.array([-60, -50, -45, -30, -35, -40, -55, -65, -70, -75, -80, -85])
south_temp = np.array([-65, -55, -50, -35, -40, -45, -60, -70, -75, -80, -85, -90])
equator_temp = np.array([-50, -45, -40, -30, -32, -35, -42, -50, -55, -60, -65, -70])
highlands_temp = np.array([-70, -60, -55, -40, -45, -50, -65, -75, -80, -85, -90, -95])
lowlands_temp = np.array([-55, -45, -40, -25, -30, -35, -50, -60, -65, -70, -75, -80])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(mars_day, north_temp, marker='s', color='c', linestyle='--', linewidth=3)
ax.plot(mars_day, south_temp, marker='^', color='r', linestyle='-.', linewidth=2)
ax.plot(mars_day, equator_temp, marker='D', color='b', linestyle=':', linewidth=2.5)
ax.plot(mars_day, highlands_temp, marker='x', color='g', linestyle='-', linewidth=2)
ax.plot(mars_day, lowlands_temp, marker='o', color='m', linestyle='-', linewidth=1.5)

ax.set_xticks(mars_day)
ax.set_yticks(np.arange(-95, -20, 5))
ax.grid(which='major', linestyle='-', linewidth=0.75, alpha=0.9)

plt.tight_layout()
plt.show()