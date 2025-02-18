import numpy as np
import matplotlib.pyplot as plt

years = np.array([2010, 2012, 2014, 2016, 2018, 2020])
fiction = np.array([30, 35, 40, 45, 50, 55])
non_fiction = np.array([20, 22, 25, 27, 30, 32])
sci_fi = np.array([10, 12, 14, 16, 18, 20])
fantasy = np.array([8, 10, 13, 16, 20, 25])

# Use a single color for all bars
single_color = '#a8dadc'

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.2
x_indices = np.arange(len(years))

ax.bar(x_indices, fiction, width=bar_width, color=single_color, label='Fiction', alpha=0.9)
ax.bar(x_indices + bar_width, non_fiction, width=bar_width, color=single_color, label='Non-Fiction', alpha=0.9)
ax.bar(x_indices + 2 * bar_width, sci_fi, width=bar_width, color=single_color, label='Science Fiction', alpha=0.9)
ax.bar(x_indices + 3 * bar_width, fantasy, width=bar_width, color=single_color, label='Fantasy', alpha=0.9)

ax.set_title("The Rise and Influence of Literary Genres\nOver a Decade", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Number of Checkouts (Thousands)", fontsize=12)

ax.set_xticks(x_indices + 1.5 * bar_width)
ax.set_xticklabels(years, rotation=45, ha='right')

ax.legend(loc='upper left', title="Genres", bbox_to_anchor=(1.05, 1), fontsize=10, title_fontsize='12', frameon=False)

plt.tight_layout()
plt.show()