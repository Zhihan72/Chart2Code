import numpy as np
import matplotlib.pyplot as plt

years = np.array([2010, 2012, 2014, 2016, 2018, 2020])

fiction = np.array([30, 35, 40, 45, 50, 55])
non_fiction = np.array([20, 22, 25, 27, 30, 32])
mystery = np.array([15, 17, 19, 21, 25, 28])
sci_fi = np.array([10, 12, 14, 16, 18, 20])
fantasy = np.array([8, 10, 13, 16, 20, 25])

colors = ['#f4a261', '#2a9d8f', '#a8dadc', '#457b9d', '#e63946']

# Define the width of the bars and their position
bar_width = 0.15
indices = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 8))

# Plot each genre as a separate bar in a group
ax.bar(indices, fiction, width=bar_width, color=colors[0], label='Fiction')
ax.bar(indices + bar_width, non_fiction, width=bar_width, color=colors[1], label='Non-Fiction')
ax.bar(indices + 2*bar_width, mystery, width=bar_width, color=colors[2], label='Mystery')
ax.bar(indices + 3*bar_width, sci_fi, width=bar_width, color=colors[3], label='Sci-Fi')
ax.bar(indices + 4*bar_width, fantasy, width=bar_width, color=colors[4], label='Fantasy')

ax.set_xticks(indices + 2*bar_width)
ax.set_xticklabels(years, rotation=45, ha='right')

ax.set_title("Trends in Book Genres\nfrom 2010 to 2020", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Publication Year", fontsize=12)
ax.set_ylabel("Borrowings (Thousands)", fontsize=12)

ax.legend()

plt.tight_layout()

plt.show()