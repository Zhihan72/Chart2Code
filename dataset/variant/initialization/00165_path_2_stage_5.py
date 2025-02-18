import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)

# Define data for each region
north_america_arabica = np.array([120, 125, 130, 140, 145, 150, 160, 170, 180, 195, 210])
north_america_robusta = np.array([40, 42, 43, 45, 47, 50, 53, 56, 60, 65, 70])
north_america_liberica = np.array([5, 5, 5, 6, 6, 7, 8, 9, 10, 11, 12])

europe_arabica = -1 * np.array([150, 155, 160, 165, 170, 175, 180, 190, 200, 210, 220])
europe_robusta = -1 * np.array([50, 52, 55, 57, 60, 63, 67, 72, 77, 83, 90])
europe_liberica = -1 * np.array([8, 9, 10, 12, 14, 16, 19, 21, 24, 27, 30])

asia_arabica = np.array([130, 132, 134, 136, 138, 140, 145, 150, 155, 162, 170])
asia_robusta = np.array([100, 105, 110, 115, 120, 125, 130, 140, 150, 160, 170])
asia_liberica = np.array([10, 11, 12, 13, 15, 17, 20, 23, 26, 30, 35])

# Initialize figure
fig, ax = plt.subplots(figsize=(12, 8))

# Plot stacked bars for each region diverging from the central axis (0)
ax.bar(years, north_america_arabica, color='darkblue', label='NA Arabica', width=0.7)
ax.bar(years, north_america_robusta, bottom=north_america_arabica, color='orange', label='NA Robusta', width=0.7)
ax.bar(years, north_america_liberica, bottom=north_america_arabica + north_america_robusta, color='pink', label='NA Liberica', width=0.7)

ax.bar(years, europe_arabica, color='purple', label='EU Arabica', width=0.7)
ax.bar(years, europe_robusta, bottom=europe_arabica, color='lime', label='EU Robusta', width=0.7)
ax.bar(years, europe_liberica, bottom=europe_arabica + europe_robusta, color='beige', label='EU Liberica', width=0.7)

ax.bar(years, asia_arabica, color='indigo', label='AS Arabica', width=0.7)
ax.bar(years, asia_robusta, bottom=asia_arabica, color='khaki', label='AS Robusta', width=0.7)
ax.bar(years, asia_liberica, bottom=asia_arabica + asia_robusta, color='salmon', label='AS Liberica', width=0.7)

# Enhance plot aesthetics
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Coffee Use Volume (Millions)", fontsize=12)
ax.set_title("Diverging Coffee Types over Time", fontsize=16)

plt.xticks(years, rotation=45)
plt.axhline(0, color='grey', linewidth=0.8)  # Add central axis line
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()