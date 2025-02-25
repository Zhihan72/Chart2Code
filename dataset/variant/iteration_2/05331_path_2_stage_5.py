import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023, 1)

opening_price = np.array([21, 23, 27, 29, 26, 27, 36, 41, 44, 51])
closing_price = np.array([20, 25, 30, 24, 27, 36, 41, 44, 52, 54])
highest_price = np.array([25, 29, 31, 28, 31, 36, 44, 47, 56, 59])
lowest_price = np.array([17, 21, 22, 19, 25, 26, 33, 38, 43, 46])

volume_traded = np.array([6, 8, 9, 7, 6, 9, 11, 13, 14, 19])

fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharex=True)

axes[0].plot(years, opening_price, marker='o', color='blue', linewidth=2)
axes[0].plot(years, closing_price, marker='o', color='blue', linewidth=2)
axes[0].plot(years, highest_price, marker='o', color='blue', linewidth=2)
axes[0].plot(years, lowest_price, marker='o', color='blue', linewidth=2)

# Changed title and axis labels
axes[0].set_title('Financial Highlights of ABC Corp. (2013-2022)', fontsize=16, fontweight='bold')
axes[0].set_ylabel('Stock Value (USD)', fontsize=14)

axes[1].bar(years, volume_traded, color='blue', alpha=0.7)

# Changed title and axis labels
axes[1].set_title('Trading Volume of ABC Corp. (2013-2022)', fontsize=16, fontweight='bold')
axes[1].set_xlabel('Fiscal Year', fontsize=14)
axes[1].set_ylabel('Shares Traded (Millions)', fontsize=14)

# Changed significant years and events to match the new theme
significant_years = [2017, 2020]
events = ['Strategic Merger', 'Pandemic Impact']
volume_spots = volume_traded[np.isin(years, significant_years)]

for (year, event, volume) in zip(significant_years, events, volume_spots):
    axes[1].annotate(f'{event}\n{volume}M', xy=(year, volume), xytext=(year, volume + 2),
                     arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, ha='center', bbox=dict(boxstyle="round,pad=0.3", edgecolor='none', facecolor='lightgrey', alpha=0.5))

plt.xticks(years, rotation=45)

plt.tight_layout(pad=2)

plt.show()