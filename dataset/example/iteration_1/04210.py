import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# This chart represents the air quality index (AQI) evolution over a year in an urban area. There are 3 different areas within the city,
# each monitored for AQI over 12 months. The plot shows the comparison of AQI trends in these areas to provide insights into air pollution patterns.

# Months of the year
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# AQI data for three different areas
area1_aqi = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105])
area2_aqi = np.array([40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62])
area3_aqi = np.array([45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])

# Define automatic margins and layout adjustment
plt.figure(figsize=(14, 8))
plt.tight_layout()

# Plotting the data
plt.plot(months, area1_aqi, linestyle='-', color='blue', marker='o', label='Residential Area')
plt.plot(months, area2_aqi, linestyle='--', color='green', marker='s', label='Industrial Area')
plt.plot(months, area3_aqi, linestyle=':', color='red', marker='^', label='Commercial Area')

# Highlighting specific points where AQI exceeds safe levels (>100 AQI marked as Unsafe)
for i, val in enumerate(area3_aqi):
    if val > 100:
        plt.annotate('Unsafe', xy=(months[i], val), 
                     xytext=(months[i], val + 5),
                     arrowprops=dict(facecolor='black', shrink=0.05),
                     fontsize=10, ha='center')

# Titles and labels
plt.title("Urban Air Quality Index (AQI) Trends Throughout The Year", fontsize=16, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Air Quality Index (AQI)", fontsize=12)

# Customizing x-ticks for better visibility
plt.xticks(months, fontsize=10)
plt.yticks(np.arange(0, 120, 10), fontsize=10)

# Adding a legend
plt.legend(loc='upper left', fontsize=10)

# Enabling grid with custom style
plt.grid(True, linestyle='--', alpha=0.7)

# Adjusting layout to avoid overlapping
plt.tight_layout()

# Displaying the plot
plt.show()