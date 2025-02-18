import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2031)

# Modify some data values within each continent group to introduce randomness while keeping the structure
africa_north_users = np.array([115, 125, 160, 175, 215, 260, 320, 370, 445, 475, 525, 565, 625, 675, 735, 795, 855, 905, 995, 1035, 1095])
africa_south_users = np.array([35, 42, 55, 95, 115, 165, 195, 255, 305, 375, 455, 500, 575, 655, 715, 785, 875, 925, 990, 1060, 1160])
asia_users = np.array([830, 850, 910, 940, 1020, 1050, 1120, 1200, 1290, 1410, 1530, 1650, 1830, 1980, 2170, 2320, 2590, 2810, 3070, 3340, 3660])
europe_users = np.array([495, 515, 525, 535, 545, 555, 575, 585, 605, 635, 675, 685, 715, 735, 750, 745, 755, 770, 765, 780, 785])
north_america_users = np.array([272, 274, 282, 283, 288, 292, 298, 312, 318, 322, 327, 333, 336, 341, 343, 346, 349, 351, 353, 354, 356])
south_america_users = np.array([162, 168, 182, 198, 225, 248, 282, 322, 358, 403, 442, 478, 515, 528, 552, 568, 592, 605, 632, 648, 672])
australia_users = np.array([31, 33, 35, 37, 37, 41, 43, 47, 49, 52, 55, 60, 61, 66, 67, 71, 71, 71, 75, 76, 77])

africa_users = africa_north_users + africa_south_users

colors = ['#FFD700', '#FF4500', '#8A2BE2', '#00FF00', '#1E90FF', '#FF69B4']

plt.figure(figsize=(16, 9))

plt.stackplot(years, africa_users, asia_users, europe_users, north_america_users, south_america_users, australia_users, 
              labels=['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Australia'], colors=colors, alpha=0.8)

plt.title('Evolution of Internet Users by Continent\n(Annual Data from 2010-2030)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Internet Users (Millions)', fontsize=12)

plt.legend(title='Continent', title_fontsize=12, fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(years, rotation=45)

plt.annotate('Rapid Growth in Asia', xy=(2023, 2900), xytext=(2025, 2500), 
             arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=10, color='darkred')

plt.tight_layout()
plt.show()