import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
springfield_temps = np.array([1, 3, 8, 12, 16, 20, 23, 22, 18, 13, 8, 3])
laketown_temps = np.array([-2, 0, 5, 9, 14, 18, 21, 20, 15, 9, 4, -1])

fig, ax = plt.subplots(figsize=(12, 8))

# Apply a single color ('green') consistently
single_color = 'green'
ax.plot(months, springfield_temps, marker='o', linestyle='-', color=single_color, label='Springfield')
ax.plot(months, laketown_temps, marker='o', linestyle='-.', color=single_color, label='Laketown')

ax.set_title('Annual Temperature Variations\nin Springfield and Laketown', fontsize=16, fontweight='bold')
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Temperature (°C)', fontsize=14)

ax.legend(title='Cities', fontsize=12)
ax.grid(True, linestyle='--', which='both', color='grey', alpha=0.7)

# Annotate using the single color
for i in range(len(months)):
    ax.annotate(f"{springfield_temps[i]}°C", (months[i], springfield_temps[i]), 
                textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color=single_color)
    ax.annotate(f"{laketown_temps[i]}°C", (months[i], laketown_temps[i]), 
                textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color=single_color)

plt.tight_layout()
plt.show()