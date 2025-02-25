import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2021)
facebook_hours = [1.5, 1.7, 2.0, 2.3, 2.5, 2.8, 3.0, 3.1]
instagram_hours = [0.5, 0.7, 1.0, 1.5, 2.0, 2.3, 2.6, 2.8]
twitter_hours = [0.8, 1.0, 1.1, 1.4, 1.6, 1.7, 1.9, 2.0]

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