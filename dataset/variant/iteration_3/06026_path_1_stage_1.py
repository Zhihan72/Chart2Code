import matplotlib.pyplot as plt
import numpy as np

# Updated genres randomly
genres = ['Adventure', 'Thriller', 'Drama', 'Horror', 'Biography']

# The same popularity percentages
popularity = [30, 20, 25, 15, 10]

# Same colors for pie segments
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Explode settings to highlight 'Adventure' and 'Drama' slices
explode = (0.1, 0, 0.1, 0, 0)

# Create the pie chart with updated text elements
fig, ax = plt.subplots(figsize=(7, 7))
wedges, texts, autotexts = ax.pie(popularity, labels=genres, colors=colors, autopct='%1.1f%%', startangle=140,
                                  explode=explode, shadow=True, wedgeprops={'edgecolor': 'black'}, textprops={'fontsize': 12})

# Changed title of the pie chart
ax.set_title("The Rising Tides of Literature Genres\n(Recent Years)", fontsize=14, fontweight='bold', pad=20)

# Customize the percentage labels inside the pie chart
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Updated legend with a new title
ax.legend(wedges, genres, title="Literature Genres", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10)

# Automatically adjust layout for the best fit
plt.tight_layout()

# Display the pie chart
plt.show()