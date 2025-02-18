import matplotlib.pyplot as plt
import numpy as np

years = ['22', '23', '24', '25', '26']
hull = np.array([60, 70, 80, 90, 100])
engine = np.array([50, 65, 75, 85, 95])
living = np.array([30, 50, 65, 80, 90])

fig, ax = plt.subplots(figsize=(10, 7))

new_colors = ['#FF4500', '#3CB371', '#FFD700']

ax.bar(years, hull, color=new_colors[0], edgecolor='black')
ax.bar(years, engine, bottom=hull, color=new_colors[1], edgecolor='black')
ax.bar(years, living, 
       bottom=hull + engine, 
       color=new_colors[2], 
       edgecolor='black')

ax.set_xlabel('Yr', fontsize=12)
ax.set_ylabel('Progress (%)', fontsize=12)

ax.set_ylim(0, 260)

plt.tight_layout()

plt.show()