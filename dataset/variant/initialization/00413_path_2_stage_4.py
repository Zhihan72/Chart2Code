import matplotlib.pyplot as plt
import numpy as np

sports = [
    "Skydiving", "Bungee Jumping", "White Water Rafting",
    "Rock Climbing", "Mountain Biking", "Paragliding",
    "Surfing", "Kart Racing", "Hang Gliding"
]
adrenaline_levels = [95, 90, 85, 80, 75, 70, 65, 60, 55]

plt.figure(figsize=(8, 8))
colors = plt.cm.viridis(np.linspace(0, 1, len(sports)))

# Shuffle colors by manually rearranging the index for the colors array
shuffled_colors = [colors[2], colors[0], colors[3], colors[5], colors[8], colors[7], colors[1], colors[4], colors[6]]

# Create a pie chart and make it a donut
plt.pie(adrenaline_levels, labels=sports, colors=shuffled_colors, startangle=140, wedgeprops=dict(width=0.3, edgecolor='w'))

plt.show()