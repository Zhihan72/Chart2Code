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

# Applied a single color consistently across all groups
ax.stackplot(years, media_data, labels=['Podcasts', 'Online News', 'Social Media', 'Streaming Services'], 
             colors=['#1e90ff'], alpha=0.8)

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Weekly Hours', fontsize=14)
ax.set_title("Digital Media Consumption (2010-2020)", fontsize=18, fontweight='bold')

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=0)

# Customizing border style
for spine in ax.spines.values():
    spine.set_color('darkred')
    spine.set_linewidth(1.5)

# Add legend on top of the plot
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=4, title='Media Categories', markerscale=0.9)

ax.annotate('Streaming Booms', xy=(2018, 42), xytext=(2016, 47), 
            arrowprops=dict(facecolor='darkred', arrowstyle='->'), fontsize=12)

ax.annotate('Podcasts Rise', xy=(2020, 58), xytext=(2018, 65), 
            arrowprops=dict(facecolor='darkred', arrowstyle='->'), fontsize=12)

plt.tight_layout()
plt.show()