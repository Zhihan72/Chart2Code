import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1900, 2001, 10)

atlantic_data = [17.2, 17, 16.5, 18, 17.6, 16, 18.3, 17.5, 18.1, 18.5, 16]
pacific_data = [15.6, 15.2, 16.8, 15, 16.4, 15.8, 17, 16.2, 15.5, 16.6, 16]
indian_data = [10.5, 11, 10.3, 10.1, 11.2, 10.8, 11.7, 10.7, 10.4, 11.5, 10]
southern_data = [12.3, 13.2, 12.6, 13.5, 12, 12.8, 13, 12.5, 13.6, 12.4, 13.8]
arctic_data = [0.8, 1.3, 1.1, 0.9, 1.5, 0.6, 1.4, 0.5, 0.7, 1, 1.2]

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(decades, atlantic_data, label='Atlantic Waters', marker='x', linestyle='-', linewidth=2.5, color='#d62728')
ax1.plot(decades, pacific_data, label='Pacific Waters', marker='*', linestyle=':', linewidth=1.5, color='#1f77b4')
ax1.plot(decades, indian_data, label='Indian Waters', marker='h', linestyle='--', linewidth=2, color='#9467bd')
ax1.plot(decades, southern_data, label='Southern Waters', marker='p', linestyle='-', linewidth=3, color='#2ca02c')
ax1.plot(decades, arctic_data, label='Arctic Waters', marker='d', linestyle='-.', linewidth=1, color='#ff7f0e')

ax1.set_title("Ocean Flow Changes Over the 20th Century\nA Study on Global Ocean Currents", fontsize=18, fontweight='bold')
ax1.set_xlabel('Time Periods', fontsize=14, fontweight='bold')
ax1.set_ylabel('Flow Strength (Sverdrup)', fontsize=14, fontweight='bold')
ax1.legend(loc='upper right', title='Ocean Regions', fontsize=12, title_fontsize='13', frameon=False)
ax1.grid(True, linestyle='-', linewidth=0.5, alpha=0.5)

ax1.annotate('Rise in\nArctic Flow', xy=(2000, 1.5), xytext=(1940, 3),
             arrowprops=dict(facecolor='gray', shrink=0.05, width=1, headwidth=5),
             fontsize=12, color='purple')

plt.tight_layout()
plt.show()