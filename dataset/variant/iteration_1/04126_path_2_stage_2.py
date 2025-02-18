import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

streaming_services = np.array([2, 3, 5, 8, 12, 17, 22, 28, 35, 42, 50])
social_media = np.array([4, 6, 9, 11, 14, 18, 22, 25, 30, 34, 38])
online_news = np.array([3, 5, 7, 9, 11, 14, 16, 19, 21, 23, 25])
podcasts = np.array([1, 2, 3, 4, 5, 6, 8, 9, 11, 13, 15])

media_data = np.vstack([streaming_services, social_media, online_news, podcasts])

fig, ax = plt.subplots(figsize=(14, 8))

# Apply a single color across all data groups
ax.stackplot(years, media_data, labels=['Podcasts', 'Online News', 'Social Media', 'Streaming Services'], 
             colors=['#1e90ff'], alpha=0.7)

ax.set_xlabel('Year', fontsize=16)
ax.set_ylabel('Weekly Hours', fontsize=12)
ax.set_title("Digital Media Usage Trends (2010-2020)", fontsize=20, fontweight='normal')

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

ax.grid(True, which='minor', linestyle='-.', linewidth=0.7, color='purple', alpha=0.5)

ax.legend(loc='upper right', bbox_to_anchor=(0.8, 0.95), title='Media Types')

ax.annotate('Podcast Growth', xy=(2019, 58), xytext=(2018, 65),
            arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=14)

plt.tight_layout()

plt.show()