import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

fps_viewership = [2, 5, 8, 10, 13, 19, 35, 42, 50, 62, 75]
moba_viewership = [1, 3, 7, 14, 22, 30, 45, 55, 68, 80, 95]

fig, ax1 = plt.subplots(figsize=(14, 9))

single_color = 'blue'
ax1.plot(years, fps_viewership, color=single_color, linestyle='-', linewidth=2, marker='o')
ax1.plot(years, moba_viewership, color=single_color, linestyle='--', linewidth=2, marker='s')

ax1.set_title('The Evolution of E-Sports Viewership (2010-2020)', fontsize=16, weight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Viewership (Millions)', fontsize=14)

highlight_years = [2013, 2015, 2018]
for year in highlight_years:
    ax1.axvline(x=year, color='black', linestyle='--', linewidth=1, alpha=0.8)
    ax1.text(year + 0.1, 30, f'Key Event', color='black', fontsize=12, rotation=90)

key_events = {
    '2013': 'MOBA Rise\nMajor Tournaments',
    '2015': 'FPS Boom\nNew Popular Titles',
    '2018': 'E-Sports\nMainstream'
}

for year, event in key_events.items():
    ax1.annotate(event, xy=(int(year), moba_viewership[years.tolist().index(int(year))]), 
                 xytext=(int(year), moba_viewership[years.tolist().index(int(year))] + 10),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=12, ha='center')

plt.tight_layout()
plt.show()