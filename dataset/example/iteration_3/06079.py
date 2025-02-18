import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking Climatic Changes through Average Monthly Temperatures
# The year is 2050, and scientists are studying the effects of climate change by monitoring
# the average monthly temperatures in three different cities over a span of one year.

# Define the months and the average temperatures (in °C) for three cities
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
city_a_temps = [2, 3, 7, 12, 18, 23, 27, 26, 21, 15, 9, 4]
city_b_temps = [5, 6, 10, 16, 21, 26, 31, 30, 25, 19, 12, 6]
city_c_temps = [-1, 0, 4, 10, 16, 21, 25, 24, 19, 13, 6, 0]

# Create a subplot grid: 1 row, 2 columns
fig, axs = plt.subplots(1, 2, figsize=(14, 7), constrained_layout=True)

# First subplot: Line chart for city A and city B temperatures
axs[0].plot(months, city_a_temps, '-o', color='blue', label='City A', linewidth=2, markerfacecolor='white')
axs[0].plot(months, city_b_temps, '-s', color='green', label='City B', linewidth=2, markerfacecolor='white')

axs[0].set_title('Average Monthly Temperatures (2050):\nCity A and City B', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Months', fontsize=12)
axs[0].set_ylabel('Temperature (°C)', fontsize=12)
axs[0].set_xticks(np.arange(len(months)))
axs[0].set_xticklabels(months)
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].legend(loc='upper left', fontsize=10)

# Second subplot: Line chart for city C temperatures with seasonal mean temperatures
axs[1].plot(months, city_c_temps, '-^', color='red', label='City C', linewidth=2, markerfacecolor='white')

# Seasonal breakdown (Winter: Dec-Feb, Spring: Mar-May, Summer: Jun-Aug, Autumn: Sep-Nov)
winter_mean = np.mean(city_c_temps[0:2] + city_c_temps[11:])
spring_mean = np.mean(city_c_temps[2:5])
summer_mean = np.mean(city_c_temps[5:8])
autumn_mean = np.mean(city_c_temps[8:11])

axs[1].axhline(y=winter_mean, color='blue', linestyle='--', label='Winter Mean')
axs[1].axhline(y=spring_mean, color='green', linestyle='--', label='Spring Mean')
axs[1].axhline(y=summer_mean, color='orange', linestyle='--', label='Summer Mean')
axs[1].axhline(y=autumn_mean, color='purple', linestyle='--', label='Autumn Mean')

axs[1].set_title('Average Monthly Temperatures (2050):\nCity C with Seasonal Means', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Months', fontsize=12)
axs[1].set_ylabel('Temperature (°C)', fontsize=12)
axs[1].set_xticks(np.arange(len(months)))
axs[1].set_xticklabels(months)
axs[1].grid(True, linestyle='--', alpha=0.6)
axs[1].legend(loc='upper left', fontsize=10)

# Annotate seasonal means
season_annot = [('Winter', winter_mean), ('Spring', spring_mean), ('Summer', summer_mean), ('Autumn', autumn_mean)]
for season, mean_temp in season_annot:
    axs[1].text(len(months)-1, mean_temp + 0.5, f'{season} mean: {mean_temp:.1f}°C', 
                fontsize=10, color='black', ha='right', backgroundcolor='white')

# Display the plot
plt.show()