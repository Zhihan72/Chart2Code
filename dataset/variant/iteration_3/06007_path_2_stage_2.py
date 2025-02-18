import matplotlib.pyplot as plt
import numpy as np

# Defining years and viewership data for each genre (in millions)
years = np.arange(2015, 2026)

drama_viewership = np.array([30, 35, 40, 50, 55, 60, 70, 75, 80, 85, 90])
comedy_viewership = np.array([20, 25, 30, 35, 40, 46, 50, 55, 60, 65, 70])
scifi_viewership = np.array([15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])
horror_viewership = np.array([10, 12, 14, 18, 22, 26, 30, 35, 40, 45, 50])
fantasy_viewership = np.array([18, 22, 25, 27, 30, 33, 35, 40, 45, 50, 55])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, drama_viewership, '-o', color='blue', linewidth=2, markersize=6)
ax.plot(years, comedy_viewership, '-s', color='orange', linewidth=2, markersize=6)
ax.plot(years, scifi_viewership, '-^', color='green', linewidth=2, markersize=6)
ax.plot(years, horror_viewership, '-d', color='red', linewidth=2, markersize=6)
ax.plot(years, fantasy_viewership, '-p', color='purple', linewidth=2, markersize=6)

ax.set_title("Popularity in Streaming: A Journey Through Genres\nTV Series Viewership from 2015 to 2025", fontsize=16, pad=20)
ax.set_xlabel("Timeline", fontsize=12)
ax.set_ylabel("Audience Count (Millions)", fontsize=12)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, fontsize=10)
ax.yaxis.set_tick_params(labelsize=10)

plt.tight_layout()

plt.show()