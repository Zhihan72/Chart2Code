import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

fantasy = np.array([22, 17, 15, 21, 20, 19, 18, 18, 19, 20, 19])
sci_fi = np.array([12, 22, 13, 14, 15, 16, 11, 20, 21, 18, 23])
mystery = np.array([23, 25, 24, 21, 20, 19, 18, 18, 17, 16, 15])
romance = np.array([23, 21, 24, 23, 25, 22, 20, 26, 25, 24, 21])
non_fiction = np.array([23, 28, 27, 21, 22, 22, 21, 18, 18, 18, 17])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, fantasy, sci_fi, mystery, romance, non_fiction,
             colors=['#f6b393', '#f7e1a0', '#aad6a1', '#c9d1d3', '#b0a8d0'], alpha=0.85)

ax.set_title('Tracking Reading Preferences: Genres & Trends\n(Reading Evolution)', fontsize=18, fontweight='bold', loc='center')
ax.set_xlabel('Time Period', fontsize=14)
ax.set_ylabel('Reading Percentage Share', fontsize=14)

plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)

plt.tight_layout()
plt.show()