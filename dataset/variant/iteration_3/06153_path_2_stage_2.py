import matplotlib.pyplot as plt
import numpy as np

# Years and altered data
years = np.arange(2000, 2021)
fiction_books = [320, 355, 365, 392, 425, 470, 550, 600, 670, 720, 340, 410, 370, 450, 495, 525, 575, 640, 685, 700, 625]
non_fiction_books = [200, 235, 295, 380, 410, 530, 220, 260, 340, 395, 245, 360, 280, 315, 430, 455, 490, 475, 545, 560, 510]
scifi_books = [175, 160, 215, 235, 245, 290, 320, 405, 170, 420, 230, 245, 185, 220, 200, 275, 305, 335, 350, 365, 380]

# Create plot
fig, ax = plt.subplots(figsize=(14, 7))
width = 0.25
x = np.arange(len(years))

rects1 = ax.bar(x - width, fiction_books, width, label='Fiction', color='tomato')
rects2 = ax.bar(x, non_fiction_books, width, label='Non-Fiction', color='cornflowerblue')
rects3 = ax.bar(x + width, scifi_books, width, label='Science Fiction', color='gold')

# Set labels and title
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Books Published', fontsize=12)
ax.set_title('Trends in Book Publications (2000-2020)', fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()

# Add labels on top of bars
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10)

add_labels(rects1)
add_labels(rects2)
add_labels(rects3)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.grid(True, linestyle='--', alpha=0.6)
ax.set_axisbelow(True)

plt.tight_layout()
plt.show()