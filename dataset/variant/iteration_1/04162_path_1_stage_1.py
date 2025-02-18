import matplotlib.pyplot as plt
import numpy as np

# Define months
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Constructing average temperature data for four cities
city_names = ['Metropolis', 'Oceanville', 'Highland', 'Sunset City']
city_a_temps = np.array([3, 4, 8, 12, 17, 22, 24, 23, 19, 14, 8, 4])
city_b_temps = np.array([5, 7, 12, 18, 24, 28, 30, 29, 25, 18, 11, 7])
city_c_temps = np.array([-1, 0, 5, 10, 15, 20, 22, 21, 17, 10, 5, 0])
city_d_temps = np.array([10, 12, 15, 19, 23, 27, 29, 28, 24, 19, 14, 11])

# Create the plot area
fig, ax = plt.subplots(figsize=(14, 8))

# Plot lines for each city
ax.plot(months, city_a_temps, marker='o', linestyle='-', label='Metropolis')
ax.plot(months, city_b_temps, marker='s', linestyle='--', label='Oceanville')
ax.plot(months, city_c_temps, marker='d', linestyle='-.', label='Highland')
ax.plot(months, city_d_temps, marker='^', linestyle=':', label='Sunset City')

# Customize title and labels
ax.set_title("Climate Patterns of Global Cities (2023)", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Calendar Months", fontsize=14, weight='bold')
ax.set_ylabel("Avg. Temp (°C)", fontsize=14, weight='bold')
ax.legend(loc='upper right', fontsize=12, title='Locations')

# Add grid for better readability
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Highlight hottest and coldest months for each city
for city_temps, city_name in zip([city_a_temps, city_b_temps, city_c_temps, city_d_temps], city_names):
    hottest_month = months[np.argmax(city_temps)]
    coldest_month = months[np.argmin(city_temps)]
    hottest_temp = np.max(city_temps)
    coldest_temp = np.min(city_temps)
    
    ax.annotate(f'Top Month: {hottest_month}\n{hottest_temp}°C', 
                xy=(hottest_month, hottest_temp), 
                xytext=(hottest_month, hottest_temp + 3), 
                arrowprops=dict(facecolor='red', shrink=0.05), 
                fontsize=10, color='darkred', ha='center')
    
    ax.annotate(f'Lowest Month: {coldest_month}\n{coldest_temp}°C', 
                xy=(coldest_month, coldest_temp), 
                xytext=(coldest_month, coldest_temp - 5), 
                arrowprops=dict(facecolor='blue', shrink=0.05), 
                fontsize=10, color='darkblue', ha='center')

# Improve tick appearance
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Adjust layout
plt.tight_layout()

# Display the chart
plt.show()