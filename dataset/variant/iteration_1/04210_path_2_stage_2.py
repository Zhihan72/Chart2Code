import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

area1_aqi = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105])
area2_aqi = np.array([40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62])
area3_aqi = np.array([45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])

plt.figure(figsize=(14, 8))

# Updated colors: Replace 'purple' with 'red', 'orange' with 'green', 'cyan' with 'blue'
plt.plot(months, area1_aqi, linestyle='-.', color='red', marker='x', label='Residential Area')
plt.plot(months, area2_aqi, linestyle='-', color='green', marker='D', label='Industrial Area')
plt.plot(months, area3_aqi, linestyle='--', color='blue', marker='*', label='Commercial Area')

for i, val in enumerate(area3_aqi):
    if val > 100:
        plt.annotate('Unsafe', xy=(months[i], val), 
                     xytext=(months[i], val + 5),
                     arrowprops=dict(facecolor='gray', shrink=0.05),
                     fontsize=9, ha='center')

plt.title("Urban Air Quality Index (AQI) Trends Throughout The Year", fontsize=16, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Air Quality Index (AQI)", fontsize=12)

plt.xticks(months, fontsize=10)
plt.yticks(np.arange(0, 120, 10), fontsize=10)

plt.legend(loc='lower right', fontsize=10)

plt.grid(True, linestyle='-', alpha=0.9)

plt.tight_layout()

plt.show()