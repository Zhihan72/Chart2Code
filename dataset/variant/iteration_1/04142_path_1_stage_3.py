import matplotlib.pyplot as plt

# Data for the donut chart
products = ['Smartwatches', 'Desktops', 'VR Headsets', 'Smart Lighting', 'Cyber Security']
revenue_percentages = [45, 25, 15, 10, 5]

color = '#4682B4'
explode = (0.1, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    revenue_percentages,
    labels=products,
    autopct='%1.1f%%',
    startangle=150,
    colors=[color] * len(products),
    explode=explode,
    shadow=True,
    wedgeprops=dict(width=0.3, edgecolor='w')  # Adjusting width for donut shape
)

plt.setp(autotexts, size=12, weight='bold', color='black')
plt.setp(texts, size=12)

plt.title('Income Distribution of InnovateCorp in 2023 across Sections', fontsize=14, fontweight='bold')

ax.legend(wedges, products, title="Sales Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)

ax.axis('equal')

plt.tight_layout()
plt.show()