import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1990, 2015)
traditional_agriculture = np.array([49, 47, 46, 44, 41, 36, 34, 31, 29, 27, 24, 21, 19, 17, 14, 11, 9, 7, 5, 3, 1, 0, 0, 0, 0])
organic_farming = np.array([3, 4, 5, 4, 7, 9, 8, 12, 14, 14, 17, 22, 22, 26, 28, 31, 33, 33, 37, 39, 41, 43, 44, 44, 46])
hydroponics = np.array([0, 1, 1, 1, 3, 2, 5, 5, 7, 9, 11, 14, 16, 21, 21, 24, 25, 27, 31, 31, 34, 37, 40, 43, 48])
vertical_farming = np.array([0, 0, 0, 0, 0, 2, 1, 3, 4, 3, 7, 7, 9, 13, 15, 15, 17, 19, 23, 25, 27, 29, 31, 30, 36])

total_agriculture = (traditional_agriculture + organic_farming + hydroponics + vertical_farming)

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, traditional_agriculture, organic_farming, hydroponics, vertical_farming,
             labels=['Trad.', 'Org.', 'Hydr.', 'Vert.'],
             colors=['#ffcc99', '#66b3ff', '#99ff99', '#ff9999'], alpha=0.85)

ax.plot(years, total_agriculture, label='Total Area', color='purple', linestyle='-', marker='x')

ax.set_title("Land Use Changes (1990-2015)", fontsize=18, fontweight='bold')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Land (M ha)", fontsize=14)

ax.set_xticks(years[::2])
ax.set_yticks(np.arange(0, 101, 10))
ax.grid(True, linestyle='-.', linewidth=0.7, alpha=0.5)
ax.minorticks_on()
ax.grid(which='minor', linestyle=':', linewidth=0.5, alpha=0.3)

ax.legend(loc='lower right', fontsize=10, shadow=True)

for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_color('gray')
    spine.set_linewidth(1.2)

ax.annotate('Start of Hydroponics', xy=(2001, 2), xytext=(1995, 10),
            arrowprops=dict(arrowstyle='-|>', color='purple'), fontsize=12, color='purple')
ax.annotate('Rapid growth in Vertical Farming', xy=(2015, 16), xytext=(2012, 30),
            arrowprops=dict(arrowstyle='-|>', color='purple'), fontsize=12, color='purple')

fig.tight_layout()

plt.show()