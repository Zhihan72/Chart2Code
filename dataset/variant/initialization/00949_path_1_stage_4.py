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

# Manually changing stylistic elements including colors and marker types
new_colors = ['#99ccff', '#ff6666', '#66ff66', '#ffccff', '#ffff66', '#cc99ff', '#66ffcc']

plt.figure(figsize=(14, 8))
plt.stackplot(years, data, labels=['Telgm', 'Telph', 'Radio', 'TV', 'Net', 'Soc Med', 'Smartph'], 
              colors=new_colors, alpha=0.75)

plt.title('Comm Modes (1900-2000)', fontsize=18, fontweight='normal')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Units', fontsize=14)
plt.xlim(years[0], years[-1])
plt.ylim(0, 220)

# Manually altered grid style
plt.grid(True, linestyle='-.', linewidth=0.8, alpha=0.5)

plt.legend(loc='upper right', fontsize=9, title="Technologies", title_fontsize='11')

plt.xticks(years, rotation=30)

plt.annotate('Rise of Telephony', xy=(1950, 60), xytext=(1910, 150),
             arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=11)

plt.annotate('Internet Begins', xy=(2000, 60), xytext=(1970, 120),
             arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=11)

plt.tight_layout()

plt.show()