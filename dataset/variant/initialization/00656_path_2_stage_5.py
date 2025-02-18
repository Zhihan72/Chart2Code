import matplotlib.pyplot as plt
import numpy as np

cities = ['Sydney', 'Tokyo', 'London', 'São Paulo', 'New York']

# UCRI scores for 2025 based on initial array
ucri_scores_2025 = np.array([80, 76, 67, 62, 70])

fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(cities, ucri_scores_2025, color='mediumseagreen')

ax.set_xlabel('UCRI Score')
ax.set_title('UCRI Score for Cities in 2025')

plt.show()