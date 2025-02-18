import matplotlib.pyplot as plt

# Backstory:
# This chart illustrates the distribution of different categories of books in a fictional library. 
# The data represents the percentage of books in each category, showing the diversity in reading materials available.

# Book categories and their respective distribution percentages
categories = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy', 'Biographies', 'Mystery']
distribution = [30, 20, 15, 15, 10, 10]

# Define distinct colors for each category
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFD700', '#FFB6C1', '#DA70D6']

# Create a figure for the pie chart
fig, ax = plt.subplots(figsize=(10, 7))

# Create the pie chart
wedges, texts, autotexts = ax.pie(
    distribution, 
    labels=categories, 
    colors=colors,
    autopct='%1.1f%%', 
    startangle=90,
    explode=(0.05, 0, 0, 0, 0, 0),  # Explode the Fiction slice for emphasis
    shadow=True
)

# Customize text appearance for the pie chart
for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# Ensure the pie chart is a circle
ax.axis('equal')

# Add title to the pie chart
ax.set_title('Book Categories Distribution\nin the Fictional Library - 2023', fontsize=16, fontweight='bold', pad=20)

# Add a legend for clarity
ax.legend(wedges, categories, loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), title="Categories", fontsize='small', title_fontsize='13')

# Automatically adjust layout for a clear presentation
plt.tight_layout()

# Display the chart
plt.show()