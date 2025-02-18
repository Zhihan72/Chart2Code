import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2031)
africa_north_users = np.array([110, 130, 155, 180, 210, 250, 310, 380, 440, 480, 520, 570, 620, 680, 740, 800, 860, 920, 980, 1040, 1100])
africa_south_users = np.array([30, 40, 60, 90, 120, 160, 200, 250, 310, 380, 450, 510, 580, 650, 720, 790, 860, 930, 1000, 1070, 1150])
asia_users = np.array([820, 860, 900, 950, 1000, 1060, 1130, 1210, 1300, 1400, 1520, 1660, 1810, 1970, 2150, 2350, 2580, 2820, 3080, 3360, 3650])
europe_users = np.array([500, 510, 520, 530, 540, 550, 570, 590, 610, 640, 670, 690, 710, 730, 740, 750, 760, 765, 770, 775, 780])
north_america_users = np.array([270, 275, 280, 285, 290, 295, 300, 310, 315, 320, 325, 330, 335, 338, 340, 345, 348, 350, 352, 353, 355])
south_america_users = np.array([160, 170, 185, 200, 220, 250, 280, 320, 360, 400, 440, 480, 510, 530, 550, 570, 590, 610, 630, 650, 670])
australia_users = np.array([30, 32, 34, 36, 38, 40, 42, 45, 48, 51, 54, 58, 62, 65, 68, 70, 72, 73, 74, 75, 76])
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