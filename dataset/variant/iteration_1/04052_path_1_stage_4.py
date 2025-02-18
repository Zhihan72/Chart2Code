import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
soccer_subs = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 130, 140, 150, 160, 170, 180]
tennis_subs = [20, 22, 24, 26, 28, 30, 32, 35, 38, 40, 45, 50, 55, 58, 60, 62, 65, 70, 75, 80, 85]
esports_subs = [5, 10, 15, 20, 28, 35, 40, 50, 60, 70, 85, 100, 115, 130, 145, 160, 175, 190, 210, 230, 250]

fig, ax = plt.subplots(figsize=(14, 8))

consistent_color = '#1f77b4'

ax.plot(years, soccer_subs, marker='o', linestyle='-', linewidth=2, color=consistent_color)
ax.plot(years, tennis_subs, marker='s', linestyle='-.', linewidth=2, color=consistent_color)
ax.plot(years, esports_subs, marker='^', linestyle=':', linewidth=2, color=consistent_color)

ax.set_title('Sports Popularity (2000-2020)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14, fontweight='semibold')
ax.set_ylabel('Subscribers (k)', fontsize=14, fontweight='semibold')

ax.annotate('Soccer momentum', xy=(2016, 130), xytext=(2010, 120),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=12, color=consistent_color)

ax.annotate('E-sports boom', xy=(2016, 160), xytext=(2005, 180),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=12, color=consistent_color)

ax.annotate('Tennis stable', xy=(2016, 62), xytext=(2005, 35),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=12, color=consistent_color)

ax.set_facecolor('#f7f7f9')
fig.patch.set_facecolor('#eeeeee')

plt.tight_layout()

plt.show()