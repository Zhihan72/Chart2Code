import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)

drama_viewership = np.array([60, 35, 40, 50, 75, 55, 30, 80, 85, 70, 90])
comedy_viewership = np.array([25, 40, 20, 35, 65, 46, 50, 55, 30, 70, 60])
scifi_viewership = np.array([35, 20, 60, 15, 25, 40, 45, 50, 55, 65, 30])
horror_viewership = np.array([18, 14, 12, 10, 30, 40, 26, 45, 22, 35, 50])
fantasy_viewership = np.array([40, 22, 27, 33, 18, 50, 25, 45, 35, 55, 30])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, drama_viewership, '-o', color='orange', linewidth=2, markersize=6)
ax.plot(years, comedy_viewership, '-s', color='green', linewidth=2, markersize=6)
ax.plot(years, scifi_viewership, '-^', color='purple', linewidth=2, markersize=6)
ax.plot(years, horror_viewership, '-d', color='blue', linewidth=2, markersize=6)
ax.plot(years, fantasy_viewership, '-p', color='red', linewidth=2, markersize=6)

ax.set_title("TV Genre Popularity Over the Years\nViewership Trends (Millions)", fontsize=16, pad=20)
ax.set_xlabel("Timeline (Year)", fontsize=12)
ax.set_ylabel("Audience Size (Millions)", fontsize=12)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, fontsize=10)
ax.yaxis.set_tick_params(labelsize=10)

ax.annotate('Drama High Point',
            xy=(2025, 90), xytext=(2020, 60),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, ha='center')

ax.annotate('Sci-Fi Surge',
            xy=(2025, 30), xytext=(2018, 35),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, ha='center')

plt.tight_layout()
plt.show()