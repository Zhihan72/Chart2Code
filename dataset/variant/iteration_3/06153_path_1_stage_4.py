import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2000, 2021)
fiction_books = np.array([320, 340, 355, 365, 370, 392, 410, 425, 450, 470, 495, 525, 550, 575, 600, 625, 640, 670, 685, 700, 720])
non_fiction_books = np.array([200, 220, 235, 245, 260, 280, 295, 315, 340, 360, 380, 395, 410, 430, 455, 475, 490, 510, 530, 545, 560])
scifi_books = np.array([150, 160, 170, 185, 200, 215, 220, 230, 245, 260, 275, 290, 305, 320, 335, 350, 365, 380, 390, 405, 420])
mystery_books = np.array([100, 110, 120, 130, 140, 155, 170, 185, 200, 220, 240, 255, 270, 290, 300, 320, 340, 360, 375, 390, 410])

# Calculate total and sort
total_books_per_genre = fiction_books + non_fiction_books + scifi_books + mystery_books
sorted_indices = np.argsort(total_books_per_genre)

# Sorting
years = years[sorted_indices]
fiction_books = fiction_books[sorted_indices]
non_fiction_books = non_fiction_books[sorted_indices]
scifi_books = scifi_books[sorted_indices]
mystery_books = mystery_books[sorted_indices]

# Plot
fig, ax = plt.subplots(figsize=(14, 7))
width = 0.2
x = np.arange(len(years))

# Bar chart
ax.bar(x - 1.5*width, fiction_books, width, color='firebrick', label='Fiction')
ax.bar(x - 0.5*width, non_fiction_books, width, color='mediumvioletred', label='Non-Fiction')
ax.bar(x + 0.5*width, scifi_books, width, color='dodgerblue', label='Sci-Fi')
ax.bar(x + 1.5*width, mystery_books, width, color='seagreen', label='Mystery')

ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.grid(True, linestyle='--', alpha=0.6)
ax.set_axisbelow(True)

plt.tight_layout()
plt.show()