import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
temperature = [5, 7, 12, 18, 22, 25, 27, 26, 22, 16, 10, 6]

# Create a single plot for average monthly temperature line chart
fig, ax = plt.subplots(figsize=(14, 5))

ax.plot(months, temperature, color='purple', marker='o', linestyle='-', linewidth=2, markersize=5, label='Temperature (°C)')
ax.set_title('WeatherVille Monthly Temperature Trends', fontsize=16, fontweight='bold')
ax.set_xlabel('Months', fontsize=12)
ax.set_ylabel('Temperature (°C)', fontsize=12)
ax.legend(loc='upper right')
ax.grid(True, which='both', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()