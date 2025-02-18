import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2024)

# Internet traffic data in petabytes (hypothetical)
streaming_services = np.array([30, 40, 55, 65, 75, 90, 100, 115, 130, 150, 170])
online_gaming = np.array([15, 20, 22, 24, 28, 35, 45, 50, 58, 70, 85])
social_media = np.array([10, 12, 15, 20, 25, 35, 50, 60, 80, 100, 130])

fig, ax = plt.subplots(figsize=(14, 8))

# Changed colors for the plots
ax.plot(years, streaming_services, marker='o', linestyle='-', color='#e41a1c', linewidth=2, label='Streaming')
ax.plot(years, online_gaming, marker='s', linestyle='--', color='#377eb8', linewidth=2, label='Gaming')
ax.plot(years, social_media, marker='^', linestyle='-.', color='#4daf4a', linewidth=2, label='Social')

ax.set_title('Internet Trends in FantasyLand', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Traffic (Petabytes)', fontsize=12)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

ax.legend(title='Media Types', loc='upper left', fontsize=10)

annotations = {
    2015: ("Mobile Surge", streaming_services[2]),
    2020: ("Global Gaming", online_gaming[7]),
    2023: ("Social Dominance", social_media[10]),
}

for year, (text, y_value) in annotations.items():
    ax.annotate(text, xy=(year, y_value), xytext=(year, y_value + 15),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5), fontsize=10, color='black', ha='center')

ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()