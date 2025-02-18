import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2011, 2021)
instagram = np.array([10, 15, 20, 25, 33, 45, 55, 60, 65, 70])
snapchat = np.array([0, 5, 12, 20, 25, 30, 40, 50, 55, 60])
facebook = np.array([20, 22, 24, 26, 28, 29, 30, 32, 34, 35])
twitter = np.array([10, 12, 15, 18, 22, 25, 27, 28, 30, 32])
tiktok = np.array([0, 0, 0, 0, 5, 15, 25, 35, 45, 55])
youtube = np.array([5, 7, 10, 15, 22, 30, 38, 45, 50, 55])

data = np.vstack([instagram, snapchat, facebook, twitter, tiktok, youtube])

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, data, colors=['#FF69B4', '#4169E1', '#32CD32', '#FFD700', '#8A2BE2', '#FF6347'], alpha=0.7)

ax.set_xticks(years)
ax.set_xticklabels([], rotation=30)  # Remove the labels but keep the ticks for guidance

ax.grid(axis='x', linestyle=':', alpha=0.5)
ax.legend([], loc='upper right')  # Removing the legend labels

plt.tight_layout()
plt.show()