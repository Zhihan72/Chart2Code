import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2031)
africa_north_users = np.array([130, 110, 180, 155, 250, 210, 310, 380, 480, 440, 570, 520, 680, 620, 800, 740, 920, 860, 1040, 980, 1100])
africa_south_users = np.array([40, 30, 90, 60, 160, 120, 200, 250, 380, 310, 510, 450, 650, 580, 790, 720, 930, 860, 1070, 1000, 1150])
asia_users = np.array([860, 820, 950, 900, 1060, 1000, 1210, 1130, 1400, 1300, 1660, 1520, 1970, 1810, 2350, 2150, 2820, 2580, 3360, 3080, 3650])
europe_users = np.array([510, 500, 530, 520, 550, 540, 590, 570, 640, 610, 690, 670, 730, 710, 750, 740, 765, 760, 775, 770, 780])
north_america_users = np.array([275, 270, 285, 280, 295, 290, 310, 300, 320, 315, 330, 325, 338, 335, 345, 340, 350, 348, 353, 352, 355])
south_america_users = np.array([170, 160, 200, 185, 250, 220, 320, 280, 400, 360, 480, 440, 530, 510, 570, 550, 610, 590, 650, 630, 670])
australia_users = np.array([32, 30, 36, 34, 40, 38, 45, 42, 51, 48, 58, 54, 65, 62, 70, 68, 73, 72, 75, 74, 76])
africa_users = africa_north_users + africa_south_users

colors = ['#8A2BE2', '#FFD700', '#1E90FF', '#FF69B4', '#FF4500', '#00FF00']

plt.figure(figsize=(16, 9))

plt.stackplot(years, africa_users, asia_users, europe_users, north_america_users, south_america_users, australia_users, 
              labels=['Afrique', 'Asie', 'Europe', 'Amérique du Nord', 'Amérique du Sud', 'Australie'], colors=colors, alpha=0.6)

plt.title('Internet Users Growth by Region\n(Annual Data 2010-2030)', fontsize=17, fontweight='bold', pad=25)
plt.xlabel('Year', fontsize=13)
plt.ylabel('Internet Users (millions)', fontsize=13)

plt.legend(title='Region', title_fontsize=13, fontsize=11, loc='upper right', bbox_to_anchor=(0.85, 0.95))

plt.grid(True, linestyle='-.', lw=1, alpha=0.6)
plt.xticks(years, rotation=30)
plt.annotate('Rapid Growth in Asia', xy=(2023, 2900), xytext=(2026, 2500), 
             arrowprops=dict(arrowstyle='-|>', lw=1.5, color='navy'), fontsize=11, color='darkgreen')

plt.tight_layout()
plt.show()