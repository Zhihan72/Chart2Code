import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

netflix_subs = np.array([20, 24, 30, 37, 45, 53, 62, 72, 82, 92, 107])
hulu_subs = np.array([7, 8, 10, 13, 16, 20, 25, 29, 31, 33, 36])
prime_subs = np.array([15, 17, 20, 24, 27, 32, 36, 42, 48, 53, 60])
disney_subs = np.array([0, 0, 0, 0, 0, 0, 0, 10, 28, 50, 73])
apple_tv_subs = np.array([0, 0, 0, 0, 0, 0, 5, 8, 12, 18, 25])

fig, ax1 = plt.subplots(figsize=(14, 8))

single_color = '#3090C7'

ax1.plot(years, netflix_subs, marker='o', color=single_color, linewidth=2, linestyle='-')
ax1.plot(years, hulu_subs, marker='s', color=single_color, linewidth=2, linestyle='--')
ax1.plot(years, prime_subs, marker='^', color=single_color, linewidth=2, linestyle='-.')
ax1.plot(years, disney_subs, marker='d', color=single_color, linewidth=2, linestyle=':')
ax1.plot(years, apple_tv_subs, marker='*', color=single_color, linewidth=2, linestyle='-')

ax1.set_title('Streaming Growth (2010-2020)', fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Subscribers (M)', fontsize=14)

total_subs = netflix_subs + hulu_subs + prime_subs + disney_subs + apple_tv_subs
market_share_netflix = (netflix_subs / total_subs) * 100
market_share_hulu = (hulu_subs / total_subs) * 100
market_share_prime = (prime_subs / total_subs) * 100
market_share_disney = (disney_subs / total_subs) * 100
market_share_apple_tv = (apple_tv_subs / total_subs) * 100

ax2 = ax1.twinx()
ax2.plot(years, market_share_netflix, color=single_color, linestyle='--', linewidth=1.5, alpha=0.4)
ax2.plot(years, market_share_hulu, color=single_color, linestyle='--', linewidth=1.5, alpha=0.4)
ax2.plot(years, market_share_prime, color=single_color, linestyle='--', linewidth=1.5, alpha=0.4)
ax2.plot(years, market_share_disney, color=single_color, linestyle='--', linewidth=1.5, alpha=0.4)
ax2.plot(years, market_share_apple_tv, color=single_color, linestyle='--', linewidth=1.5, alpha=0.4)
ax2.set_ylabel('Market Share (%)', fontsize=14)

plt.tight_layout()
plt.show()