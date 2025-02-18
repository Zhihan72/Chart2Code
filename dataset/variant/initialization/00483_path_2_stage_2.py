import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

fantasy = np.array([15, 17, 19, 21, 20, 19, 18, 18, 19, 20, 22])
sci_fi = np.array([12, 11, 13, 14, 15, 16, 18, 20, 21, 22, 23])
mystery = np.array([25, 24, 23, 21, 20, 19, 18, 18, 17, 16, 15])
romance = np.array([20, 21, 22, 23, 23, 24, 25, 26, 25, 24, 23])
non_fiction = np.array([28, 27, 23, 21, 22, 22, 21, 18, 18, 18, 17])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, fantasy, sci_fi, mystery, romance, non_fiction,
             colors=['#c9d1d3', '#aad6a1', '#f6b393', '#f7e1a0', '#b0a8d0'], alpha=0.85)

ax.set_title('Reading Preferences (2010-2020)', fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('% Readership', fontsize=14)

plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
plt.tight_layout()

plt.show()