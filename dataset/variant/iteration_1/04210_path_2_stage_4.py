import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

area1_aqi = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105])
area2_aqi = np.array([40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62])
area3_aqi = np.array([45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
area4_aqi = np.array([30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])  # New data series
area5_aqi = np.array([70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48])  # New data series

plt.figure(figsize=(14, 8))

plt.plot(months, area1_aqi, linestyle='-.', color='red', marker='x', label='Zone A')
plt.plot(months, area2_aqi, linestyle='-', color='green', marker='D', label='Zone B')
plt.plot(months, area3_aqi, linestyle='--', color='blue', marker='*', label='Zone C')
plt.plot(months, area4_aqi, linestyle=':', color='purple', marker='o', label='Zone D')  # Plot Zone D
plt.plot(months, area5_aqi, linestyle='-', color='orange', marker='s', label='Zone E')  # Plot Zone E

for i, val in enumerate(area3_aqi):
    if val > 100:
        plt.annotate('High Risk', xy=(months[i], val), 
                     xytext=(months[i], val + 5),
                     arrowprops=dict(facecolor='gray', shrink=0.05),
                     fontsize=9, ha='center')

plt.title("Annual Air Metrics Evaluation", fontsize=16, fontweight='bold')
plt.xlabel("Timeline", fontsize=12)
plt.ylabel("Pollution Score", fontsize=12)

plt.xticks(months, fontsize=10)
plt.yticks(np.arange(0, 120, 10), fontsize=10)

plt.legend(loc='lower right', fontsize=10)

plt.grid(True, linestyle='-', alpha=0.9)

plt.tight_layout()

plt.show()