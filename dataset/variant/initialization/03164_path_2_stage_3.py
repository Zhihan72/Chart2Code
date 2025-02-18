import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2024)
video_streaming = [50, 65, 80, 95, 115, 135, 160, 190, 220, 250, 280]
music_streaming = [30, 35, 40, 50, 60, 75, 95, 115, 135, 160, 180]
podcasts = [5, 8, 12, 18, 25, 33, 43, 55, 70, 85, 100]

media_types = np.array([video_streaming, music_streaming, podcasts])

fig, ax = plt.subplots(figsize=(12, 7))

# Manually shuffled colors for the data groups
ax.stackplot(years, media_types, colors=['coral', 'skyblue', 'limegreen'], alpha=0.8)

ax.grid(True, linestyle='--', alpha=0.5)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()