import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analyzing the popularity of various genres of books from 2000 to 2020.
# This chart will show the number of books published each year in three genres: Fiction, Non-Fiction, and Science Fiction.

# Defining the years and data
years = np.arange(2000, 2021)
fiction_books = [320, 340, 355, 365, 370, 392, 410, 425, 450, 470, 495, 525, 550, 575, 600, 625, 640, 670, 685, 700, 720]
non_fiction_books = [200, 220, 235, 245, 260, 280, 295, 315, 340, 360, 380, 395, 410, 430, 455, 475, 490, 510, 530, 545, 560]
scifi_books = [150, 160, 170, 185, 200, 215, 220, 230, 245, 260, 275, 290, 305, 320, 335, 350, 365, 380, 390, 405, 420]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 7))

# Plotting the bar chart on years
width = 0.25  # Width of the bars
x = np.arange(len(years))

rects1 = ax.bar(x - width, fiction_books, width, label='Fiction', color='mediumseagreen')
rects2 = ax.bar(x, non_fiction_books, width, label='Non-Fiction', color='royalblue')
rects3 = ax.bar(x + width, scifi_books, width, label='Science Fiction', color='darkorange')

# Add some text for labels, title, and custom x-axis tick labels, etc.
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Books Published', fontsize=12)
ax.set_title('Trends in Book Publications (2000-2020)', fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()

# Function to add labels on top of the bars
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10)

add_labels(rects1)
add_labels(rects2)
add_labels(rects3)

# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Draw grid lines behind bars
ax.yaxis.grid(True, linestyle='--', alpha=0.6)
ax.set_axisbelow(True)

# Automatically adjust the layout
plt.tight_layout()

# Show the chart
plt.show()