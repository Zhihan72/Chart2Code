import matplotlib.pyplot as plt
import numpy as np

# Original sports and adrenaline levels
sports = [
    "Skydiving", "Bungee Jumping", "White Water Rafting",
    "Rock Climbing", "Mountain Biking", "Paragliding"
]
adrenaline_levels = [95, 90, 85, 80, 75, 70]

# New sports and their adrenaline levels
new_sports = ["Surfing", "Kart Racing", "Hang Gliding"]
new_adrenaline_levels = [65, 60, 55]

# Extend original datasets with new data
sports.extend(new_sports)
adrenaline_levels.extend(new_adrenaline_levels)

plt.figure(figsize=(14, 8))
colors = plt.cm.viridis(np.linspace(0, 1, len(sports)))
patterns = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.']

bars = plt.barh(sports, adrenaline_levels, color=colors, edgecolor='black', hatch='/', height=0.6)

plt.gca().set_facecolor('#f0f0f0')
plt.gca().set_axisbelow(True)
plt.grid(axis='x', linestyle='--', alpha=0.5, color='gray')

for bar, pattern in zip(bars, patterns):
    bar.set_hatch(pattern)

plt.gca().invert_yaxis()

ax_inset = plt.gcf().add_axes([0.75, 0.15, 0.2, 0.2])
ax_inset.pie(adrenaline_levels, colors=colors, startangle=140)

plt.show()