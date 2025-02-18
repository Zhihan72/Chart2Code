import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])
video_streaming = np.array([20, 23, 29, 35, 40])
online_news = np.array([12, 13, 15, 17, 16])
gaming = np.array([8, 9, 10, 14, 18])

platforms = [video_streaming, online_news, gaming]
colors = ['#1f77b4', '#2ca02c', '#9467bd']

plt.figure(figsize=(12, 7))
plt.stackplot(years, *platforms, colors=colors, alpha=0.8)

plt.xticks(years, fontsize=10)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Monthly Engagement Hours', fontsize=12)

plt.tight_layout()
plt.show()