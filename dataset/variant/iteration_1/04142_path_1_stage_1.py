import matplotlib.pyplot as plt

# Data for the pie chart
product_lines = ['Smartphones', 'Laptops', 'Wearables', 'Home Automation', 'Cloud Services']
revenue_percentages = [45, 25, 15, 10, 5]  # Total adds up to 100%

# Setting a single color for all product lines
color = '#4682B4'

# Exploding the 'Smartphones' slice to highlight it
explode = (0.1, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    revenue_percentages,
    labels=product_lines,
    autopct='%1.1f%%',
    startangle=140,
    colors=[color] * len(product_lines),  # Apply the single color
    explode=explode,
    shadow=True,
    wedgeprops=dict(edgecolor='w')
)

# Customizing the text properties
plt.setp(autotexts, size=12, weight='bold', color='black')
plt.setp(texts, size=12)

# Setting the title
plt.title('Revenue Breakdown of TechnoCorp in 2023 by Product Line', fontsize=14, fontweight='bold')

# Adding a legend for clarity
ax.legend(wedges, product_lines, title="Product Lines", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)

# Ensuring a round pie chart
ax.axis('equal')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()