import matplotlib.pyplot as plt
import numpy as np

years = np.array(range(2015, 2024))

netflix = np.array([45, 50, 42, 40, 38, 35, 33, 30, 48])
amazon_prime = np.array([22, 23, 24, 25, 26, 27, 28, 29, 20])
disney_plus = np.array([0, 0, 5, 10, 0, 15, 18, 20, 0])
hulu = np.array([9, 8, 8, 7, 7, 7, 10, 7, 7])
others = np.array([21, 24, 26, 23, 19, 16, 14, 14, 20])

fig, ax = plt.subplots(figsize=(10, 6))

ax.stackplot(years, netflix, amazon_prime, disney_plus, hulu, others, labels=[
    'Netflix', 'Amazon Prime Video', 'Disney+', 'Hulu', 'Others'],
    colors=['#99FF99', '#C2C2C2', '#FFCC99', '#66B2FF', '#FF9999'], alpha=0.8)

ax.set_title('Market Share of Streaming Platforms\n(2015-2023)', fontsize=16)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Market Share (%)', fontsize=12)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title="Platforms")

plt.tight_layout(rect=[0, 0, 0.85, 1])

plt.show()