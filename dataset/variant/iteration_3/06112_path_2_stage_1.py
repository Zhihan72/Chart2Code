import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2018, 2023)
swimmer_assist = np.array([50, 45, 60, 55, 65])
minor_injuries = np.array([20, 25, 15, 18, 22])
major_injuries = np.array([5, 4, 6, 7, 6])
rough_seas = np.array([15, 13, 18, 20, 17])
crowd_control = np.array([10, 9, 14, 13, 11])

rescue_data = np.vstack([swimmer_assist, minor_injuries, major_injuries, rough_seas, crowd_control])

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, rescue_data, labels=['Swimmer Assist', 'Minor Injuries', 'Major Injuries', 
                                         'Rescues in Rough Seas', 'Crowd Control'], 
             colors=['#87CEEB', '#3CB371', '#FFD700', '#8B0000', '#6A5ACD'], alpha=0.85)

ax.set_title('Seasonal Beach Lifeguard Rescues in Wave Harbor (2018-2022)', fontsize=18, weight='bold', pad=20)
ax.set_xlabel('Year', fontsize=13, weight='bold')
ax.set_ylabel('Number of Rescues', fontsize=13, weight='bold')

highlight_years = [2019, 2021]
for year in highlight_years:
    ax.axvline(x=year, color='gray', linestyle='-.', linewidth=1.5)

ax.annotate('Increased Rough Seas Rescues', xy=(2021, 110), xytext=(2018.7, 125),
            arrowprops=dict(facecolor='gray', shrink=0.05), fontsize=11, ha='left')

ax.grid(visible=True, linestyle=':', alpha=0.5)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=40, ha='right')

ax.legend(loc='lower left', bbox_to_anchor=(0, 0), title='Rescue Types', fontsize=12, shadow=False)

for y, color in zip(rescue_data, ['#87CEEB', '#3CB371', '#FFD700', '#8B0000', '#6A5ACD']):
    ax.plot(years, y, marker='d', markersize=7, color=color, linestyle='-', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()