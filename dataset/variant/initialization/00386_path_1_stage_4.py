import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1950, 2030, 10)
jazz_popularity = [70, 65, 55, 50, 40, 30, 25, 20]
rock_popularity = [20, 60, 80, 75, 60, 50, 45, 40]
hiphop_popularity = [0, 0, 10, 30, 65, 80, 90, 85]
electronic_popularity = [5, 10, 15, 20, 30, 50, 60, 70]

fig, ax = plt.subplots(figsize=(12, 7))

single_color = 'steelblue'

ax.plot(decades, jazz_popularity, label='Blues', color=single_color, marker='p', linewidth=1, linestyle='--')
ax.plot(decades, rock_popularity, label='Metal', color=single_color, marker='h', linewidth=1.5, linestyle='-')
ax.plot(decades, hiphop_popularity, label='Rap', color=single_color, marker='v', linewidth=1.5, linestyle='-.')
ax.plot(decades, electronic_popularity, label='Trance', color=single_color, marker='+', linewidth=2, linestyle=':')

ax.set_xlabel('Epoch', fontsize=12)
ax.set_ylabel('Popularity Rank', fontsize=12)
ax.set_title('Rhythms of Time:\nGenres Popularity Evolution', fontsize=16, fontweight='bold')

ax.grid(True, linestyle='-', alpha=0.1)
ax.legend(loc='lower center', title='Sound Styles', fontsize=10, title_fontsize='12')

plt.xticks(decades, fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()