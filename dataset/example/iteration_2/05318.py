import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart illustrates the rise in subscription numbers for various streaming services over a decade. 
# The data spans from 2010 to 2020, showing how different streaming platforms have grown in popularity.

# Years
years = np.arange(2010, 2021)

# Manually created data showing subscription numbers (in millions)
netflix_subs = np.array([20, 24, 30, 37, 45, 53, 62, 72, 82, 92, 107])
hulu_subs = np.array([7, 8, 10, 13, 16, 20, 25, 29, 31, 33, 36])
prime_subs = np.array([15, 17, 20, 24, 27, 32, 36, 42, 48, 53, 60])
disney_subs = np.array([0, 0, 0, 0, 0, 0, 0, 10, 28, 50, 73])

# Initialize figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting streaming service data
ax1.plot(years, netflix_subs, marker='o', color='red', label='Netflix', linewidth=2, linestyle='-')
ax1.plot(years, hulu_subs, marker='s', color='green', label='Hulu', linewidth=2, linestyle='--')
ax1.plot(years, prime_subs, marker='^', color='blue', label='Amazon Prime', linewidth=2, linestyle='-.')
ax1.plot(years, disney_subs, marker='d', color='purple', label='Disney+', linewidth=2, linestyle=':')

# Annotate significant events
ax1.annotate('Disney+ Launch', xy=(2017, 10), xytext=(2016, 30),
             arrowprops=dict(facecolor='gray', arrowstyle='->', linestyle='--', linewidth=1.5), 
             fontsize=10, color='black', bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.5', alpha=0.8))

# Highlighting key numbers
for i, year in enumerate(years):
    ax1.text(year, netflix_subs[i] + 1, f'{netflix_subs[i]}', ha='center', va='bottom', fontsize=8, color='red')
    ax1.text(year, hulu_subs[i] + 1, f'{hulu_subs[i]}', ha='center', va='bottom', fontsize=8, color='green')
    ax1.text(year, prime_subs[i] + 1, f'{prime_subs[i]}', ha='center', va='bottom', fontsize=8, color='blue')
    ax1.text(year, disney_subs[i] + 1, f'{disney_subs[i]}', ha='center', va='bottom', fontsize=8, color='purple')

# Titles and labels
ax1.set_title('Decade of Growth in Streaming Services (2010-2020)', fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Number of Subscribers (millions)', fontsize=14)

# Enhanced legend
ax1.legend(loc='upper left', fontsize=11, shadow=True, fancybox=True)

# Enable enhanced grid
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)

# Secondary axis for market share percentage
ax2 = ax1.twinx()
total_subs = netflix_subs + hulu_subs + prime_subs + disney_subs
market_share_netflix = (netflix_subs / total_subs) * 100
market_share_hulu = (hulu_subs / total_subs) * 100
market_share_prime = (prime_subs / total_subs) * 100
market_share_disney = (disney_subs / total_subs) * 100

ax2.plot(years, market_share_netflix, color='red', linestyle='--', linewidth=1.5, alpha=0.4, label='Netflix Market Share (%)')
ax2.plot(years, market_share_hulu, color='green', linestyle='--', linewidth=1.5, alpha=0.4, label='Hulu Market Share (%)')
ax2.plot(years, market_share_prime, color='blue', linestyle='--', linewidth=1.5, alpha=0.4, label='Amazon Prime Market Share (%)')
ax2.plot(years, market_share_disney, color='purple', linestyle='--', linewidth=1.5, alpha=0.4, label='Disney+ Market Share (%)')
ax2.set_ylabel('Market Share Percentage (%)', fontsize=14)
ax2.legend(loc='upper right', fontsize=10, frameon=False)

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()