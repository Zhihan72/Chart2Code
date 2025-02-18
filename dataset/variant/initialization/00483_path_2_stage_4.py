import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Randomly altered the contents within data groups while maintaining structure
fantasy = np.array([19, 17, 18, 22, 20, 19, 15, 18, 21, 20, 19])
sci_fi = np.array([13, 22, 15, 16, 14, 20, 23, 12, 18, 21, 11])
mystery = np.array([24, 19, 18, 15, 20, 25, 21, 23, 18, 16, 17])
romance = np.array([21, 24, 22, 23, 26, 23, 25, 20, 25, 23, 22])
non_fiction = np.array([27, 23, 18, 21, 17, 28, 21, 18, 22, 22, 18])

fig, ax = plt.subplots(figsize=(14, 8))

new_colors = ['#e63946', '#a8dadc', '#457b9d', '#f4a261', '#2a9d8f']
ax.stackplot(years, fantasy, sci_fi, mystery, romance, non_fiction,
             colors=new_colors, alpha=0.85)

ax.set_title('Reading Preferences (2010-2020)', fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('% Readership', fontsize=14)

plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
plt.tight_layout()

plt.show()