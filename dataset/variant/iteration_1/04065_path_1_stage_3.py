import matplotlib.pyplot as plt
import numpy as np

weeks = np.arange(1, 11)

sales = np.array([60, 75, 90, 120, 130, 160, 170, 150, 135, 125])
temperature = np.array([20, 22, 25, 27, 30, 32, 33, 31, 28, 26])
satisfaction = np.array([6, 7, 7.5, 8, 9, 9, 9.5, 8.5, 8, 7.5])

plt.figure(figsize=(14, 9))

plt.scatter(temperature, sales, s=satisfaction*100, c=satisfaction, cmap='plasma', alpha=0.75, edgecolors='black', linewidth=1)

plt.xlabel("Weather Degree (°C)", fontsize=14)
plt.ylabel("Cold Treats Sold (Units)", fontsize=14)

for i, week in enumerate(weeks):
    plt.annotate(f"Period {week}", (temperature[i] + 0.5, sales[i]), fontsize=10, fontweight='bold', bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray'))

plt.tight_layout()

plt.show()