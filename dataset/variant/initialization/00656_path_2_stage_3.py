import matplotlib.pyplot as plt
import numpy as np

cities = ['Sydney', 'Tokyo', 'London', 'São Paulo', 'New York']
year_index = 0  # Index for the year 2025

ucri_scores = np.array([
    [86, 88, 85, 83, 80, 77, 75, 72, 70, 68],
    [87, 90, 85, 83, 82, 80, 78, 77, 76, 74],
    [82, 84, 80, 78, 76, 74, 72, 69, 67, 65],
    [75, 77, 73, 72, 70, 68, 66, 64, 62, 60],
    [86, 88, 85, 83, 80, 77, 75, 72, 70, 68]
])
# Average UCRI scores for 2025
ucri_scores_2025 = ucri_scores[:, year_index]

fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(cities, ucri_scores_2025, color='mediumseagreen')

ax.set_xlabel('UCRI Score')
ax.set_title('UCRI Score for Cities in 2025')

plt.show()