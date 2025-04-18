import matplotlib.pyplot as plt
import numpy as np

# Artificial data representing the strength of ocean currents (in Sv) across different oceans per decade
decades = np.arange(1900, 2001, 10)
atlantic_data = [16, 16.5, 17, 17.2, 17.5, 17.6, 17.8, 18, 18.1, 18.3, 18.5]
pacific_data = [15, 15.2, 15.5, 15.6, 15.8, 16, 16.2, 16.4, 16.6, 16.8, 17]
indian_data = [10, 10.1, 10.3, 10.5, 10.7, 10.8, 11, 11.2, 11.4, 11.5, 11.7]
southern_data = [12, 12.3, 12.5, 12.6, 12.8, 13, 13.2, 13.3, 13.5, 13.6, 13.8]
arctic_data = [0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(decades, atlantic_data, label='Atlantic Ocean', marker='x', linestyle=':', linewidth=2.5, color='magenta')
ax1.plot(decades, pacific_data, label='Pacific Zone', marker='d', linestyle='-', linewidth=1.5, color='cyan')
ax1.plot(decades, indian_data, label='India\'s Waters', marker='p', linestyle='--', linewidth=2, color='orange')
ax1.plot(decades, southern_data, label='Southern Hemisphere', marker='h', linestyle='-.', linewidth=3, color='green')
ax1.plot(decades, arctic_data, label='Frozen North', marker='*', linestyle='-', linewidth=1, color='grey')

ax1.set_title("Century-long Shifts in Oceanic Patterns", fontsize=18, fontweight='normal')
ax1.set_xlabel('Time Period', fontsize=14, fontweight='bold')
ax1.set_ylabel('Flow Strength in Sv', fontsize=14, fontweight='bold')
ax1.legend(loc='best', fontsize=12)

ax1.grid(False)

ax1.annotate('Gradual Rise\nin Frozen North', xy=(2000, 1.5), xytext=(1930, 3),
             arrowprops=dict(facecolor='red', shrink=0.05, width=1, headwidth=6),
             fontsize=12, color='darkred')

plt.tight_layout()
plt.show()