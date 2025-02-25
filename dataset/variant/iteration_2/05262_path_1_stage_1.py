import matplotlib.pyplot as plt

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
    startangle=45,
    explode=(0.05, 0, 0.1, 0, 0, 0.1),  # Explode the Fiction and Mystery slices for emphasis
    shadow=False  # Removed shadow for a cleaner look
)

# Customize text appearance for the pie chart
for text in texts:
    text.set_fontsize(14)

for autotext in autotexts:
    autotext.set_color('blue')
    autotext.set_fontsize(12)

# Added gridlines to enhance presentation
ax.grid(which='both', linestyle='--', linewidth=0.5)

# Add a different title style for the pie chart
ax.set_title('Book Categories in the Fictional Library', fontsize=18, style='italic', pad=15)

# Slightly modified legend position and style
ax.legend(wedges, categories, loc='upper right', bbox_to_anchor=(0.9, 1), title="Categories")

# Automatically adjust layout for a clear presentation
plt.tight_layout()

# Display the chart
plt.show()