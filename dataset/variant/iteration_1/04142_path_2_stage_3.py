import matplotlib.pyplot as plt

product_lines = ['Smartphones', 'Laptops', 'Wearables', 'Home Automation', 'Cloud Services', 'Gaming Consoles', 'VR Headsets']
revenue_percentages = [40, 20, 15, 8, 5, 7, 5]

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFA500', '#800080', '#FFD700', '#DC143C']
explode = (0.1, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))

# Creating a donut pie chart with an inner circle
wedges, texts, autotexts = ax.pie(
    revenue_percentages,
    labels=product_lines,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    wedgeprops=dict(edgecolor='w', width=0.4)
)

plt.setp(autotexts, size=12, weight='bold', color='black')
plt.setp(texts, size=12)

plt.title('Revenue Breakdown of TechnoCorp in 2023 by Product Line', fontsize=14, fontweight='bold')

ax.axis('equal')

plt.show()