import matplotlib.pyplot as plt
import numpy as np

# Data definitions
fruit_categories = ['Citrus', 'Berries', 'Tropical', 'Pomes', 'Drupes', 'Melons']
fruit_popularity = [35, 25, 20, 10, 5, 5]  # Percentages of fruits sold by category
sales_growth = [3, 4, 2, 1, 5, 2]  # Sales growth in percentage compared to the previous year
colors = ['#FFA07A', '#C71585', '#FFD700', '#98FB98', '#DDA0DD', '#00CED1']

# Create the main figure and add subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Create the bar chart in the first subplot
bars = ax1.bar(fruit_categories, sales_growth, color=colors, edgecolor='black')
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{height}%', ha='center', va='bottom', fontsize=10)

# Set the title and labels for the bar chart
ax1.set_title("Year-over-Year Sales Growth", fontsize=14, fontweight='bold')
ax1.set_ylabel("Growth Percentage", fontsize=12)
ax1.set_ylim(0, max(sales_growth) + 2)

# Create the pie chart in the second subplot
wedges, texts, autotexts = ax2.pie(fruit_popularity, labels=fruit_categories, autopct='%1.1f%%',
                                    startangle=140, colors=colors, pctdistance=0.85,
                                    wedgeprops=dict(edgecolor='white'), shadow=True)

# Customize the text and autotexts within the pie chart
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

for text in texts:
    text.set_fontsize(10)
    text.set_fontweight('normal')

# Add a title to the pie chart
ax2.set_title("2023 Farmer's Market Fruit Sales Distribution", fontsize=14, fontweight='bold')

# Add a legend outside of the pie chart
ax2.legend(wedges, fruit_categories, title="Fruit Categories", loc='center left', bbox_to_anchor=(1, 0.5), 
           fontsize=10, title_fontsize=12)

# Enhance the pie chart with a small circle in the middle to create a donut effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax2.add_artist(centre_circle)

# Adjust layout to prevent overlap and ensure neatness
plt.tight_layout()

# Show the plot
plt.show()