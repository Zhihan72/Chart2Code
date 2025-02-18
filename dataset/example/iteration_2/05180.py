import matplotlib.pyplot as plt

# Defining the backstory:
# Suppose we are analyzing the consumption patterns of different dessert types in a popular city's famous sweet festival. 
# The data represents the percentage share of each dessert type in the total dessert sales.

# Desserts and their percentage share
desserts = ['Cakes', 'Cookies', 'Ice Cream', 'Pastries', 'Pies', 'Donuts']
sales_percentage = [30, 20, 15, 10, 10, 15]  # Summed up to 100%

# Colors for each dessert type
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Explode the largest segment (Cakes) for emphasis
explode = (0.1, 0, 0, 0, 0, 0)  # Explode Cakes segment

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(sales_percentage, labels=desserts, autopct='%1.1f%%', startangle=140,
                                  colors=colors, explode=explode, textprops=dict(color="black", fontsize=12))

# Customizing the percentage text inside the pie chart
plt.setp(autotexts, size=10, weight="bold")

# Set the title
ax.set_title("Sweet Festival: Dessert Sales Distribution 2023", fontsize=16, fontweight='bold')

# Add a legend
ax.legend(wedges, desserts, title="Desserts", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Maintain equal aspect ratio to ensure pie is drawn as a circle.
ax.axis('equal')

# Adjust layout to avoid text and chart overlap
plt.tight_layout()

# Show the plot
plt.show()