import matplotlib.pyplot as plt
import numpy as np

# Define the genres of books and their corresponding percentages
genres = ['Science Fiction', 'Romance', 'Mystery', 'Fantasy', 'Non-Fiction', 'Historical']
distribution = [20, 25, 15, 20, 10, 10]

# Hypothetical trend data for each genre over recent years
years = ['2018', '2019', '2020', '2021', '2022']
trend_data = {
    'Science Fiction': [15, 17, 20, 22, 20],
    'Romance': [22, 23, 25, 24, 25],
    'Mystery': [12, 14, 15, 16, 15],
    'Fantasy': [18, 19, 20, 22, 20],
    'Non-Fiction': [10, 11, 10, 9, 10],
    'Historical': [8, 9, 10, 10, 10]
}

# Colors for pie and bars
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Create the figure and axes
fig, ax = plt.subplots(figsize=(14, 8), subplot_kw=dict(aspect="equal"))

# Create the pie chart
wedges, texts, autotexts = ax.pie(
    distribution, labels=genres, colors=colors,
    autopct='%1.1f%%', startangle=140, pctdistance=0.85,
    wedgeprops=dict(width=0.3), shadow=True, explode=(0.05,) * len(genres)
)

# Customizing text properties for pie chart
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
for text in texts:
    text.set_fontsize(11)

# Adding a legend for the pie chart
ax.legend(wedges, genres, title="Book Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Create secondary axes for overlaying a line chart
ax2 = ax.twinx()

# Set up line chart
x = np.arange(len(years))

# Plot lines for each genre
for i, genre in enumerate(genres):
    ax2.plot(x, trend_data[genre], marker='o', linestyle='-', color=colors[i], label=genre)

# Customizing the overlay line chart
ax2.set_ylabel('Annual Popularity Trend (%)', fontsize=12)
ax2.set_xticks(x)
ax2.set_xticklabels(years, fontsize=10)
ax2.set_ylim(0, 30)
ax2.legend(title="Yearly Trends", loc="upper left", bbox_to_anchor=(1.05, 1))

# Customize the plot title
plt.title("Evolution of Literary Tastes:\nCurrent Distribution and Trends Over Time", 
          fontsize=14, fontweight='bold', pad=20)

# Adjust layout for readability
plt.tight_layout()

# Display the plot
plt.show()