import matplotlib.pyplot as plt
import numpy as np

years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
netflix_popularity = np.array([82, 88, 78, 92, 95, 85, 97, 93, 96])
amazon_prime_popularity = np.array([65, 55, 70, 58, 62, 75, 87, 80, 85])
hulu_popularity = np.array([50, 56, 58, 60, 64, 53, 66, 62, 68])
disney_plus_popularity = np.array([0, 45, 0, 0, 0, 60, 90, 75, 85])

plt.figure(figsize=(12, 8))

# Randomized changes in marker styles, colors have been shuffled within initial options
plt.plot(years, netflix_popularity, marker='^', linestyle='--', color='blue', label='Netflix')
plt.plot(years, amazon_prime_popularity, marker='x', linestyle='-', color='red', label='Amazon Prime')
plt.plot(years, hulu_popularity, marker='o', linestyle='-.', color='purple', label='Hulu')
plt.plot(years, disney_plus_popularity, marker='s', linestyle=':', color='green', label='Disney+')

# Title and Labels
plt.title("Popularity Trends of Streaming Platforms (2015-2023)\nHow the Market Has Evolved Over Years", fontsize=16, weight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Popularity Score (out of 100)', fontsize=12)

# Alter legend location
plt.legend(loc='lower right', fontsize=12)

# Alter grid style
plt.grid(True, linestyle='-', alpha=0.3)

# Remove plot border (spines) example
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# Annotate significant event 
plt.annotate('Disney+ Launch', xy=(2019.5, 45), xytext=(2017, 55),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, ha='center')

plt.tight_layout()
plt.show()