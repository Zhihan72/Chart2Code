import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2000, 2021)
fiction_books = np.array([320, 340, 355, 365, 370, 392, 410, 425, 450, 470, 495, 525, 550, 575, 600, 625, 640, 670, 685, 700, 720])
non_fiction_books = np.array([200, 220, 235, 245, 260, 280, 295, 315, 340, 360, 380, 395, 410, 430, 455, 475, 490, 510, 530, 545, 560])
scifi_books = np.array([150, 160, 170, 185, 200, 215, 220, 230, 245, 260, 275, 290, 305, 320, 335, 350, 365, 380, 390, 405, 420])

# Calculate totals and sort
total_books_per_genre = fiction_books + non_fiction_books + scifi_books
sorted_indices = np.argsort(total_books_per_genre)

# Sorting
years = years[sorted_indices]
fiction_books = fiction_books[sorted_indices]
non_fiction_books = non_fiction_books[sorted_indices]
scifi_books = scifi_books[sorted_indices]

# Plot
fig, ax = plt.subplots(figsize=(14, 7))
width = 0.25
x = np.arange(len(years))

# Bar chart
ax.bar(x - width, fiction_books, width, color='firebrick')
ax.bar(x, non_fiction_books, width, color='mediumvioletred')
ax.bar(x + width, scifi_books, width, color='dodgerblue')

ax.set_xticks(x)
ax.set_xticklabels(years)

# Remove spines and grids for minimalism
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Grid
ax.yaxis.grid(True, linestyle='--', alpha=0.6)
ax.set_axisbelow(True)

plt.tight_layout()
plt.show()