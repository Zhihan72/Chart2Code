import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
categories = ['Housing', 'Food', 'Transportation', 'Utilities', 'Medical', 'Entertainment']

expenses_data = np.array([
    [1200, 1250, 1300, 1280, 1230, 1190, 1220, 1240, 1210, 1260, 1280, 1290],
    [500, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620],
    [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310],
    [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155],
    [150, 160, 170, 165, 160, 155, 150, 145, 140, 135, 130, 125],
    [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]
])

# New color set
colors = ['#e74c3c', '#3498db', '#2ecc71', '#9b59b6', '#f1c40f', '#34495e']

fig, ax = plt.subplots(figsize=(12, 8))

index = np.arange(len(months))
bottom = np.zeros(len(months))

for i in range(len(categories)):
    ax.bar(index, expenses_data[i], bottom=bottom, color=colors[i], label=categories[i])
    bottom += expenses_data[i]

ax.set_xlabel('Months', fontsize=12)
ax.set_ylabel('Expenses (USD)', fontsize=12)
ax.set_xticks(index)
ax.set_xticklabels(months, rotation=45, ha='right')

ax.legend()

plt.show()