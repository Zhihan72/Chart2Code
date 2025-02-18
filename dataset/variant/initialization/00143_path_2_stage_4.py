import numpy as np
import matplotlib.pyplot as plt

fantasy = np.array([20, 25, 30, 45, 65, 80, 95, 110, 130, 145, 160])
mystery = np.array([30, 35, 40, 45, 50, 55, 65, 70, 75, 85, 90])
science_fiction = np.array([15, 20, 28, 35, 45, 55, 70, 85, 100, 115, 130])
romance = np.array([25, 30, 35, 40, 45, 50, 60, 70, 80, 85, 95])
non_fiction = np.array([10, 15, 20, 25, 30, 40, 50, 55, 60, 65, 70])
historical = np.array([5, 10, 15, 20, 25, 35, 45, 50, 60, 70, 75])
horror = np.array([8, 10, 13, 17, 20, 28, 37, 45, 55, 65, 70])

genre_data = [fantasy, mystery, science_fiction, romance, non_fiction, historical, horror]
labels = ['Fan.', 'Myst.', 'Sci-Fi', 'Rom.', 'Non-Fic.', 'Hist.', 'Hor.']

fig, ax = plt.subplots(figsize=(14, 9))

ax.boxplot(genre_data, vert=False, patch_artist=True, labels=labels)

ax.set_title("Genre Popularity (2010-2020)", fontsize=18, fontweight='bold')
ax.set_xlabel('Popularity (Units)', fontsize=14)
ax.set_ylabel('Genre Type', fontsize=14)

plt.tight_layout()

plt.show()