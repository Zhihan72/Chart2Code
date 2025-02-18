import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
fiction_books = [320, 355, 365, 392, 425, 470, 550, 600, 670, 720, 340, 410, 370, 450, 495, 525, 575, 640, 685, 700, 625]
non_fiction_books = [200, 235, 295, 380, 410, 530, 220, 260, 340, 395, 245, 360, 280, 315, 430, 455, 490, 475, 545, 560, 510]
scifi_books = [175, 160, 215, 235, 245, 290, 320, 405, 170, 420, 230, 245, 185, 220, 200, 275, 305, 335, 350, 365, 380]

fig, ax = plt.subplots(figsize=(14, 7))
width = 0.25
x = np.arange(len(years))

ax.bar(x - width, fiction_books, width, color='tomato')
ax.bar(x, non_fiction_books, width, color='cornflowerblue')
ax.bar(x + width, scifi_books, width, color='gold')

# Removed axis labels, group labels, and title
# Removed x-tick labels
ax.set_xticks(x)

# Removed data labels on each bar
# ax.annotate function lines are removed

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_axisbelow(True)

plt.tight_layout()
plt.show()