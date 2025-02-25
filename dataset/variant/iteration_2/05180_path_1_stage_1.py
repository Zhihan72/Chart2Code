import matplotlib.pyplot as plt

# Desserts and their percentage share
desserts = ['Cakes', 'Cookies', 'Ice Cream', 'Pastries', 'Pies', 'Donuts']
sales_percentage = [30, 20, 15, 10, 10, 15]

# Colors for each dessert type
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Explode the first segment (Cakes) for emphasis
explode = (0.1, 0, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(sales_percentage, labels=desserts, autopct='%1.1f%%', startangle=180,
                                  colors=colors, explode=explode, textprops=dict(color="black", fontsize=12))

# Altering the percentage text style inside the pie chart
plt.setp(autotexts, size=11, weight="medium")

# Set the title with a different style
ax.set_title("Dessert Sales Distribution at Sweet Festival 2023", fontsize=14, fontweight='medium')

# Add a legend with altered placement and title style
ax.legend(wedges, desserts, title="Festive Desserts", loc="upper right", bbox_to_anchor=(1.1, 1), fontsize=9)

# Alter the axis property for visual flair
ax.get_yaxis().set_visible(False)

# Add gridlines for segment distinction
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

# Adjust layout
plt.tight_layout()

plt.show()