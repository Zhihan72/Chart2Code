import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1900, 2001, 10)

atlantic_data = [16, 16.5, 17, 17.2, 17.5, 17.6, 17.8, 18, 18.1, 18.3, 18.5]
pacific_data = [15, 15.2, 15.5, 15.6, 15.8, 16, 16.2, 16.4, 16.6, 16.8, 17]
indian_data = [10, 10.1, 10.3, 10.5, 10.7, 10.8, 11, 11.2, 11.4, 11.5, 11.7]
southern_data = [12, 12.3, 12.5, 12.6, 12.8, 13, 13.2, 13.3, 13.5, 13.6, 13.8]
arctic_data = [0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]

fig, ax1 = plt.subplots(figsize=(14, 8))

# Colors are shuffled by swapping them among the line plots
ax1.plot(decades, atlantic_data, label='Atlantic Ocean', marker='o', linestyle='-', linewidth=2, color='#d62728')  # Changed
ax1.plot(decades, pacific_data, label='Pacific Ocean', marker='s', linestyle='--', linewidth=2, color='#1f77b4')  # Changed
ax1.plot(decades, indian_data, label='Indian Ocean', marker='^', linestyle='-.', linewidth=2, color='#9467bd')  # Changed
ax1.plot(decades, southern_data, label='Southern Ocean', marker='D', linestyle=':', linewidth=2, color='#2ca02c')  # Changed
ax1.plot(decades, arctic_data, label='Arctic Ocean', marker='v', linestyle='-', linewidth=2, color='#ff7f0e')  # Changed

ax1.set_title("Century-long Trends in Ocean Currents (1900-2000)\nAnalyzing Strength Across Various Oceans", fontsize=18, fontweight='bold')
ax1.set_xlabel('Decades', fontsize=14, fontweight='bold')
ax1.set_ylabel('Current Strength (Sverdrup, Sv)', fontsize=14, fontweight='bold')
ax1.legend(loc='upper left', title='Oceans', fontsize=12, title_fontsize='13')
ax1.grid(True, linestyle='--', alpha=0.7)

ax1.annotate('Significant Increase\nin Arctic Ocean', xy=(2000, 1.5), xytext=(1940, 3),
             arrowprops=dict(facecolor='blue', shrink=0.05, width=1, headwidth=5),
             fontsize=12, color='darkblue')

plt.tight_layout()
plt.show()