import matplotlib.pyplot as plt
import numpy as np

months = np.array(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
                   'September', 'October', 'November', 'December'])

area1_aqi = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105])
area2_aqi = np.array([40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62])
area3_aqi = np.array([45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])

plt.figure(figsize=(14, 8))

# Changed marker styles and line styles
plt.plot(months, area1_aqi, linestyle='-.', color='blue', marker='D', label='Living Zone')
plt.plot(months, area2_aqi, linestyle='-', color='green', marker='x', label='Factory Region')
plt.plot(months, area3_aqi, linestyle='--', color='red', marker='*', label='Shopping District')

# Removed the annotation with arrows

plt.title("City AQI Trends Over 12 Months", fontsize=16, fontweight='bold')
plt.xlabel("Months", fontsize=12)
plt.ylabel("AQI Levels", fontsize=12)

plt.xticks(months, fontsize=10)
plt.yticks(np.arange(0, 120, 10), fontsize=10)

# Changed legend location and style
plt.legend(loc='lower right', fontsize=12, edgecolor='blue', framealpha=0.3)

# Changed grid style and removed tight_layout
plt.grid(True, linestyle='-.', alpha=0.5)

plt.show()