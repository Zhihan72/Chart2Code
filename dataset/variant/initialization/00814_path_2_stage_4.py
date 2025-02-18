import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2024)

# Randomly altering content within data groups while preserving structure
streaming_services = np.array([100, 65, 40, 130, 30, 75, 115, 90, 170, 55, 150])
online_gaming = np.array([45, 70, 35, 15, 50, 85, 28, 22, 20, 24, 58])
social_media = np.array([60, 130, 12, 25, 10, 80, 35, 20, 15, 50, 100])

fig, ax = plt.subplots(figsize=(14, 8))

# Updated color scheme remains the same
ax.plot(years, streaming_services, marker='x', linestyle=':', color='#ff5733', linewidth=1.5, label='Streamers')
ax.plot(years, online_gaming, marker='d', linestyle='-', color='#33ff57', linewidth=2.5, label='Video Games')
ax.plot(years, social_media, marker='v', linestyle='--', color='#3357ff', linewidth=1, label='SocMedia')

ax.set_title('Data Flow in Wonderland\nA Technological Voyage', fontsize=16, fontweight='normal', pad=15)
ax.set_xlabel('Timeline', fontsize=11)
ax.set_ylabel('Internet Data (in PB)', fontsize=11)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

ax.legend(title='Data Categories', loc='lower right', fontsize=8)

# Updated annotations
annotations = {
    2015: ("Peak Streaming", streaming_services[2]),
    2020: ("Surge in Gaming", online_gaming[7]),
    2023: ("Dominant Social Media", social_media[1]),
}

for year, (text, y_value) in annotations.items():
    ax.annotate(text, xy=(year, y_value), xytext=(year, y_value + 15),
                arrowprops=dict(facecolor='gray', shrink=0.05, width=0.5, headwidth=3), fontsize=9, color='darkblue', ha='center')

ax.grid(True, linestyle='-', alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()