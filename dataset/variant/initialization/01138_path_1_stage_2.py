import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])

video_streaming = np.array([22, 25, 27, 37, 38])
social_networking = np.array([17, 20, 19, 24, 24])
online_news = np.array([14, 12, 16, 18, 14])
podcasts = np.array([6, 8, 9, 11, 13])
gaming = np.array([10, 8, 11, 13, 20])

platforms = [video_streaming, social_networking, online_news, podcasts, gaming]
platform_labels = ['Video Streaming', 'Social Networking', 'Online News', 'Podcasts', 'Gaming']
colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231']  # New set of colors

plt.figure(figsize=(12, 7))
plt.stackplot(years, *platforms, labels=platform_labels, colors=colors, alpha=0.8)
plt.title('Trends in Digital Content Consumption (2018-2022)', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Monthly Engagement Hours', fontsize=12)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Platforms', fontsize=10)
plt.xticks(years, fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()