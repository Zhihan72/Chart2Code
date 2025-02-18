import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)

north_america_arabica = [120, 125, 130, 140, 145, 150, 160, 170, 180, 195, 210]
north_america_robusta = [40, 42, 43, 45, 47, 50, 53, 56, 60, 65, 70]
north_america_liberica = [5, 5, 5, 6, 6, 7, 8, 9, 10, 11, 12]

europe_arabica = [150, 155, 160, 165, 170, 175, 180, 190, 200, 210, 220]
europe_robusta = [50, 52, 55, 57, 60, 63, 67, 72, 77, 83, 90]
europe_liberica = [8, 9, 10, 12, 14, 16, 19, 21, 24, 27, 30]

asia_arabica = [130, 132, 134, 136, 138, 140, 145, 150, 155, 162, 170]
asia_robusta = [100, 105, 110, 115, 120, 125, 130, 140, 150, 160, 170]
asia_liberica = [10, 11, 12, 13, 15, 17, 20, 23, 26, 30, 35]

south_america_arabica = [110, 115, 120, 125, 130, 135, 145, 155, 160, 170, 180]
south_america_robusta = [30, 32, 35, 37, 40, 42, 45, 50, 55, 60, 65]
south_america_liberica = [6, 7, 8, 9, 10, 12, 14, 15, 17, 18, 20]

cumulative_north_america = np.array(north_america_arabica) + np.array(north_america_robusta) + np.array(north_america_liberica)
cumulative_europe = cumulative_north_america + np.array(europe_arabica) + np.array(europe_robusta) + np.array(europe_liberica)
cumulative_asia = cumulative_europe + np.array(asia_arabica) + np.array(asia_robusta) + np.array(asia_liberica)
cumulative_south_america = cumulative_asia + np.array(south_america_arabica) + np.array(south_america_robusta) + np.array(south_america_liberica)

fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(years, north_america_arabica, color='darkblue', width=0.7)
ax.bar(years, north_america_robusta, bottom=north_america_arabica, color='orange', width=0.7)
ax.bar(years, north_america_liberica, bottom=np.array(north_america_arabica) + np.array(north_america_robusta), color='pink', width=0.7)

ax.bar(years, europe_arabica, bottom=np.array(cumulative_north_america), color='purple', width=0.7)
ax.bar(years, europe_robusta, bottom=np.array(cumulative_north_america) + np.array(europe_arabica), color='lime', width=0.7)
ax.bar(years, europe_liberica, bottom=np.array(cumulative_north_america) + np.array(europe_arabica) + np.array(europe_robusta), color='beige', width=0.7)

ax.bar(years, asia_arabica, bottom=np.array(cumulative_europe), color='indigo', width=0.7)
ax.bar(years, asia_robusta, bottom=np.array(cumulative_europe) + np.array(asia_arabica), color='khaki', width=0.7)
ax.bar(years, asia_liberica, bottom=np.array(cumulative_europe) + np.array(asia_arabica) + np.array(asia_robusta), color='salmon', width=0.7)

ax.bar(years, south_america_arabica, bottom=np.array(cumulative_asia), color='mediumseagreen', width=0.7)
ax.bar(years, south_america_robusta, bottom=np.array(cumulative_asia) + np.array(south_america_arabica), color='teal', width=0.7)
ax.bar(years, south_america_liberica, bottom=np.array(cumulative_asia) + np.array(south_america_arabica) + np.array(south_america_robusta), color='silver', width=0.7)

ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Coffee Consumption (Million Kg)", fontsize=12)

plt.xticks(years, rotation=45)
plt.tight_layout()
plt.show()