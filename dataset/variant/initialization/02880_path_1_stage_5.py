import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2024)
seasons = ['Spring', 'Summer', 'Autumn', 'Winter', 'Stormy']

# Visitor data
visitors_spring = np.array([30, 34, 36, 38])
visitors_summer = np.array([50, 55, 60, 62])
visitors_autumn = np.array([25, 27, 28, 30])
visitors_winter = np.array([15, 18, 16, 14])
visitors_stormy = np.array([10, 12, 11, 15])

# Temperature data
temps = [
    [12, 13, 14, 15],  # Spring
    [25, 26, 27, 28],  # Summer
    [14, 13, 13, 12],  # Autumn
    [2, 3, 4, 3],      # Winter
    [8, 7, 9, 10],     # Stormy
]

fig, axs = plt.subplots(2, 1, figsize=(10, 10), constrained_layout=True)

# To create a sorted bar chart, first, sort the visitors data for each year
total_visitors = np.array([visitors_spring + visitors_summer + visitors_autumn + visitors_winter + visitors_stormy])
total_visitor_sort_indices = np.argsort(total_visitors[0])  # Sort by total number of visitors
sorted_years = years[total_visitor_sort_indices]

# Sorted visitors data
sorted_visitors_spring = visitors_spring[total_visitor_sort_indices]
sorted_visitors_summer = visitors_summer[total_visitor_sort_indices]
sorted_visitors_autumn = visitors_autumn[total_visitor_sort_indices]
sorted_visitors_winter = visitors_winter[total_visitor_sort_indices]
sorted_visitors_stormy = visitors_stormy[total_visitor_sort_indices]

# Bar plot for sorted visitors.
axs[0].bar(sorted_years, sorted_visitors_spring, label='Spring', color='#FF6347')
axs[0].bar(sorted_years, sorted_visitors_summer, bottom=sorted_visitors_spring, label='Summer', color='#FFD700')
axs[0].bar(sorted_years, sorted_visitors_autumn, bottom=sorted_visitors_spring + sorted_visitors_summer, label='Autumn', color='#98FB98')
axs[0].bar(sorted_years, sorted_visitors_winter, bottom=sorted_visitors_spring + sorted_visitors_summer + sorted_visitors_autumn, label='Winter', color='#4682B4')
axs[0].bar(sorted_years, sorted_visitors_stormy, bottom=sorted_visitors_spring + sorted_visitors_summer + sorted_visitors_autumn + sorted_visitors_winter, label='Stormy', color='#8B008B')

axs[0].set_title('Sorted Seasonal Visitor Trends\nEvergreen National Park (2020-2023)', fontsize=14, fontweight='bold', pad=10)
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Visitors (Thousands)', fontsize=12)
axs[0].set_xticks(sorted_years)
axs[0].set_xticklabels(sorted_years, rotation=45, ha='right')
axs[0].legend(loc='best', title='Seasons', fontsize=10)

# To create sorted temperature data
average_temps = np.mean(temps, axis=1)
temp_sort_indices = np.argsort(average_temps)  # Sort by average temperatures
sorted_seasons = [seasons[i] for i in temp_sort_indices]
sorted_temps = np.array(temps)[temp_sort_indices]

# Bar plot for sorted temperatures
bar_width = 0.15
x_indices = np.arange(len(years))

for i, season in enumerate(sorted_seasons):
    axs[1].bar(x_indices + i * bar_width, sorted_temps[i], bar_width, label=season, alpha=0.8)

axs[1].set_title('Sorted Average Seasonal Temperatures (°C)', fontsize=14, fontweight='bold', pad=10)
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Temperature (°C)', fontsize=12)
axs[1].set_xticks(x_indices + bar_width * 2)
axs[1].set_xticklabels(years, rotation=45, ha='right')
axs[1].legend(loc='upper right', title='Seasons', fontsize=10)

plt.show()