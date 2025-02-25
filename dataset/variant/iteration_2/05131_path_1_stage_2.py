import matplotlib.pyplot as plt
import numpy as np

years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
netflix_popularity = np.array([78, 82, 85, 88, 92, 95, 97, 96, 93])
amazon_prime_popularity = np.array([55, 58, 62, 65, 70, 75, 80, 85, 87])
hulu_popularity = np.array([50, 53, 56, 58, 60, 62, 64, 66, 68])
disney_plus_popularity = np.array([0, 0, 0, 0, 45, 60, 75, 85, 90])

plt.figure(figsize=(12, 8))

# Shuffled colors for each data group
plt.plot(years, netflix_popularity, marker='o', linestyle='-', color='blue', label='Netflix')
plt.plot(years, amazon_prime_popularity, marker='s', linestyle='-', color='green', label='Amazon')
plt.plot(years, hulu_popularity, marker='^', linestyle='-', color='purple', label='Hulu')
plt.plot(years, disney_plus_popularity, marker='d', linestyle='-', color='red', label='Disney+')

plt.title("Streaming Popularity (2015-2023)", fontsize=16, weight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Popularity Score', fontsize=12)

plt.legend(loc='upper left', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

plt.annotate('Disney+ Launch', xy=(2019.5, 45), xytext=(2017, 55),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, ha='center')

plt.tight_layout()
plt.show()