import matplotlib.pyplot as plt
import numpy as np

# Backstory: The chart displays the yearly book sales of different genres in a fictitious bookstore from 2015-2020.
genres = ['Science Fiction', 'Romance', 'Thriller', 'Non-Fiction', 'Fantasy']
years = [2015, 2016, 2017, 2018, 2019, 2020]

# Sales data in number of books sold
sales_data = {
    'Science Fiction': [500, 550, 600, 650, 700, 750],
    'Romance': [450, 470, 500, 530, 580, 620],
    'Thriller': [700, 720, 740, 760, 780, 800],
    'Non-Fiction': [300, 320, 340, 360, 380, 400],
    'Fantasy': [650, 680, 700, 720, 750, 780]
}

# Colors assigned to each genre for better visual distinction
color_map = plt.cm.get_cmap('tab10', len(genres))

# Creating a bar chart for each year
fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(18, 12))
ax = ax.flatten()

for i, year in enumerate(years):
    ax[i].set_title(f"Book Sales in {year}", fontsize=14, fontweight='bold')
    bars = ax[i].barh(genres, [sales_data[genre][i] for genre in genres], color=[color_map(j) for j in range(len(genres))], edgecolor='black')
    ax[i].set_xlim(0, max(max(sales) for sales in sales_data.values()) + 100)
    ax[i].set_xlabel("Books Sold", fontsize=12)
    ax[i].bar_label(bars, padding=3, fontsize=10)

# Adding a common title and adjusting layout
fig.suptitle("Yearly Book Sales by Genre (2015-2020)", fontsize=18, fontweight='bold')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plot
plt.show()