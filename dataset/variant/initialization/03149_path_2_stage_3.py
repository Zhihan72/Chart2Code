import numpy as np
import matplotlib.pyplot as plt

months = np.arange(1, 133)
genres = ['Fic', 'Myst', 'Sci-Fi', 'Non-Fic', 'Fant']

fiction = 15 + 3 * np.sin(np.linspace(0, 10 * np.pi, 132)) + np.linspace(0, 5, 132)
mystery = 12 + 4 * np.sin(np.linspace(0, 6 * np.pi, 132)) + np.linspace(2, 8, 132)
science_fiction = 8 + 5 * np.sin(np.linspace(0, 8 * np.pi, 132)) + np.linspace(1, 7, 132)
non_fiction = 10 + 2 * np.sin(np.linspace(0, 12 * np.pi, 132)) + np.linspace(1, 3, 132)
fantasy = 9 + 4 * np.sin(np.linspace(0, 9 * np.pi, 132)) + np.linspace(1, 6, 132)

data = np.vstack([fiction, mystery, science_fiction, non_fiction, fantasy])

plt.figure(figsize=(14, 8))
plt.stackplot(months, data, labels=genres, colors=['plum', 'lightgreen', 'skyblue', 'lightcoral', 'goldenrod'], alpha=0.8)

plt.title("Book Club Preferences Over Time", fontsize=16, pad=20)
plt.xlabel("Months since Jan 2010", fontsize=12, style='italic')
plt.ylabel("Avg Books Read/Month", fontsize=12, style='italic')

plt.xticks(np.arange(0, 132, step=12), ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'], fontsize=10)
plt.yticks(fontsize=10)

plt.legend(loc='lower center', fontsize=10, bbox_to_anchor=(0.5, -0.2), ncol=3, frameon=False)
plt.grid(True, linestyle='-', linewidth=0.5)

plt.tight_layout()
plt.show()