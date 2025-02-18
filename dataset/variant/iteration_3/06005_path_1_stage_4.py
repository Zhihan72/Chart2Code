import matplotlib.pyplot as plt

# Data for temperature readings over a week in degrees Celsius
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
year_2022_temps = [32, 31, 30, 29, 28, 30, 29]  
year_2023_temps = [31, 34, 32, 33, 30, 32, 33]  

fig, ax = plt.subplots(figsize=(12, 6))

# Plotting the line charts with shuffled colors for temperature variations in 2022 and 2023
ax.plot(days, year_2022_temps, marker='o', linestyle='-', color='green')
ax.plot(days, year_2023_temps, marker='v', linestyle='--', color='blue')

# Automatically adjust the layout
plt.tight_layout()

# Display the chart
plt.show()