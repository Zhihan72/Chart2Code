import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)

downtown_consumption = [220, 205, 210, 245, 240, 230, 240, 250, 230, 200, 220, 215]
uptown_consumption = [190, 195, 185, 205, 200, 195, 200, 200, 210, 185, 180, 205]
suburb_consumption = [160, 145, 150, 165, 140, 155, 155, 150, 165, 150, 155, 160]
airport_consumption = [290, 285, 300, 320, 295, 310, 280, 290, 310, 295, 300, 320]

fig, axes = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)  # Change to 1x2 grid

bar_width = 0.2
x_indices = np.arange(len(months))

colors = ['skyblue', 'lightgreen', 'lightcoral', 'silver']

for i, consumption in enumerate([downtown_consumption, uptown_consumption, suburb_consumption, airport_consumption]):
    axes[0].bar(x_indices + i * bar_width, consumption, bar_width, color=colors[i])

axes[0].set_xticks(x_indices + bar_width * 1.5)
axes[0].set_xticklabels([''] * len(months), rotation=45, ha='right')
axes[0].grid(True, linestyle='--', alpha=0.7)

quarters = ['Q1', 'Q2', 'Q3', 'Q4']
x_indices_2 = np.arange(len(quarters))
average_consumptions = {
    'Downtown': [np.mean(downtown_consumption[i*3:i*3+3]) for i in range(4)],
    'Uptown': [np.mean(uptown_consumption[i*3:i*3+3]) for i in range(4)],
    'Suburb': [np.mean(suburb_consumption[i*3:i*3+3]) for i in range(4)],
    'Airport': [np.mean(airport_consumption[i*3:i*3+3]) for i in range(4)],
}

for i, avg in enumerate(average_consumptions.values()):
    axes[1].bar(x_indices_2 + i * bar_width, avg, bar_width, color=colors[i])

axes[1].set_xticks(x_indices_2 + bar_width * 1.5)
axes[1].set_xticklabels([''] * len(quarters), rotation=45, ha='right')
axes[1].grid(True, linestyle='--', alpha=0.7)

plt.show()