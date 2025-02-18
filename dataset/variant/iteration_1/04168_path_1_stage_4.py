import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1990, 2021)

physical_media = np.array([90, 87, 85, 82, 76, 70, 65, 60, 55, 50, 45, 40, 35, 32, 28, 24, 20, 18, 15, 12, 10, 8, 6, 5, 4, 3, 3, 3, 2, 1, 1])
digital_downloads = np.array([0, 1, 2, 4, 6, 7, 8, 9, 12, 15, 20, 25, 30, 35, 40, 42, 45, 48, 50, 52, 53, 54, 56, 58, 60, 60, 58, 55, 50, 48, 45])
streaming = np.array([0, 0, 0, 0, 0, 0, 1, 2, 3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 48, 50, 55, 60, 62, 65, 68, 72, 75, 78, 82, 85, 88])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, physical_media, digital_downloads, streaming, 
             labels=['Phys', 'D-Load', 'Stream'], 
             colors=['#ff9999', '#66b3ff', '#99ff99'], alpha=0.85)

ax.set_title("Music Formats (1990-2020)", fontsize=18, fontweight='bold')
ax.set_xlabel("Yr", fontsize=14, fontweight='semibold')
ax.set_ylabel("Pct Use (%)", fontsize=14, fontweight='semibold')

ax.grid(linestyle=':', linewidth=1, alpha=0.7)
ax.legend(loc='best', fontsize=12, edgecolor='blue', shadow=True)

plt.xticks(years[::3], rotation=45)

ax.annotate('Napster Launch', xy=(1999, 50), xytext=(2001, 70),
            arrowprops=dict(facecolor='red', arrowstyle='-|>'), fontsize=10)
ax.annotate('Rise of Stream', xy=(2015, 35), xytext=(2010, 50), 
            arrowprops=dict(facecolor='green', arrowstyle='-|>'), fontsize=10)
ax.annotate('Covid Pandemic', xy=(2020, 75), xytext=(2014, 80), 
            arrowprops=dict(facecolor='orange', arrowstyle='<|-'), fontsize=10)

for spine in ax.spines.values():
    spine.set_edgecolor('purple')
    spine.set_linewidth(1.5)

plt.tight_layout()
plt.show()