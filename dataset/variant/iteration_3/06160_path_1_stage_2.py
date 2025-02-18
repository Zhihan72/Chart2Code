import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
temps_2021 = np.array([3, 5, 9, 14, 18, 22, 25, 24, 20, 14, 8, 4])
temps_2022 = np.array([2, 4, 8, 13, 17, 21, 24, 23, 19, 13, 7, 3])
temps_2023 = np.array([1, 3, 7, 12, 16, 20, 23, 22, 18, 12, 6, 2])

fig, ax = plt.subplots(figsize=(12, 6))

# Plot each year's data with the same color
ax.plot(months, temps_2021, marker='v', linestyle=':', color='b', linewidth=2, label='2021')
ax.plot(months, temps_2022, marker='x', linestyle='-.', color='b', linewidth=2, label='2022')
ax.plot(months, temps_2023, marker='p', linestyle='-', color='b', linewidth=2, label='2023')

ax.set_title('Monthly Temperature Trends in Climata (2021-2023)', fontsize=16, fontweight='bold')
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Average Temperature (°C)', fontsize=14)

plt.xticks(rotation=45)
ax.legend(loc='upper left', fontsize=11, title='Year', shadow=True)
ax.grid(alpha=0.5, linestyle='-', linewidth=1)

# Annotate each data point with temperatures using the same color
for i, txt in enumerate(temps_2021):
    ax.annotate(f'{txt}°C', (months[i], temps_2021[i]), textcoords="offset points", xytext=(-10, 10), ha='center', fontsize=9, color='b')
for i, txt in enumerate(temps_2022):
    ax.annotate(f'{txt}°C', (months[i], temps_2022[i]), textcoords="offset points", xytext=(-10, 10), ha='center', fontsize=9, color='b')
for i, txt in enumerate(temps_2023):
    ax.annotate(f'{txt}°C', (months[i], temps_2023[i]), textcoords="offset points", xytext=(-10, 10), ha='center', fontsize=9, color='b')

plt.tight_layout()

plt.show()