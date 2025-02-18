import matplotlib.pyplot as plt
import numpy as np

years = np.array([2019, 2020, 2021, 2022, 2023])
gardens_created = np.array([5, 15, 25, 40, 60])
average_area = np.array([200, 250, 300, 350, 400])

fig, ax1 = plt.subplots(figsize=(10, 6))

bar_width = 0.35
ax1.barh(years, gardens_created, bar_width, color='#ff9999', label='Gardens Created')
ax1.plot(average_area, years, color='#66b3ff', marker='o', linestyle='-', lw=2, markerfacecolor='#66b3ff', label='Average Area')

ax1.set_yticks(years)
ax1.set_yticklabels(years)

plt.tight_layout()
plt.show()