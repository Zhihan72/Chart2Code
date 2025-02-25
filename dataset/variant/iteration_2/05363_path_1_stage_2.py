import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)

fiction = [30, 35, 40, 45, 50, 55, 65, 70, 75, 80]
non_fiction = [20, 25, 22, 30, 35, 38, 40, 42, 45, 48]
science = [10, 12, 15, 17, 20, 22, 25, 28, 30, 32]
history = [15, 18, 20, 22, 25, 26, 28, 30, 32, 35]
fantasy = [25, 28, 29, 32, 35, 38, 40, 42, 45, 50]

cumulative_donations = [100, 200, 350, 500, 700, 900, 1150, 1400, 1700, 2000]

bar_width = 0.15
index = np.arange(len(years))

plt.figure(figsize=(14, 8))

plt.subplot(2, 1, 1)
plt.bar(index - 2*bar_width, fiction, bar_width)
plt.bar(index - bar_width, non_fiction, bar_width)
plt.bar(index, science, bar_width)
plt.bar(index + bar_width, history, bar_width)
plt.bar(index + 2*bar_width, fantasy, bar_width)

plt.xticks(index, years, rotation=45)

plt.subplot(2, 1, 2)
plt.plot(years, cumulative_donations, marker='o', color='b', linewidth=2, alpha=0.8)
plt.fill_between(years, cumulative_donations, color='blue', alpha=0.1)

plt.xticks(years, rotation=45)

plt.tight_layout()
plt.show()