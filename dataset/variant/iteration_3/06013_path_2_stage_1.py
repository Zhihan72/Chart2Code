import matplotlib.pyplot as plt
import numpy as np

missions = ['Apollo 11', 'Apollo 12', 'Apollo 14', 'Apollo 15', 'Apollo 16', 'Apollo 17']
daytime_highs = np.array([127, 123, 130, 125, 127, 128])
nighttime_lows = np.array([-153, -155, -150, -157, -155, -156])

fig, ax = plt.subplots(figsize=(12, 8))

width = 0.3
x_pos = np.arange(len(missions))

bars_day = ax.bar(x_pos - width, daytime_highs, width,
                  label='Apollo Day Highs', color='darkred', edgecolor='gray', linestyle='--')
bars_night = ax.bar(x_pos + width, nighttime_lows, width,
                    label='Apollo Night Lows', color='darkblue', edgecolor='gray', hatch='//')

ax.set_ylabel('Temperature (°C)', fontsize=12, fontstyle='italic')
ax.set_title('Lunar Temperatures at Apollo Sites', fontsize=16, fontweight='bold', fontstyle='italic')
ax.set_xticks(x_pos)
ax.set_xticklabels(missions, fontsize=10, rotation=30)
ax.legend(frameon=False)

def add_bar_labels(bars, color='black'):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}°C', 
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5), 
                    textcoords="offset points",
                    ha='center', va='bottom', color=color, fontsize=10, fontweight='bold')

add_bar_labels(bars_day, color='white')  
add_bar_labels(bars_night, color='yellow')

ax.yaxis.grid(True, linestyle='-.', alpha=0.5)
ax.set_axisbelow(True)

for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()