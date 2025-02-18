import matplotlib.pyplot as plt

# Desserts and their percentage share
desserts = ['Cakes', 'Cookies', 'Ice Cream', 'Pies', 'Donuts']
sales_percentage = [30, 20, 15, 10, 15]

# Colors for each dessert type
colors = ['#ff9999', '#66b3ff', '#99ff99', '#c2c2f0', '#ffb3e6']

# Explode the first segment (Cakes) for emphasis
explode = (0.1, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(sales_percentage, labels=desserts, autopct='%1.1f%%', startangle=180,
                                  colors=colors, explode=explode, textprops=dict(color="black", fontsize=12))

plt.setp(autotexts, size=11, weight="medium")
ax.set_title("Dessert Sales Distribution at Sweet Festival 2023", fontsize=14, fontweight='medium')
ax.legend(wedges, desserts, title="Festive Desserts", loc="upper right", bbox_to_anchor=(1.1, 1), fontsize=9)
ax.get_yaxis().set_visible(False)
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
plt.tight_layout()
plt.show()