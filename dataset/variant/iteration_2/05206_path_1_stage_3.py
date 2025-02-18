import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2021)
facebook_hours = [2.3, 1.7, 3.0, 2.3, 1.5, 3.1, 2.5, 2.8]  # Altered data points
instagram_hours = [1.5, 0.7, 2.6, 1.0, 2.3, 2.8, 0.5, 2.0]  # Altered data points
twitter_hours = [1.9, 1.0, 0.8, 2.0, 1.4, 2.0, 1.1, 1.7]  # Altered data points

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(years, facebook_hours, color='blue', linestyle='--', marker='D')
ax.plot(years, instagram_hours, color='purple', linestyle=':', marker='x')
ax.plot(years, twitter_hours, color='green', linestyle='-', marker='<')

ax.grid(True, linestyle=':', alpha=0.8)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

plt.tight_layout()
plt.show()