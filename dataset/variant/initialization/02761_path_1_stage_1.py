import matplotlib.pyplot as plt
import numpy as np

# Years for x-axis
years = np.arange(1010, 1020)

# Randomly rearranged data for number of festivals in different cities
atlantis_festivals = np.array([[3, 2, 5, 4], [4, 6, 5, 3], [5, 3, 7, 5], [5, 4, 8, 6], [3, 5, 6, 4], 
                               [4, 3, 5, 5], [4, 6, 6, 3], [5, 4, 7, 5], [6, 5, 5, 8], [6, 4, 9, 6]])
el_dorado_festivals = np.array([[4, 6, 1, 3], [5, 7, 4, 2], [6, 8, 4, 2], [5, 6, 3, 9], [4, 7, 2, 5],
                                [3, 4, 6, 4], [5, 7, 5, 2], [4, 6, 3, 8], [7, 4, 9, 4], [7, 4, 5, 10]])
shangri_la_festivals = np.array([[2, 4, 3, 5], [3, 4, 5, 6], [4, 6, 4, 6], [4, 5, 7, 7], [3, 5, 4, 6],
                                 [2, 4, 5, 6], [3, 5, 5, 7], [4, 5, 6, 6], [5, 6, 7, 6], [5, 5, 8, 7]])
avalon_festivals = np.array([[5, 4, 7, 6], [6, 5, 8, 7], [7, 5, 9, 7], [7, 6, 10, 8], [6, 5, 8, 7],
                             [5, 6, 7, 7], [6, 8, 8, 6], [7, 6, 9, 7], [8, 7, 7, 10], [8, 7, 6, 11]])

# Construct average attendance data
average_attendance = np.mean(atlantis_festivals + el_dorado_festivals + shangri_la_festivals + avalon_festivals, axis=1)

# Colors for the different festival types
colors = ['#FF6347', '#FFD700', '#8A2BE2', '#40E0D0']

fig, ax1 = plt.subplots(figsize=(14, 9))

# Plot stacked bars for each city and festival type
for i, (city_festivals, city_name, alpha, hatch, linestyle) in enumerate(
    zip([atlantis_festivals, el_dorado_festivals, shangri_la_festivals, avalon_festivals], 
        ['Atlantis', 'El Dorado', 'Shangri-La', 'Avalon'],
        [1, 0.8, 0.6, 0.5], 
        [None, '//', None, None], 
        ['-', '-', '-', '-'])):
    
    base = np.zeros(len(years))
    for j in range(city_festivals.shape[1]):
        ax1.bar(years, city_festivals[:, j], bottom=base, 
                color=colors[j], alpha=alpha, hatch=hatch, edgecolor='black' if city_name == 'Avalon' else None, linewidth=0.5)
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

bar_handles, _ = ax1.get_legend_handles_labels()
line_handles, _ = ax2.get_legend_handles_labels()
ax1.legend(handles=bar_handles[:4], loc='upper left', bbox_to_anchor=(1.02, 1), title='Festival Type (City)', fontsize=9, ncol=2)
ax2.legend(handles=line_handles, loc='upper right', bbox_to_anchor=(1.02, 0.5), fontsize=9)

plt.tight_layout()
plt.show()