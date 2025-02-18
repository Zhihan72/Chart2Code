import matplotlib.pyplot as plt
import numpy as np

# Data: Average Monthly Temperatures (in Celsius) for a fictitious city over a year
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
city_a_temps = np.array([2.0, 4.1, 9.3, 13.4, 18.2, 22.3, 25.6, 25.3, 20.1, 14.0, 8.1, 3.2])

# Yearly average temperature for the city
avg_city_a = np.mean(city_a_temps)

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot temperature line for City A
ax.plot(months, city_a_temps, label='City A', marker='o', color='#1f77b4', linewidth=2)

# Mark average yearly temperature with a dashed line
ax.axhline(y=avg_city_a, color='#1f77b4', linestyle='--', linewidth=1.5, alpha=0.7)

# Add annotation for average temperature
ax.text(len(months)-1, avg_city_a, f'  Avg: {avg_city_a:.1f}°C', color='#1f77b4', verticalalignment='bottom')

# Customizing title and labels
ax.set_title('Monthly Average Temperatures\nCity A Over a Year', fontsize=16, pad=20)
ax.set_xlabel('Months', fontsize=12)
ax.set_ylabel('Temperature (°C)', fontsize=12)

# Adding point of interest
ax.annotate('Peak Summer', xy=('Jul', 25.6), xytext=('May', 26),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1),
            fontsize=10, color='#1f77b4')

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