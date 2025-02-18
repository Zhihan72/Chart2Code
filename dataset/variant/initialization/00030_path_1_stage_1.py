import matplotlib.pyplot as plt
import numpy as np

years = np.array(range(2015, 2024))
netflix = np.array([50, 48, 45, 42, 40, 38, 35, 33, 30])
amazon_prime = np.array([20, 22, 23, 24, 25, 26, 27, 28, 29])
disney_plus = np.array([0, 0, 0, 0, 5, 10, 15, 18, 20])
hulu = np.array([10, 9, 8, 8, 7, 7, 7, 7, 7])
others = np.array([20, 21, 24, 26, 23, 19, 16, 14, 14])

fig, ax = plt.subplots(figsize=(10, 6))

ax.stackplot(years, netflix, amazon_prime, disney_plus, hulu, others, labels=[
    'Netflix', 'Prime', 'Disney+', 'Hulu', 'Others'],
    colors=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#C2C2C2'], alpha=0.8)

ax.set_title('Streaming Platforms (2015-2023)', fontsize=16)
ax.set_xlabel('Yr', fontsize=12)
ax.set_ylabel('Share (%)', fontsize=12)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title="Platforms")

plt.tight_layout(rect=[0, 0, 0.85, 1])

plt.show()