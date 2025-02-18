import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
mp3_popularity = [30, 40, 55, 70, 75, 80, 85, 88, 90, 87, 80, 78, 75, 70, 65, 60, 55, 50, 40, 35, 30]
aac_popularity = [10, 15, 25, 35, 45, 50, 55, 60, 65, 68, 70, 75, 78, 80, 85, 88, 90, 92, 93, 92, 90]
streaming_popularity = [0, 0, 0, 0, 5, 10, 15, 25, 30, 40, 50, 60, 70, 75, 80, 85, 88, 90, 92, 94, 95]

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# Line plot for music formats
ax[0].plot(years, mp3_popularity, marker='x', linestyle='--', linewidth=2, color='blue', label='MP3')
ax[0].plot(years, aac_popularity, marker='p', linestyle=':', linewidth=2, color='blue', label='AAC')
ax[0].fill_between(years, mp3_popularity, color='blue', alpha=0.2)
ax[0].fill_between(years, aac_popularity, color='blue', alpha=0.2)
ax[0].set_title('Music Formats (2000-20)', fontsize=14, pad=20)
ax[0].set_xlabel('Yr', fontsize=12)
ax[0].set_ylabel('Pop Index', fontsize=12)
ax[0].set_xticks(years)
ax[0].set_xticklabels(years, rotation=45)
ax[0].set_yticks(np.arange(0, 101, 10))
ax[0].grid(True, which='major', linestyle='-', linewidth=0.7, alpha=0.5)
ax[0].legend(loc='lower right', fontsize=10, title='Formats', title_fontsize='13')

ax[0].annotate('MP3 Peak', xy=(2007, 90), xytext=(2003, 95), arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=10, color='blue')
ax[0].annotate('AAC Peak', xy=(2020, 90), xytext=(2015, 95), arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=10, color='blue')

# Sort the streaming popularity data and plot sorted bar chart
sorted_years = [x for _, x in sorted(zip(streaming_popularity, years), key=lambda pair: pair[0])]
sorted_streaming_popularity = sorted(streaming_popularity)

ax[1].bar(sorted_years, sorted_streaming_popularity, color='blue', edgecolor='blue', hatch='/', label='Streaming')
ax[1].set_title('Streaming Growth (Sorted) (2000-20)', fontsize=14, pad=20)
ax[1].set_xlabel('Yr', fontsize=12)
ax[1].set_ylabel('Pop Index', fontsize=12)
ax[1].set_xticks(sorted_years)
ax[1].set_xticklabels(sorted_years, rotation=45)
ax[1].set_yticks(np.arange(0, 101, 10))
ax[1].grid(True, which='both', linestyle='-', linewidth=0.5, alpha=0.3)
ax[1].legend(loc='upper left', fontsize=11, title='Format', title_fontsize='13')

plt.tight_layout()
plt.show()