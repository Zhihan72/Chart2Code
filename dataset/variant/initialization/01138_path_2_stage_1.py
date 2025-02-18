import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])
video_streaming = np.array([20, 23, 29, 35, 40])
social_networking = np.array([18, 19, 21, 22, 25])
online_news = np.array([12, 13, 15, 17, 16])
podcasts = np.array([5, 7, 10, 12, 15])
gaming = np.array([8, 9, 10, 14, 18])

platforms = [video_streaming, social_networking, online_news, podcasts, gaming]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

plt.figure(figsize=(12, 7))
plt.stackplot(years, *platforms, colors=colors, alpha=0.8)

plt.xticks(years, fontsize=10)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Monthly Engagement Hours', fontsize=12)

plt.tight_layout()
plt.show()