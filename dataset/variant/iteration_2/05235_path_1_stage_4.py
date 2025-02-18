import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

north_region = np.array([1, 2, 4, 8, 15, 25, 38, 50, 70, 85, 100])
south_region = np.array([0, 1, 2, 5, 10, 18, 28, 37, 50, 60, 75])
west_region = np.array([0, 0, 0, 1, 4, 8, 14, 22, 32, 44, 55])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, north_region, south_region, west_region,
             colors=['#1E90FF', '#32CD32', '#FF4500'], alpha=0.8)

ax.set_title("EV Growth in EcoLand (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Timeline", fontsize=12)
ax.set_ylabel("EV Adoption (Thousands)", fontsize=12)
ax.set_xlim(years.min(), years.max())
ax.set_ylim(0, 220)

ax.annotate('Eco Policy Introduction', xy=(2015, 12), xytext=(2013, 50),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)
ax.annotate('Major Growth Surge', xy=(2018, 130), xytext=(2016, 170),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()