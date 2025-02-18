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

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Books Published', fontsize=12)
ax.set_title('Trends in Book Publications (2000-2020)', fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(years)

def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10)

add_labels(ax.patches[:len(years)])
add_labels(ax.patches[len(years):2*len(years)])
add_labels(ax.patches[2*len(years):])

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_axisbelow(True)

plt.tight_layout()
plt.show()