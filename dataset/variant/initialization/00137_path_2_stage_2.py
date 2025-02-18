import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

mp3_popularity = [30, 40, 55, 70, 75, 80, 85, 88, 90, 87, 80, 78, 75, 70, 65, 60, 55, 50, 40, 35, 30]
aac_popularity = [10, 15, 25, 35, 45, 50, 55, 60, 65, 68, 70, 75, 78, 80, 85, 88, 90, 92, 93, 92, 90]
flac_popularity = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 88, 90, 92, 94]
streaming_popularity = [0, 0, 0, 0, 5, 10, 15, 25, 30, 40, 50, 60, 70, 75, 80, 85, 88, 90, 92, 94, 95]

fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(10, 12))

# First subplot
ax[0].plot(years, mp3_popularity, marker='o', linestyle='-', linewidth=2, color='b')
ax[0].plot(years, aac_popularity, marker='s', linestyle='--', linewidth=2, color='g')
ax[0].plot(years, flac_popularity, marker='^', linestyle='-.', linewidth=2, color='r')
ax[0].fill_between(years, mp3_popularity, color='b', alpha=0.1)
ax[0].fill_between(years, aac_popularity, color='g', alpha=0.1)
ax[0].fill_between(years, flac_popularity, color='r', alpha=0.1)
ax[0].set_title('Popularity of Digital Music Formats (2000-2020)', fontsize=14, pad=20)
ax[0].set_xlabel('Year', fontsize=12)
ax[0].set_ylabel('Popularity Index', fontsize=12)
ax[0].set_xticks(years)
ax[0].set_xticklabels(years, rotation=45)
ax[0].set_yticks(np.arange(0, 101, 10))
ax[0].annotate('Peak MP3', xy=(2007, 90), xytext=(2003, 95), arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=10, color='blue')
ax[0].annotate('Peak AAC', xy=(2020, 90), xytext=(2015, 95), arrowprops=dict(facecolor='green', shrink=0.05), fontsize=10, color='green')
ax[0].annotate('Peak FLAC', xy=(2020, 94), xytext=(2016, 98), arrowprops=dict(facecolor='red', shrink=0.05), fontsize=10, color='red')

# Second subplot
ax[1].bar(years, streaming_popularity, color='cyan')
ax[1].set_title('Rise of Streaming Services (2000-2020)', fontsize=14, pad=20)
ax[1].set_xlabel('Year', fontsize=12)
ax[1].set_ylabel('Popularity Index', fontsize=12)
ax[1].set_xticks(years)
ax[1].set_xticklabels(years, rotation=45)
ax[1].set_yticks(np.arange(0, 101, 10))

plt.tight_layout()
plt.show()