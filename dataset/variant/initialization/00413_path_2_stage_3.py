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

# Create a pie chart and make it a donut
plt.pie(adrenaline_levels, labels=sports, colors=colors, startangle=140, wedgeprops=dict(width=0.3, edgecolor='w'))

plt.show()