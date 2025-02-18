import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)

# Values are shuffled within each category
fiction = [45, 30, 50, 70, 35, 40, 75, 80, 65, 55]
non_fiction = [30, 22, 25, 48, 35, 40, 38, 45, 20, 42]
science = [12, 15, 32, 20, 17, 30, 28, 10, 22, 25]
history = [28, 22, 15, 18, 32, 26, 25, 30, 35, 20]
fantasy = [29, 32, 38, 35, 42, 40, 45, 25, 28, 50]

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