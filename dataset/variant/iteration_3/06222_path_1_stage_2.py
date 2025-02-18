import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2011, 2021)

instagram = np.array([10, 15, 20, 25, 33, 45, 55, 60, 65, 70])
snapchat = np.array([0, 5, 12, 20, 25, 30, 40, 50, 55, 60])
facebook = np.array([20, 22, 24, 26, 28, 29, 30, 32, 34, 35])
twitter = np.array([10, 12, 15, 18, 22, 25, 27, 28, 30, 32])
tiktok = np.array([0, 0, 0, 0, 5, 15, 25, 35, 45, 55])

data = np.vstack([instagram, snapchat, facebook, twitter, tiktok])

fig, ax = plt.subplots(figsize=(12, 8))

# Changed color scheme
ax.stackplot(years, data, labels=['IG', 'SC', 'FB', 'TW', 'TT'], 
             colors=['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FFBD33'], alpha=0.8)

ax.set_title("Social Media Use (2011-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Avg Time (min)", fontsize=14)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.legend(loc='upper left', title='Platforms', fontsize=10, bbox_to_anchor=(1.05, 1))

plt.tight_layout()
plt.show()