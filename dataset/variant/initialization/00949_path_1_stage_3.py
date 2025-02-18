import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1900, 2010, 10)

telegrams = np.array([40, 35, 30, 20, 10, 5, 2, 1, 0, 0, 0])
telephones = np.array([5, 10, 20, 35, 50, 60, 70, 80, 85, 90, 95])
radio = np.array([0, 0, 5, 15, 25, 40, 50, 40, 30, 20, 10])
television = np.array([0, 0, 0, 0, 5, 15, 30, 45, 60, 70, 80])
internet = np.array([0, 0, 0, 0, 0, 0, 5, 15, 25, 40, 60])
social_media = np.array([0, 0, 0, 0, 0, 0, 0, 10, 30, 50, 70])
smartphones = np.array([0, 0, 0, 0, 0, 0, 0, 5, 20, 40, 65])

data = np.array([telegrams, telephones, radio, television, internet, social_media, smartphones])

shuffled_colors = ['#ffb366', '#c2c2f0', '#66b2ff', '#ff9999', '#b3b3ff', '#99ff99', '#ffcc99']

plt.figure(figsize=(14, 8))
plt.stackplot(years, data, labels=['Telgm', 'Telph', 'Radio', 'TV', 'Net', 'Soc Med', 'Smartph'], 
              colors=shuffled_colors, alpha=0.85)

plt.title('Comm Modes (1900-2000)', fontsize=16, fontweight='bold')
plt.xlabel('Yr', fontsize=12)
plt.ylabel('Units', fontsize=12)
plt.xlim(years[0], years[-1])
plt.ylim(0, 220)

plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.legend(loc='upper left', fontsize=10, title="Comm Techs")

plt.xticks(years, rotation=45)

plt.annotate('Rise of Telph', xy=(1950, 60), xytext=(1920, 130),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, fontweight='bold')
plt.annotate('Net Starts', xy=(2000, 60), xytext=(1980, 100),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, fontweight='bold')

plt.tight_layout()

plt.show()