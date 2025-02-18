import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1010, 1020)
atlantis_festivals = np.array([[5, 4, 3, 2], [6, 5, 4, 3], [7, 5, 5, 3], [8, 6, 5, 4], [6, 5, 4, 3], 
                               [5, 5, 3, 4], [6, 6, 4, 3], [7, 5, 5, 4], [8, 5, 6, 5], [9, 6, 6, 4]])
el_dorado_festivals = np.array([[6, 3, 4, 1], [7, 4, 5, 2], [8, 4, 6, 2], [9, 5, 6, 3], [7, 4, 5, 2],
                                [6, 4, 4, 3], [7, 5, 5, 2], [8, 4, 6, 3], [9, 4, 7, 4], [10, 5, 7, 3]])
avalon_festivals = np.array([[7, 6, 5, 4], [8, 7, 6, 5], [9, 7, 7, 5], [10, 8, 7, 6], [8, 7, 6, 5],
                             [7, 7, 5, 6], [8, 8, 6, 5], [9, 7, 7, 6], [10, 7, 8, 7], [11, 8, 8, 6]])

average_attendance = np.mean(atlantis_festivals + el_dorado_festivals + avalon_festivals, axis=1)

# Apply a single color for all festival groups
single_color = '#FFA07A'  # A uniform color applied across all bars

fig, ax1 = plt.subplots(figsize=(14, 9))

for city_festivals in [atlantis_festivals, el_dorado_festivals, avalon_festivals]:
    base = np.zeros(len(years))
    for j in range(city_festivals.shape[1]):
        ax1.bar(years, city_festivals[:, j], bottom=base, 
                color=single_color, edgecolor='black', linewidth=0.5)
        base += city_festivals[:, j]

ax2 = ax1.twinx()
ax2.plot(years, average_attendance, label='Avg Attendance', color='black', linestyle='--', marker='o')
ax2.set_ylabel('Average Attendance')
ax2.set_ylim(0, 40)

ax1.set_title('Annual Cultural Festival Distribution\nin Ancient Cities (1010-1019) with Avg Attendance', fontsize=14)
ax1.set_ylabel('Number of Festivals')
ax1.set_xlabel('Year')
ax1.set_xticks(years)
ax1.set_ylim(0, 50)

plt.tight_layout()
plt.show()