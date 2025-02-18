import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2024)

# Manually shuffled data maintaining original structure
video_streaming = [95, 135, 50, 250, 115, 220, 80, 280, 190, 65, 160]
music_streaming = [60, 95, 75, 40, 180, 135, 35, 115, 30, 160, 50]
podcasts = [18, 55, 25, 100, 70, 8, 5, 85, 33, 43, 12]
ebooks = [70, 35, 28, 22, 10, 15, 12, 18, 50, 42, 60]

media_types = np.array([video_streaming, music_streaming, podcasts, ebooks])

fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(years, media_types, colors=['purple', 'skyblue', 'limegreen', 'coral'], alpha=0.8)

ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Users (M)", fontsize=12)

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()