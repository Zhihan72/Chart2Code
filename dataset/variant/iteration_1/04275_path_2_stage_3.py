import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
solarland = np.array([120, 135, 150, 170, 190, 215, 240, 230, 210, 190, 160, 130])
ecotopia = np.array([80, 100, 120, 140, 160, 180, 200, 195, 175, 155, 130, 100])
sunstate = np.array([95, 110, 125, 145, 165, 185, 205, 200, 180, 160, 140, 115])

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(months, solarland, marker='o', linestyle='-', color='#E74C3C', linewidth=2)
ax.plot(months, ecotopia, marker='s', linestyle='-', color='#F1C40F', linewidth=2)
ax.plot(months, sunstate, marker='^', linestyle='-', color='#8E44AD', linewidth=2)

total_kWh = solarland + ecotopia + sunstate
ax2 = ax.twinx()
ax2.plot(months, total_kWh, color='silver', linestyle='--', linewidth=1.5)

plt.show()