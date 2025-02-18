import matplotlib.pyplot as plt

product_lines = ['Phones', 'Laptops', 'Wearable', 'Home Auto', 'Cloud', 'Gaming', 'VR Sets']
revenue_percentages = [40, 20, 15, 8, 5, 7, 5]

colors = ['#FF4500', '#1E90FF', '#228B22', '#FF1493', '#9ACD32', '#00CED1', '#8A2BE2']
explode = (0.1, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))

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

plt.title('Revenue of TechnoCorp in 2023', fontsize=14, fontweight='bold')

ax.axis('equal')

plt.show()