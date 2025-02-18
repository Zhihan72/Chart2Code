import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1960, 2030, 10)

pop_music = np.array([10, 20, 25, 30, 32, 35, 40])
rock_music = np.array([5, 15, 20, 25, 26, 27, 29])
electronic_music = np.array([0, 5, 10, 15, 20, 25, 30])
jazz_music = np.array([20, 18, 15, 10, 7, 5, 3])

plt.figure(figsize=(14, 8))

# Changed colors for each music genre
plt.plot(decades, pop_music, marker='v', linestyle=':', color='lightcoral', linewidth=2.5, label='Jazz')
plt.plot(decades, rock_music, marker='x', linestyle='-.', color='blueviolet', linewidth=2.5, label='Electronic')
plt.plot(decades, electronic_music, marker='<', linestyle='-', color='royalblue', linewidth=2.5, label='Pop')
plt.plot(decades, jazz_music, marker='h', linestyle='-', color='olive', linewidth=2.5, label='Rock')

plt.title('Trends of Radio Music Genres Over the Period', fontsize=18, fontweight='bold')
plt.xlabel('Years', fontsize=14)
plt.ylabel('Radio Airplay Share', fontsize=14)

plt.legend(loc='lower right', fontsize=12, title='Music Types')

plt.grid(True, linestyle=':', alpha=0.4)

highlight_year = 2020
pop_2020 = pop_music[-1]
plt.annotate('Dominant Pop Airplay Moment', 
             xy=(highlight_year, pop_2020),
             xytext=(highlight_year - 20, pop_2020 + 5),
             arrowprops=dict(facecolor='red', arrowstyle='fancy', lw=2), 
             fontsize=11, color='navy', bbox=dict(boxstyle="round,pad=0.5", edgecolor='red', facecolor='lightgrey'))

plt.tight_layout()

plt.show()