import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
temps_2021 = np.array([3, 5, 9, 14, 18, 22, 25, 24, 20, 14, 8, 4])
temps_2022 = np.array([2, 4, 8, 13, 17, 21, 24, 23, 19, 13, 7, 3])
temps_2023 = np.array([1, 3, 7, 12, 16, 20, 23, 22, 18, 12, 6, 2])

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(months, temps_2021, marker='o', linestyle='-', color='orange', linewidth=2)
ax.plot(months, temps_2022, marker='s', linestyle='--', color='purple', linewidth=2)
ax.plot(months, temps_2023, marker='d', linestyle='-.', color='teal', linewidth=2)

# Altered textual elements
ax.set_title('Climate Yearly Temp Variations: 2021 to 2023', fontsize=16, fontweight='bold')
ax.set_xlabel('Calendar Months', fontsize=14)
ax.set_ylabel('Avg. Temp in Celsius', fontsize=14)

plt.xticks(rotation=45)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

plt.show()