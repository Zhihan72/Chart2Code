import numpy as np
import matplotlib.pyplot as plt

months = np.arange(1, 133)

fiction = 15 + 3 * np.sin(np.linspace(0, 10 * np.pi, 132)) + np.linspace(0, 5, 132)
mystery = 12 + 4 * np.sin(np.linspace(0, 6 * np.pi, 132)) + np.linspace(2, 8, 132)
science_fiction = 8 + 5 * np.sin(np.linspace(0, 8 * np.pi, 132)) + np.linspace(1, 7, 132)
non_fiction = 10 + 2 * np.sin(np.linspace(0, 12 * np.pi, 132)) + np.linspace(1, 3, 132)
fantasy = 9 + 4 * np.sin(np.linspace(0, 9 * np.pi, 132)) + np.linspace(1, 6, 132)
romance = 11 + 3.5 * np.sin(np.linspace(0, 11 * np.pi, 132)) + np.linspace(2, 9, 132)
horror = 7 + 5.5 * np.sin(np.linspace(0, 7 * np.pi, 132)) + np.linspace(1, 5, 132)

data = np.vstack([fiction, mystery, science_fiction, non_fiction, fantasy, romance, horror])

plt.figure(figsize=(14, 8))

# Randomly changed colors for the stackplot
plt.stackplot(months, data, colors=['teal', 'gold', 'limegreen', 'orchid', 'crimson', 'mediumslateblue', 'salmon'])

# Randomly altered grid and border style
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(True, linestyle='-', alpha=0.5)

# Added random legend location and more visible border
plt.legend(['Fiction', 'Mystery', 'Science Fiction', 'Non-Fiction', 'Fantasy', 'Romance', 'Horror'], loc='upper left', fontsize=10)
plt.gca().spines['top'].set_linewidth(1.5)
plt.gca().spines['right'].set_linewidth(1.5)

plt.tight_layout()
plt.show()