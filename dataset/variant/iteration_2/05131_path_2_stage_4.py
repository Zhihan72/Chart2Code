import matplotlib.pyplot as plt
import numpy as np

years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
netflix_popularity = np.array([82, 88, 78, 92, 95, 85, 97, 93, 96])
amazon_prime_popularity = np.array([65, 55, 70, 58, 62, 75, 87, 80, 85])
hulu_popularity = np.array([50, 56, 58, 60, 64, 53, 66, 62, 68])
disney_plus_popularity = np.array([0, 45, 0, 0, 0, 60, 90, 75, 85])

plt.figure(figsize=(12, 8))

plt.plot(years, netflix_popularity, marker='^', linestyle='--', color='blue', label='MovieFlix')
plt.plot(years, amazon_prime_popularity, marker='x', linestyle='-', color='red', label='PriMeTime')
plt.plot(years, hulu_popularity, marker='o', linestyle='-.', color='purple', label='HuWatch')
plt.plot(years, disney_plus_popularity, marker='s', linestyle=':', color='green', label='D+ Platform')

plt.title("Streaming Platform Trends (2015-2023)\nMarket Evolution", fontsize=16, weight='bold')
plt.xlabel('Timeline', fontsize=12)
plt.ylabel('Popularity Index', fontsize=12)

plt.legend(loc='lower right', fontsize=12)
plt.grid(True, linestyle='-', alpha=0.3)

for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.annotate('D+ Starts', xy=(2019.5, 45), xytext=(2017, 55),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, ha='center')

plt.tight_layout()
plt.show()