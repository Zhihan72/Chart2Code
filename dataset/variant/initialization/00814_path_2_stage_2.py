import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2024)

streaming_services = np.array([30, 40, 55, 65, 75, 90, 100, 115, 130, 150, 170])
online_gaming = np.array([15, 20, 22, 24, 28, 35, 45, 50, 58, 70, 85])
social_media = np.array([10, 12, 15, 20, 25, 35, 50, 60, 80, 100, 130])

fig, ax = plt.subplots(figsize=(14, 8))

# Randomized stylistic elements
ax.plot(years, streaming_services, marker='x', linestyle=':', color='#e377c2', linewidth=1.5, label='Streamers')
ax.plot(years, online_gaming, marker='d', linestyle='-', color='#bcbd22', linewidth=2.5, label='Video Games')
ax.plot(years, social_media, marker='v', linestyle='--', color='#17becf', linewidth=1, label='SocMedia')

ax.set_title('Data Flow in Wonderland\nA Technological Voyage', fontsize=16, fontweight='normal', pad=15)
ax.set_xlabel('Timeline', fontsize=11)
ax.set_ylabel('Internet Data (in PB)', fontsize=11)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Changed legend style and position
ax.legend(title='Data Categories', loc='lower right', fontsize=8)

# Modified annotations for effect
annotations = {
    2015: ("Peak Streaming", streaming_services[2]),
    2020: ("Surge in Gaming", online_gaming[7]),
    2023: ("Dominant Social Media", social_media[10]),
}

for year, (text, y_value) in annotations.items():
    ax.annotate(text, xy=(year, y_value), xytext=(year, y_value + 15),
                arrowprops=dict(facecolor='gray', shrink=0.05, width=0.5, headwidth=3), fontsize=9, color='darkblue', ha='center')

# Altered grid and border
ax.grid(True, linestyle='-', alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()