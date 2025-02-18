import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2011, 2021)

instagram = np.array([10, 15, 20, 25, 33, 45, 55, 60, 65, 70])
snapchat = np.array([0, 5, 12, 20, 25, 30, 40, 50, 55, 60])
facebook = np.array([20, 22, 24, 26, 28, 29, 30, 32, 34, 35])
twitter = np.array([10, 12, 15, 18, 22, 25, 27, 28, 30, 32])
tiktok = np.array([0, 0, 0, 0, 5, 15, 25, 35, 45, 55])
bytetrend = np.array([3, 6, 9, 12, 15, 18, 21, 24, 27, 30])  # New data series

data = np.vstack([instagram, snapchat, facebook, twitter, tiktok, bytetrend])

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, data, labels=['IG', 'SC', 'FB', 'TW', 'TT', 'BT'], 
             colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'], alpha=0.8, linestyle='-.')

ax.set_title("Social Media Use (2011-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Avg Time (min)", fontsize=14)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

ax.grid(axis='x', linestyle=':', alpha=0.5)

ax.legend(loc='center right', title='Platforms', fontsize=10, bbox_to_anchor=(1.25, 0.5), borderaxespad=0, shadow=True)

for spine in ax.spines.values():
    spine.set_linewidth(1.5)
    spine.set_edgecolor('#333333')

plt.tight_layout()
plt.show()