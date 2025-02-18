import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1960, 2030, 10)
pop_music = np.array([10, 20, 25, 30, 32, 35, 40])
rock_music = np.array([5, 15, 20, 25, 26, 27, 29])
hiphop_music = np.array([0, 0, 5, 10, 15, 20, 25])
jazz_music = np.array([20, 18, 15, 10, 7, 5, 3])

plt.figure(figsize=(14, 8))

plt.plot(decades, pop_music, marker='D', linestyle='--', color='green', linewidth=3, label='Pop')
plt.plot(decades, rock_music, marker='v', linestyle='-.', color='darkred', linewidth=2, label='Rock')
plt.plot(decades, hiphop_music, marker='x', linestyle='-', color='gold', linewidth=2, label='Hip Hop')
plt.plot(decades, jazz_music, marker='h', linestyle=':', color='blue', linewidth=2, label='Jazz')

plt.title('Evolution of Music Genres in Radio Airplay (1960 - 2020)', fontsize=18, fontweight='bold')
plt.xlabel('Decade', fontsize=14)
plt.ylabel('Percentage of Radio Airplay', fontsize=14)

plt.legend(loc='lower right', fontsize=12)
plt.grid(True, linestyle='-.', alpha=0.8)

highlight_year = 2020
pop_2020 = pop_music[-1]
plt.annotate('Peak Pop Music Airplay', 
             xy=(highlight_year, pop_2020),
             xytext=(highlight_year - 20, pop_2020 + 5),
             arrowprops=dict(facecolor='red', arrowstyle='->', lw=1.5), 
             fontsize=11, color='blue', bbox=dict(boxstyle="round,pad=0.3", edgecolor='blue', facecolor='lightgray'))

plt.tight_layout()
plt.show()