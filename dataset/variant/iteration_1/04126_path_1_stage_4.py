import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Fictional data representing hours spent weekly on different digital media
streaming_services = np.array([12, 17, 22, 28, 35, 42, 50, 2, 3, 5, 8])
social_media = np.array([22, 25, 30, 34, 38, 4, 6, 9, 11, 14, 18])
online_news = np.array([11, 14, 16, 19, 21, 23, 25, 3, 5, 7, 9])
podcasts = np.array([8, 9, 11, 13, 15, 1, 2, 3, 4, 5, 6])

media_data = np.vstack([streaming_services, social_media, online_news, podcasts])

fig, ax = plt.subplots(figsize=(14, 8))

# Maintain the stackplot without labels and legend
ax.stackplot(years, media_data, colors=['#1e90ff'], alpha=0.8)

# Customizing border style
for spine in ax.spines.values():
    spine.set_color('darkred')
    spine.set_linewidth(1.5)

plt.tight_layout()
plt.show()