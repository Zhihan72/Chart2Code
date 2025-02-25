import matplotlib.pyplot as plt
import numpy as np

# Months
months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

# Temperatures in °C
sf_temps = np.array([18, 13, 17, 11, 16, 14, 12, 18, 15, 12, 17, 11])
ny_temps = np.array([10, 27, 4, 0, 24, 13, 2, 22, 18, 7, 16, 26])
tk_temps = np.array([19, 26, 15, 14, 22, 27, 10, 6, 9, 5, 24, 19])
pa_temps = np.array([22, 5, 12, 9, 16, 21, 14, 19, 9, 18, 6, 6])
sy_temps = np.array([14, 23, 22, 19, 20, 16, 18, 13, 14, 16, 23, 22])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each city's data
ax.plot(months, sf_temps, label='SF', color='tab:blue', marker='o', linestyle='-')
ax.plot(months, ny_temps, label='NY', color='tab:orange', marker='o', linestyle='-')
ax.plot(months, tk_temps, label='TK', color='tab:green', marker='o', linestyle='-')
ax.plot(months, pa_temps, label='PA', color='tab:red', marker='o', linestyle='-')
ax.plot(months, sy_temps, label='SY', color='tab:purple', marker='o', linestyle='-')

# Title and labels
ax.set_title('Avg Monthly Temps 2022', fontsize=16, fontweight='bold')
ax.set_xlabel('Months', fontsize=14)
ax.set_ylabel('Temp (°C)', fontsize=14)

# Add a legend
ax.legend(title='City', fontsize=12, title_fontsize=14, loc='upper right')

# Customize grid
ax.grid(True, linestyle='--', alpha=0.7)

# Annotate specific points
for (month, temp_sf) in zip(months, sf_temps):
    if temp_sf in [14, 22]:
        ax.annotate(f'{temp_sf}°C', xy=(month, temp_sf), xytext=(5, -15), 
                    textcoords='offset points', arrowprops=dict(arrowstyle='->', lw=1))

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()