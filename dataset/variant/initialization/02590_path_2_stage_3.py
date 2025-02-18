import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2000, 2021)
dolphin_population = [30, 32, 34, 36, 38, 40, 42, 45, 48, 50, 52, 55, 58, 61, 65, 68, 70, 72, 75, 78, 80]
sea_turtle_population = [20, 22, 21, 23, 24, 26, 27, 28, 30, 31, 33, 35, 36, 37, 39, 40, 42, 44, 45, 47, 50]
coral_reef_fish_population = [100, 105, 108, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 162, 165, 167, 170, 172, 175, 177, 180]
shark_population = [8, 8, 9, 9, 10, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 16, 17]

fig, ax = plt.subplots(figsize=(14, 9))
new_colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3']

ax.fill_between(years, 0, dolphin_population, color=new_colors[0], alpha=0.5, label='Dolphins', edgecolor='grey', linewidth=2, linestyle='-.')
ax.fill_between(years, dolphin_population, np.add(dolphin_population, sea_turtle_population), color=new_colors[1], alpha=0.6, label='Sea Turtles', edgecolor='blue', linewidth=0.8, linestyle='--')
ax.fill_between(years, np.add(dolphin_population, sea_turtle_population), np.add.reduce([dolphin_population, sea_turtle_population, coral_reef_fish_population]), color=new_colors[2], alpha=0.5, label='Coral Reef Fish', edgecolor='green', linewidth=1.5, linestyle=':')
ax.fill_between(years, np.add.reduce([dolphin_population, sea_turtle_population, coral_reef_fish_population]), np.add.reduce([dolphin_population, sea_turtle_population, coral_reef_fish_population, shark_population]), color=new_colors[3], alpha=0.5, label='Sharks', edgecolor='purple', linewidth=1, linestyle='-')

ax.set_title("Marine Biodiversity in Coral Bay:\nPopulation Trends Over Two Decades", fontsize=18, fontweight='bold', loc='right', pad=25)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Population (in thousands)", fontsize=14)

ax.plot(years, dolphin_population, marker='d', markersize=6, color=new_colors[0], linestyle='--')
ax.plot(years, np.add(dolphin_population, sea_turtle_population), marker='v', markersize=6, color=new_colors[1], linestyle='-.')
ax.plot(years, np.add.reduce([dolphin_population, sea_turtle_population, coral_reef_fish_population]), marker='p', markersize=6, color=new_colors[2], linestyle='-')
ax.plot(years, np.add.reduce([dolphin_population, sea_turtle_population, coral_reef_fish_population, shark_population]), marker='*', markersize=6, color=new_colors[3], linestyle='--')

plt.xticks(years, rotation=30, ha="right")

ax.legend(loc='upper right', title='Marine Species', fontsize=11, title_fontsize='12')
plt.grid(axis='both', linestyle='-.', alpha=0.5)
plt.tight_layout()
plt.show()