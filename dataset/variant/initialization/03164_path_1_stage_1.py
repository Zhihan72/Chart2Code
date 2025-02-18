import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2024)

video_streaming = [50, 65, 80, 95, 115, 135, 160, 190, 220, 250, 280]
music_streaming = [30, 35, 40, 50, 60, 75, 95, 115, 135, 160, 180]
podcasts = [5, 8, 12, 18, 25, 33, 43, 55, 70, 85, 100]
ebooks = [10, 12, 15, 18, 22, 28, 35, 42, 50, 60, 70]

media_types = np.array([video_streaming, music_streaming, podcasts, ebooks])

fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(years, media_types, colors=['skyblue', 'limegreen', 'coral', 'purple'], alpha=0.8)

ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Consumption (Millions of Users)", fontsize=12)

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()