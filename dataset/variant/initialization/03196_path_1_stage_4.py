import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

ny_commuting = np.array([1.0, 1.2, 1.5, 2.0, 2.5, 3.1, 3.7, 4.3, 4.6, 5.0, 5.2])
sf_commuting = np.array([3.2, 3.5, 4.0, 4.4, 5.1, 5.7, 6.3, 6.8, 7.0, 7.3, 7.5])
cph_commuting = np.array([26.4, 27.5, 28.7, 29.9, 31.0, 32.2, 33.3, 34.5, 35.6, 36.7, 37.8])
ams_commuting = np.array([20.3, 21.1, 22.0, 23.2, 24.6, 25.8, 26.7, 27.5, 28.0, 29.0, 30.2])

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(years, ny_commuting, marker='o', linestyle='-', linewidth=2, color='orange')
ax.plot(years, sf_commuting, marker='s', linestyle='-', linewidth=2, color='red')
ax.plot(years, cph_commuting, marker='^', linestyle='-', linewidth=2, color='blue')
ax.plot(years, ams_commuting, marker='d', linestyle='-', linewidth=2, color='green')

# Shortening the annotations for the final value in 2020
ax.annotate(f'{ny_commuting[-1]:.1f}%', xy=(2020, ny_commuting[-1]), xytext=(2018.5, ny_commuting[-1]+2),
            arrowprops=dict(arrowstyle="->", color='orange'), color='orange', fontsize=10)
ax.annotate(f'{sf_commuting[-1]:.1f}%', xy=(2020, sf_commuting[-1]), xytext=(2018.5, sf_commuting[-1]+2),
            arrowprops=dict(arrowstyle="->", color='red'), color='red', fontsize=10)
ax.annotate(f'{cph_commuting[-1]:.1f}%', xy=(2020, cph_commuting[-1]), xytext=(2018.5, cph_commuting[-1]-3),
            arrowprops=dict(arrowstyle="->", color='blue'), color='blue', fontsize=10)
ax.annotate(f'{ams_commuting[-1]:.1f}%', xy=(2020, ams_commuting[-1]), xytext=(2018.5, ams_commuting[-1]+2),
            arrowprops=dict(arrowstyle="->", color='green'), color='green', fontsize=10)

# Simplified title and axis labels
ax.set_title("Bicycle Commuting Trends (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Bicycle Commuters (%)", fontsize=14)
ax.set_xticks(years)
ax.set_ylim(0, 40)

plt.tight_layout()

plt.show()