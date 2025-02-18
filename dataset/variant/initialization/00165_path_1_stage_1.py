import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2020, 2031)

# Original data for coffee consumption (in million kg) by coffee type for each region
north_america_arabica = [120, 125, 130, 140, 145, 150, 160, 170, 180, 195, 210]
north_america_robusta = [40, 42, 43, 45, 47, 50, 53, 56, 60, 65, 70]
north_america_liberica = [5, 5, 5, 6, 6, 7, 8, 9, 10, 11, 12]

europe_arabica = [150, 155, 160, 165, 170, 175, 180, 190, 200, 210, 220]
europe_robusta = [50, 52, 55, 57, 60, 63, 67, 72, 77, 83, 90]
europe_liberica = [8, 9, 10, 12, 14, 16, 19, 21, 24, 27, 30]

asia_arabica = [130, 132, 134, 136, 138, 140, 145, 150, 155, 162, 170]
asia_robusta = [100, 105, 110, 115, 120, 125, 130, 140, 150, 160, 170]
asia_liberica = [10, 11, 12, 13, 15, 17, 20, 23, 26, 30, 35]

# New Data: Introducing additional regions, Africa and South America
africa_arabica = [50, 52, 54, 56, 58, 60, 62, 65, 68, 72, 76]
africa_robusta = [30, 32, 34, 36, 38, 40, 42, 45, 48, 52, 55]
africa_liberica = [5, 5, 6, 6, 7, 8, 8, 9, 10, 11, 12]

south_america_arabica = [200, 205, 210, 215, 220, 230, 240, 250, 260, 275, 290]
south_america_robusta = [70, 73, 75, 78, 82, 86, 90, 95, 100, 106, 112]
south_america_liberica = [12, 13, 14, 15, 16, 17, 18, 20, 22, 24, 26]

# Calculate cumulative heights for stacked bar chart with added regions
cumulative_north_america = np.array(north_america_arabica) + np.array(north_america_robusta) + np.array(north_america_liberica)
cumulative_europe = cumulative_north_america + np.array(europe_arabica) + np.array(europe_robusta) + np.array(europe_liberica)
cumulative_asia = cumulative_europe + np.array(asia_arabica) + np.array(asia_robusta) + np.array(asia_liberica)
cumulative_africa = cumulative_asia + np.array(africa_arabica) + np.array(africa_robusta) + np.array(africa_liberica)

# Create a new figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Existing regions
ax.bar(years, north_america_arabica, label='NA - Arabica', color='c', width=0.7)
ax.bar(years, north_america_robusta, bottom=north_america_arabica, label='NA - Robusta', color='m', width=0.7)
ax.bar(years, north_america_liberica, bottom=np.array(north_america_arabica) + np.array(north_america_robusta), label='NA - Liberica', color='y', width=0.7)

ax.bar(years, europe_arabica, bottom=np.array(cumulative_north_america), label='Europe - Arabica', color='b', width=0.7)
ax.bar(years, europe_robusta, bottom=np.array(cumulative_north_america) + np.array(europe_arabica), label='Europe - Robusta', color='g', width=0.7)
ax.bar(years, europe_liberica, bottom=np.array(cumulative_north_america) + np.array(europe_arabica) + np.array(europe_robusta), label='Europe - Liberica', color='r', width=0.7)

ax.bar(years, asia_arabica, bottom=np.array(cumulative_europe), label='Asia - Arabica', color='lightcoral', width=0.7)
ax.bar(years, asia_robusta, bottom=np.array(cumulative_europe) + np.array(asia_arabica), label='Asia - Robusta', color='plum', width=0.7)
ax.bar(years, asia_liberica, bottom=np.array(cumulative_europe) + np.array(asia_arabica) + np.array(asia_robusta), label='Asia - Liberica', color='tan', width=0.7)

# New Regions
ax.bar(years, africa_arabica, bottom=np.array(cumulative_asia), label='Africa - Arabica', color='gold', width=0.7)
ax.bar(years, africa_robusta, bottom=np.array(cumulative_asia) + np.array(africa_arabica), label='Africa - Robusta', color='orange', width=0.7)
ax.bar(years, africa_liberica, bottom=np.array(cumulative_asia) + np.array(africa_arabica) + np.array(africa_robusta), label='Africa - Liberica', color='mediumseagreen', width=0.7)

ax.bar(years, south_america_arabica, bottom=np.array(cumulative_africa), label='SA - Arabica', color='dodgerblue', width=0.7)
ax.bar(years, south_america_robusta, bottom=np.array(cumulative_africa) + np.array(south_america_arabica), label='SA - Robusta', color='purple', width=0.7)
ax.bar(years, south_america_liberica, bottom=np.array(cumulative_africa) + np.array(south_america_arabica) + np.array(south_america_robusta), label='SA - Liberica', color='pink', width=0.7)

# Chart configuration
ax.set_title("Global Coffee Consumption by Region and Source (2020-2030)", fontsize=14, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Coffee Consumption (Million Kg)", fontsize=12)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Region and Source')
ax.grid(alpha=0.3)
plt.xticks(years, rotation=45)
plt.tight_layout()
plt.show()