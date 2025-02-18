import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1990, 2021)

physical_media = np.array([90, 87, 85, 82, 76, 70, 65, 60, 55, 50, 45, 40, 35, 32, 28, 24, 20, 18, 15, 12, 10, 8, 6, 5, 4, 3, 3, 3, 2, 1, 1])
digital_downloads = np.array([0, 1, 2, 4, 6, 7, 8, 9, 12, 15, 20, 25, 30, 35, 40, 42, 45, 48, 50, 52, 53, 54, 56, 58, 60, 60, 58, 55, 50, 48, 45])
streaming = np.array([0, 0, 0, 0, 0, 0, 1, 2, 3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 48, 50, 55, 60, 62, 65, 68, 72, 75, 78, 82, 85, 88])
others = 100 - (physical_media + digital_downloads + streaming)

fig, ax = plt.subplots(figsize=(14, 8))

# Change colors for variation
colors = ['#FFD700', '#DA70D6', '#32CD32', '#FF6347']

ax.stackplot(years, physical_media, digital_downloads, streaming, others, 
             labels=['Physical Media', 'Digital Downloads', 'Streaming', 'Others'], 
             colors=colors, alpha=0.8)

ax.set_title("Evolution of Music Consumption Formats (1990-2020)", fontsize=16, fontweight='normal')
ax.set_xlabel("Year", fontsize=12, fontweight='normal')
ax.set_ylabel("Percentage of Total Consumption (%)", fontsize=12, fontweight='normal')

# Alter grid style
ax.grid(linestyle='-', linewidth=1, alpha=0.3)

# Change legend style
ax.legend(loc='upper right', fontsize=12, frameon=False)

plt.xticks(years[::5])

# Alter annotations
ax.annotate('Napster Launch', 
            xy=(1999, 50), xytext=(1997, 70), 
            arrowprops=dict(color='brown', arrowstyle='->'), fontsize=9)
ax.annotate('Streaming Rise', 
            xy=(2015, 35), xytext=(2011, 40), 
            arrowprops=dict(color='green', arrowstyle='-|>'), fontsize=9)

plt.tight_layout()
plt.show()