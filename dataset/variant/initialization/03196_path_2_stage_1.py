import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
ny_commuting = np.array([1.0, 1.2, 1.5, 2.0, 2.5, 3.1, 3.7, 4.3, 4.6, 5.0, 5.2])
cph_commuting = np.array([26.4, 27.5, 28.7, 29.9, 31.0, 32.2, 33.3, 34.5, 35.6, 36.7, 37.8])

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(years, ny_commuting, marker='o', linestyle='-', linewidth=2, color='blue', label='New York')
ax.plot(years, cph_commuting, marker='^', linestyle='-', linewidth=2, color='red', label='Copenhagen')

ax.annotate(f'{ny_commuting[-1]:.1f}%', xy=(2020, ny_commuting[-1]), xytext=(2018.5, ny_commuting[-1]+2),
            arrowprops=dict(arrowstyle="->", color='blue'), color='blue', fontsize=10)
ax.annotate(f'{cph_commuting[-1]:.1f}%', xy=(2020, cph_commuting[-1]), xytext=(2018.5, cph_commuting[-1]-3),
            arrowprops=dict(arrowstyle="->", color='red'), color='red', fontsize=10)

ax.set_title("Rising Trends in Urban Bicycle Commuting:\nA Decade of Change (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Percentage of Workforce Commuting by Bicycle (%)", fontsize=14)
ax.set_xticks(years)
ax.set_ylim(0, 40)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

ax.legend(title='Cities', fontsize=12, loc='upper left')

plt.tight_layout()
plt.show()