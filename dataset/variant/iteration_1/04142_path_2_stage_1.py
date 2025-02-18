import matplotlib.pyplot as plt

# Updated data with additional product lines
product_lines = ['Smartphones', 'Laptops', 'Wearables', 'Home Automation', 'Cloud Services', 'Gaming Consoles', 'VR Headsets']
revenue_percentages = [40, 20, 15, 8, 5, 7, 5]  # Total still adds up to 100%

# Adding colors for the new product lines
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFA500', '#800080', '#FFD700', '#DC143C']

# Exploding the 'Smartphones' slice to highlight it
explode = (0.1, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    revenue_percentages,
    labels=product_lines,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    shadow=True,
    wedgeprops=dict(edgecolor='w')
)

plt.setp(autotexts, size=12, weight='bold', color='black')
plt.setp(texts, size=12)

plt.title('Revenue Breakdown of TechnoCorp in 2023 by Product Line', fontsize=14, fontweight='bold')

ax.legend(wedges, product_lines, title="Product Lines", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)

ax.axis('equal')

plt.tight_layout()

plt.show()