import matplotlib.pyplot as plt
import numpy as np

expenses_data = np.array([
    [1200, 1250, 1300, 1280, 1230, 1190, 1220, 1240, 1210, 1260, 1280, 1290],
    [500, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620],
    [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310],
    [150, 160, 170, 165, 160, 155, 150, 145, 140, 135, 130, 125],
    [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]
])

colors = ['#e74c3c', '#3498db', '#2ecc71', '#f1c40f', '#34495e']

fig, ax = plt.subplots(figsize=(12, 8))

index = np.arange(12)  # Replaced len(months) with 12 directly since months are not labeled
bottom = np.zeros(12)

for i in range(len(colors)):  # Loop through the number of colors for bars, categories are not labeled
    ax.bar(index, expenses_data[i], bottom=bottom, color=colors[i])
    bottom += expenses_data[i]

plt.show()