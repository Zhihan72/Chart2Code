import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2024)

streaming_services = np.array([30, 40, 55, 65, 75, 90, 100, 115, 130, 150, 170])
online_gaming = np.array([15, 20, 22, 24, 28, 35, 45, 50, 58, 70, 85])
social_media = np.array([10, 12, 15, 20, 25, 35, 50, 60, 80, 100, 130])
cloud_storage = np.array([5, 8, 10, 14, 18, 25, 33, 50, 67, 85, 110])
video_conferencing = np.array([2, 3, 5, 7, 10, 12, 20, 30, 40, 55, 70])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, streaming_services, marker='o', linestyle='-', color='#e41a1c', linewidth=2, label='Streaming Services')
ax.plot(years, online_gaming, marker='s', linestyle='--', color='#377eb8', linewidth=2, label='Online Gaming')
ax.plot(years, social_media, marker='^', linestyle='-.', color='#4daf4a', linewidth=2, label='Social Media')
ax.plot(years, cloud_storage, marker='d', linestyle=':', color='#984ea3', linewidth=2, label='Cloud Storage')
ax.plot(years, video_conferencing, marker='h', linestyle='-', color='#ff7f00', linewidth=2, label='Video Conferencing')

ax.set_title('Internet Trends in FantasyLand', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Traffic (Petabytes)', fontsize=12)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

annotations = {
    2015: ("Mobile Surge", streaming_services[2]),
    2020: ("Global Gaming", online_gaming[7]),
    2023: ("Social Dominance", social_media[10]),
}

for year, (text, y_value) in annotations.items():
    ax.annotate(text, xy=(year, y_value), xytext=(year, y_value + 15),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5), fontsize=10, color='black', ha='center')

ax.legend(loc='upper left')
plt.tight_layout()
plt.show()