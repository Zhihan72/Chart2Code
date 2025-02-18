import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
temperature = [5, 7, 12, 18, 22, 25, 27, 26, 22, 16, 10, 6]

fig, ax = plt.subplots(figsize=(14, 5))

ax.plot(months, temperature, color='skyblue', marker='o', linestyle='-', linewidth=2, markersize=5)
ax.set_ylabel('Temp (°C)', fontsize=12)
ax.set_xlabel('Month', fontsize=12)
ax.set_title('WeatherVille Temperature Trends', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.show()