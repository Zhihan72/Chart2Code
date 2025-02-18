import matplotlib.pyplot as plt

# Data for temperature readings over a week in degrees Celsius
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
year_2022_temps = [30, 32, 31, 29, 28, 29, 30]
year_2023_temps = [32, 33, 34, 32, 31, 30, 33]

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(days, year_2022_temps, marker='o', linestyle='-', color='blue', label='2022')
ax.plot(days, year_2023_temps, marker='v', linestyle='--', color='green', label='2023')

# Titles and labels
ax.set_title("Temp Changes: Tropica\n2022 vs 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Days', fontsize=14)
ax.set_ylabel('Temp (°C)', fontsize=14)

# Annotations at each data point
for i, temp in enumerate(year_2022_temps):
    ax.annotate(f'{temp}°C', xy=(days[i], temp), xytext=(5, 5), textcoords='offset points', fontsize=10, color='blue')

for i, temp in enumerate(year_2023_temps):
    ax.annotate(f'{temp}°C', xy=(days[i], temp), xytext=(5, -15), textcoords='offset points', fontsize=10, color='green')

# Legend
ax.legend(loc='upper right', fontsize=12, frameon=False)

# Grid lines
ax.grid(True, linestyle='--', which='both', color='grey', alpha=0.6)

# Adjust layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()