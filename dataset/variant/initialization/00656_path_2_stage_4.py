import matplotlib.pyplot as plt
import numpy as np

cities = ['Sydney', 'Tokyo', 'London', 'São Paulo', 'New York']
year_index = 0

# Randomly different UCRI scores maintaining original dimensions
ucri_scores = np.array([
    [80, 68, 75, 72, 70, 68, 77, 83, 86, 88],
    [76, 74, 78, 90, 82, 77, 85, 83, 87, 80],
    [67, 65, 80, 84, 76, 72, 74, 69, 82, 78],
    [62, 60, 70, 73, 66, 77, 64, 72, 75, 68],
    [70, 72, 86, 88, 80, 75, 83, 68, 85, 77]
])

ucri_scores_2025 = ucri_scores[:, year_index]

fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(cities, ucri_scores_2025, color='mediumseagreen')

ax.set_xlabel('UCRI Score')
ax.set_title('UCRI Score for Cities in 2025')

plt.show()