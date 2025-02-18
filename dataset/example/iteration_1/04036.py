import matplotlib.pyplot as plt
import numpy as np

# Data: Average Monthly Temperatures (in Celsius) for two fictitious cities over a year
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
city_a_temps = np.array([2.0, 4.1, 9.3, 13.4, 18.2, 22.3, 25.6, 25.3, 20.1, 14.0, 8.1, 3.2])
city_b_temps = np.array([-5.0, -2.8, 2.5, 10.1, 15.3, 19.8, 23.4, 22.9, 16.5, 9.0, 1.2, -3.7])

# Yearly average temperature for both cities
avg_city_a = np.mean(city_a_temps)
avg_city_b = np.mean(city_b_temps)

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot temperature lines
ax.plot(months, city_a_temps, label='City A', marker='o', color='#1f77b4', linewidth=2)
ax.plot(months, city_b_temps, label='City B', marker='s', color='#ff7f0e', linewidth=2)

# Mark average yearly temperatures with dashed lines
ax.axhline(y=avg_city_a, color='#1f77b4', linestyle='--', linewidth=1.5, alpha=0.7)
ax.axhline(y=avg_city_b, color='#ff7f0e', linestyle='--', linewidth=1.5, alpha=0.7)

# Add annotations for average temperatures
ax.text(len(months)-1, avg_city_a, f'  Avg: {avg_city_a:.1f}°C', color='#1f77b4', verticalalignment='bottom')
ax.text(len(months)-1, avg_city_b, f'  Avg: {avg_city_b:.1f}°C', color='#ff7f0e', verticalalignment='top')

# Customizing title and labels
ax.set_title('Monthly Average Temperatures\nCity A vs City B Over a Year', fontsize=16, pad=20)
ax.set_xlabel('Months', fontsize=12)
ax.set_ylabel('Temperature (°C)', fontsize=12)

# Adding points of interest
ax.annotate('Peak Summer', xy=('Jul', 25.6), xytext=('May', 26),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1),
            fontsize=10, color='#1f77b4')
ax.annotate('Winter Trough', xy=('Jan', -5.0), xytext=('Mar', -12),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1),
            fontsize=10, color='#ff7f0e')

# Customizing grid and ticks
ax.grid(visible=True, which='both', linestyle='--', linewidth=0.6, color='grey', alpha=0.7)
ax.set_xticks(months)
ax.set_yticks(np.arange(-10, 31, 5))
ax.set_ylim(-10, 30)

# Adding legend
ax.legend(title='Cities', title_fontsize='13', fontsize='10', loc='upper left')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()