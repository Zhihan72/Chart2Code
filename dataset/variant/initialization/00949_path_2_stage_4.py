import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1900, 2010, 10)

telegrams = np.array([40, 35, 30, 20, 10, 5, 2, 1, 0, 0, 0])
telephones = np.array([5, 10, 20, 35, 50, 60, 70, 80, 85, 90, 95])
television = np.array([0, 0, 0, 0, 5, 15, 30, 45, 60, 70, 80])
internet = np.array([0, 0, 0, 0, 0, 0, 5, 15, 25, 40, 60])

data = np.array([telegrams, telephones, television, internet])

plt.figure(figsize=(14, 8))
plt.stackplot(years, data, labels=['Telegrams', 'Telephones', 'Television', 'Internet'],
              colors=['#ffeda0', '#fa9fb5', '#7481bf', '#a1dab4'], alpha=0.8)

plt.title('Evolution of Communication Methods in the 20th Century', fontsize=16, fontweight='bold')
plt.xlabel('Years', fontsize=12, fontstyle='italic')
plt.ylabel('Index', fontsize=12, fontstyle='italic')
plt.xlim(years[0], years[-1])
plt.ylim(0, 220)

plt.grid(True, linestyle='-', linewidth=0.7, alpha=0.5)

plt.legend(loc='best', fontsize=10, title="Communication Media", title_fontsize='11')

plt.xticks(years, rotation=0)

plt.annotate('Rise of Telephones', xy=(1960, 50), xytext=(1920, 120),
             arrowprops=dict(facecolor='blue', arrowstyle='->', lw=2), fontsize=10, fontweight='light')
plt.annotate('Online Revolution', xy=(2000, 45), xytext=(1990, 90),
             arrowprops=dict(facecolor='green', arrowstyle='-|>', lw=2), fontsize=10, fontweight='light')

plt.tight_layout()
plt.show()