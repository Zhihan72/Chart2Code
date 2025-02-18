import matplotlib.pyplot as plt
import numpy as np

years = ['2022', '2023', '2024', '2025', '2026']
hull_progress = np.array([60, 70, 80, 90, 100])
engine_progress = np.array([50, 65, 75, 85, 95])
control_systems_progress = np.array([40, 55, 70, 85, 95])
living_quarters_progress = np.array([30, 50, 65, 80, 90])

fig, ax = plt.subplots(figsize=(10, 7))

new_colors = ['#FF4500', '#3CB371', '#1E90FF', '#FFD700']

ax.bar(years, hull_progress, color=new_colors[0], edgecolor='black')
ax.bar(years, engine_progress, bottom=hull_progress, color=new_colors[1], edgecolor='black')
ax.bar(years, control_systems_progress, bottom=hull_progress + engine_progress, color=new_colors[2], edgecolor='black')
ax.bar(years, living_quarters_progress, 
       bottom=hull_progress + engine_progress + control_systems_progress, 
       color=new_colors[3], 
       edgecolor='black')

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Construction Progress (%)', fontsize=12)

ax.set_ylim(0, 320)

plt.tight_layout()

plt.show()