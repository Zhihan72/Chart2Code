import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

deer = [12, 14, 15, 15, 18, 20, 22, 23, 25, 27, 28]
foxes = [8, 9, 10, 11, 12, 12, 13, 14, 15, 16, 16]
rabbits = [30, 28, 26, 27, 29, 31, 32, 34, 35, 38, 40]
wolves = [4, 4, 5, 5, 6, 6, 7, 7, 8, 9, 9]

populations = np.vstack([deer, foxes, rabbits, wolves])

colors = ['#8B4513', '#D2691E', '#FFD700', '#4682B4']

plt.figure(figsize=(14, 8))

plt.stackplot(years, populations, colors=colors, alpha=0.8)

# Randomly altered textual elements
plt.title('Wildlife Dynamics Over Time\n(Decade Analysis 2010-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Timeline (Years)', fontsize=12)
plt.ylabel('Species Count (×1,000)', fontsize=12)

plt.xticks(years, rotation=45)

plt.annotate('Deer Pop. Spike', xy=(2014, deer[4]), xytext=(2015, 20),
             arrowprops=dict(facecolor='green', arrowstyle='->', lw=1.5),
             fontsize=10, color='darkgreen', fontweight='bold')
plt.annotate('Foxes Stability', xy=(2018, foxes[8]), xytext=(2016, 12),
             arrowprops=dict(facecolor='orange', arrowstyle='->', lw=1.5),
             fontsize=10, color='darkorange', fontweight='bold')

plt.tight_layout()

plt.show()