import numpy as np
import matplotlib.pyplot as plt

years = np.array([2010, 2012, 2014, 2016, 2018, 2020])

fiction = np.array([30, 35, 40, 45, 50, 55])
non_fiction = np.array([20, 22, 25, 27, 30, 32])
mystery = np.array([15, 17, 19, 21, 25, 28])
sci_fi = np.array([10, 12, 14, 16, 18, 20])
fantasy = np.array([8, 10, 13, 16, 20, 25])

colors = ['#f4a261', '#2a9d8f', '#a8dadc', '#457b9d', '#e63946']

fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(years, fiction, color=colors[0], alpha=0.9)
ax.bar(years, non_fiction, bottom=fiction, color=colors[1], alpha=0.9)
ax.bar(years, mystery, bottom=fiction + non_fiction, color=colors[2], alpha=0.9)
ax.bar(years, sci_fi, bottom=fiction + non_fiction + mystery, color=colors[3], alpha=0.9)
ax.bar(years, fantasy, bottom=fiction + non_fiction + mystery + sci_fi, color=colors[4], alpha=0.9)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

ax.set_title("Trends in Book Genres\nfrom 2010 to 2020", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Publication Year", fontsize=12)
ax.set_ylabel("Cumulative Borrowings (Thousands)", fontsize=12)

plt.tight_layout()

plt.show()