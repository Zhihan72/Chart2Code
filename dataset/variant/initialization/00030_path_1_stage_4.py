import matplotlib.pyplot as plt
import numpy as np

years = np.array(range(2015, 2024))
netflix = np.array([50, 48, 45, 42, 40, 38, 35, 33, 30])
amazon_prime = np.array([20, 22, 23, 24, 25, 26, 27, 28, 29])
disney_plus = np.array([0, 0, 0, 0, 5, 10, 15, 18, 20])
hulu = np.array([10, 9, 8, 8, 7, 7, 7, 7, 7])
others = np.array([20, 21, 24, 26, 23, 19, 16, 14, 14])
hbo_max = np.array([0, 0, 0, 0, 0, 0, 2, 3, 4])

fig, ax = plt.subplots(figsize=(10, 6))

ax.stackplot(years, netflix, amazon_prime, disney_plus, hulu, others, hbo_max, 
             colors=['#66B2FF'], alpha=0.8)

ax.set_title('Streaming Platforms (2015-2023)', fontsize=16)
ax.set_xlabel('Yr', fontsize=12)
ax.set_ylabel('Share (%)', fontsize=12)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

plt.show()