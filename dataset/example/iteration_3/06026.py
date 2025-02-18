import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# We are showcasing the distribution of different genres in a fictional eBook reading community.
# The genres have been gaining various levels of popularity over the past few years.
# We will display this data using a pie chart to visualize the popularity of each genre.

# List of genres
genres = ['Science Fiction', 'Mystery', 'Romance', 'Fantasy', 'Non-fiction']

# Percentage popularity of each genre
popularity = [30, 20, 25, 15, 10]  # Percentages

# Colors for the pie segments
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Explode settings to highlight 'Science Fiction' and 'Romance' slices
explode = (0.1, 0, 0.1, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(7, 7))
wedges, texts, autotexts = ax.pie(popularity, labels=genres, colors=colors, autopct='%1.1f%%', startangle=140,
                                  explode=explode, shadow=True, wedgeprops={'edgecolor': 'black'}, textprops={'fontsize': 12})

# Title of the pie chart
ax.set_title("eBook Genre Popularity in a Fictional Community\n(Last Five Years)", fontsize=14, fontweight='bold', pad=20)

# Customize the percentage labels inside the pie chart
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Add a legend with a title
ax.legend(wedges, genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10)

# Automatically adjust layout for the best fit
plt.tight_layout()

# Display the pie chart
plt.show()