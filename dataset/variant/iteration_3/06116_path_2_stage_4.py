import matplotlib.pyplot as plt
import numpy as np

heroes = ["The Silent Knight", "Thunder Hornet", "Crimson Tornado", "Midnight Leopard"]
timeframe = ["Year 2018", "Year 2019", "Year 2020", "Year 2021", "Year 2022"]

rescues = np.array([
    [125, 135, 155, 145, 165],
    [100, 105, 115, 110, 130],
    [85, 90, 100, 95, 115],
    [115, 120, 125, 135, 140]
])
battles = np.array([
    [85, 100, 110, 90, 105],
    [65, 75, 85, 80, 80],
    [80, 85, 95, 90, 100],
    [95, 90, 105, 100, 120]
])
community = np.array([
    [35, 45, 55, 50, 60],
    [25, 30, 35, 40, 45],
    [30, 35, 40, 45, 50],
    [40, 45, 50, 55, 50]
])

fig, axs = plt.subplots(figsize=(14, 8))
width = 0.2
x = np.arange(len(timeframe))

axs.bar(x - 1.5 * width, rescues[0], width, color='#2E86C1', edgecolor='black')
axs.bar(x - 0.5 * width, battles[0], width, color='#1ABC9C', edgecolor='black')
axs.bar(x + 0.5 * width, community[0], width, color='#7D3C98', edgecolor='black')

axs.bar(x - 1.5 * width + 1 * len(timeframe), rescues[1], width, color='#F1C40F', edgecolor='black')
axs.bar(x - 0.5 * width + 1 * len(timeframe), battles[1], width, color='#E67E22', edgecolor='black')
axs.bar(x + 0.5 * width + 1 * len(timeframe), community[1], width, color='#E74C3C', edgecolor='black')

axs.bar(x - 1.5 * width + 2 * len(timeframe), rescues[2], width, color='#5DADE2', edgecolor='black')
axs.bar(x - 0.5 * width + 2 * len(timeframe), battles[2], width, color='#58D68D', edgecolor='black')
axs.bar(x + 0.5 * width + 2 * len(timeframe), community[2], width, color='#AF7AC5', edgecolor='black')

axs.bar(x - 1.5 * width + 3 * len(timeframe), rescues[3], width, color='#F4D03F', edgecolor='black')
axs.bar(x - 0.5 * width + 3 * len(timeframe), battles[3], width, color='#DC7633', edgecolor='black')
axs.bar(x + 0.5 * width + 3 * len(timeframe), community[3], width, color='#C0392B', edgecolor='black')

axs.set_title('Superheroes Achievements (Years 2018-2022)', fontsize=16, fontweight='bold', pad=20)
axs.set_xlabel('Time Periods', fontsize=12)
axs.set_ylabel('Mission Count Successfully Completed', fontsize=12)

axs.set_xticks(np.concatenate([x + offset * len(timeframe) for offset in range(4)]))
axs.set_xticklabels(timeframe * 4, rotation=45)

plt.tight_layout()
plt.show()