import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the Effects of Climate Change on Monthly Average Temperatures
# We will compare monthly average temperatures over a span of five years
# in two different cities: City A and City B.

# Months of the year
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Monthly average temperatures (°C) for City A over five years
city_a_2016 = np.array([3.1, 4.0, 7.5, 12.3, 17.9, 22.2, 25.5, 24.9, 20.3, 14.2, 9.1, 4.1])
city_a_2017 = np.array([2.9, 3.8, 7.7, 11.8, 17.5, 21.8, 25.2, 24.8, 20.1, 14.0, 8.8, 3.9])
city_a_2018 = np.array([3.0, 4.2, 7.6, 12.2, 18.0, 22.1, 25.7, 25.0, 20.4, 14.5, 9.2, 4.3])
city_a_2019 = np.array([3.2, 4.1, 7.8, 12.4, 18.1, 22.3, 25.9, 25.3, 20.7, 14.8, 9.4, 4.4])
city_a_2020 = np.array([3.3, 4.3, 8.0, 12.5, 18.3, 22.5, 26.0, 25.4, 20.9, 15.0, 9.6, 4.5])

# Monthly average temperatures (°C) for City B over five years
city_b_2016 = np.array([10.1, 12.0, 17.5, 22.3, 27.9, 32.2, 35.5, 34.9, 30.3, 24.2, 18.1, 12.1])
city_b_2017 = np.array([10.0, 11.9, 17.4, 22.1, 27.8, 32.3, 35.8, 35.0, 30.5, 24.0, 18.0, 11.8])
city_b_2018 = np.array([10.2, 12.1, 17.6, 22.4, 28.0, 32.5, 36.0, 35.2, 30.7, 24.3, 18.3, 12.2])
city_b_2019 = np.array([10.5, 12.3, 17.8, 22.6, 28.2, 32.7, 36.2, 35.4, 30.9, 24.5, 18.5, 12.3])
city_b_2020 = np.array([10.6, 12.4, 17.9, 22.8, 28.3, 32.9, 36.3, 35.5, 31.0, 24.7, 18.6, 12.4])

# Plotting the data
plt.figure(figsize=(14, 8))

# Plotting City A temperatures
plt.plot(months, city_a_2016, marker='o', label='City A 2016', color='#1f77b4')
plt.plot(months, city_a_2017, marker='s', label='City A 2017', color='#ff7f0e')
plt.plot(months, city_a_2018, marker='^', label='City A 2018', color='#2ca02c')
plt.plot(months, city_a_2019, marker='d', label='City A 2019', color='#d62728')
plt.plot(months, city_a_2020, marker='*', label='City A 2020', color='#9467bd')

# Plotting City B temperatures
plt.plot(months, city_b_2016, marker='o', linestyle='dashed', label='City B 2016', color='#17becf')
plt.plot(months, city_b_2017, marker='s', linestyle='dashed', label='City B 2017', color='#bcbd22')
plt.plot(months, city_b_2018, marker='^', linestyle='dashed', label='City B 2018', color='#8c564b')
plt.plot(months, city_b_2019, marker='d', linestyle='dashed', label='City B 2019', color='#e377c2')
plt.plot(months, city_b_2020, marker='*', linestyle='dashed', label='City B 2020', color='#7f7f7f')

# Customizing the chart
plt.title("Average Monthly Temperatures Over 5 Years\n(2016-2020) in City A and City B", fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.legend(loc='upper left', fontsize=10, title='Cities and Years', bbox_to_anchor=(1.05, 1))
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Adding annotations for significant temperature differences
plt.annotate('Hot Summer in City B (2020)', xy=('Jul', 36.3), xytext=('May', 34),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')
plt.annotate('Cool Spring in City A (2017)', xy=('Apr', 11.8), xytext=('Feb', 14),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the chart
plt.show()