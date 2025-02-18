import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2030, 2040)

# Total tourists for each year
total_tourists = [
    sum(x) for x in zip([20, 22, 27, 35, 40, 43, 45, 50, 56, 65],
                        [15, 18, 21, 26, 30, 32, 37, 40, 44, 50],
                        [10, 12, 15, 19, 23, 28, 31, 35, 38, 42],
                        [8, 10, 12, 15, 20, 24, 27, 30, 33, 38],
                        [5, 7, 10, 12, 16, 18, 21, 25, 28, 30],
                        [12, 14, 18, 22, 26, 30, 33, 37, 41, 46])
]

# Sorting the total tourists and corresponding years
sorted_indices = np.argsort(total_tourists)
sorted_years = np.array(years)[sorted_indices]
sorted_totals = np.array(total_tourists)[sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))

# Plot sorted bar chart
ax.bar(sorted_years, sorted_totals, color='#87ceeb')

ax.set_xlabel('Year')
ax.set_ylabel('Total Tourists')
ax.set_title('Total Tourists Per Year (Sorted)')
ax.set_xticks(years)
ax.set_xticklabels(sorted_years)

plt.tight_layout()
plt.show()