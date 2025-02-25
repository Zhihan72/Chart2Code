import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

fps_viewership = [2, 5, 8, 10, 13, 19, 35, 42, 50, 62, 75]
moba_viewership = [1, 3, 7, 14, 22, 30, 45, 55, 68, 80, 95]
rts_viewership = [8, 9, 10, 12, 14, 16, 19, 21, 25, 26, 28]

fig, ax1 = plt.subplots(figsize=(14, 9))

# Use a single color for consistency across all data groups
ax1.plot(years, fps_viewership, color='blue', linestyle=':', linewidth=2, marker='v', label='FPS Games')
ax1.plot(years, moba_viewership, color='blue', linestyle='-.', linewidth=2, marker='d', label='MOBA Games')
ax1.plot(years, rts_viewership, color='blue', linestyle='-', linewidth=2, marker='x', label='RTS Games')

ax1.grid(True, linestyle='-', linewidth=0.75, alpha=0.5)

ax1.set_title('Online Gaming Audience Growth (2010-2020)', fontsize=17, weight='normal')
ax1.set_xlabel('Year', fontsize=13)
ax1.set_ylabel('Audience (Millions)', fontsize=13)

highlight_years = [2013, 2015, 2018]
for year in highlight_years:
    ax1.axvline(x=year, color='gray', linestyle='-.', linewidth=1, alpha=0.7)
    ax1.text(year + 0.2, 30, 'Event', color='brown', fontsize=11, rotation=90)

key_events = {
    '2013': 'Arena\nExpansion',
    '2015': 'Shooter\nBoom',
    '2018': 'Public\nInterest'
}

for year, event in key_events.items():
    ax1.annotate(event, xy=(int(year), moba_viewership[years.tolist().index(int(year))]),
                 xytext=(int(year), moba_viewership[years.tolist().index(int(year))] + 15),
                 arrowprops=dict(facecolor='gray', arrowstyle='-|>'),
                 fontsize=13, ha='right')

ax1.legend(loc='upper right', fontsize=11)

plt.tight_layout()

plt.show()