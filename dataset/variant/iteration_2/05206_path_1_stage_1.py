import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2021)
facebook_hours = [1.5, 1.7, 2.0, 2.3, 2.5, 2.8, 3.0, 3.1]
instagram_hours = [0.5, 0.7, 1.0, 1.5, 2.0, 2.3, 2.6, 2.8]
twitter_hours = [0.8, 1.0, 1.1, 1.4, 1.6, 1.7, 1.9, 2.0]

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(years, facebook_hours, label='Facebook', color='blue', linestyle='--', marker='D')
ax.plot(years, instagram_hours, label='Instagram', color='purple', linestyle=':', marker='x')
ax.plot(years, twitter_hours, label='Twitter', color='green', linestyle='-', marker='<')

ax.annotate('Instagram surpasses 1 hour mark', xy=(2016, 1.5), xytext=(2017, 2),
            arrowprops=dict(facecolor='gray', shrink=0.05), fontsize=11, color='darkred')
ax.annotate('Facebook reaches 3 hours', xy=(2018, 3), xytext=(2017, 2.6),
            arrowprops=dict(facecolor='gray', shrink=0.05), fontsize=11, color='darkred')

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Daily Usage (hours)', fontsize=12)
ax.set_title('Average Daily Social Media Usage Hours\n(2013-2020)', fontsize=16, fontweight='bold')

ax.grid(True, linestyle=':', alpha=0.8)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

ax.legend(title='Platform', loc='lower right', fontsize=10, frameon=True, framealpha=0.5)

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

plt.tight_layout()
plt.show()