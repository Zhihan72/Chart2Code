import matplotlib.pyplot as plt

fruit_categories = ['Citrus', 'Berries', 'Tropical', 'Pomes', 'Drupes', 'Melons', 'Stone fruits']
fruit_popularity = [35, 25, 20, 10, 5, 5, 15]
sales_growth = [3, 4, 2, 1, 5, 2, 3]

colors = ['#8A2BE2', '#5F9EA0', '#DAA520', '#CD5C5C', '#48D1CC', '#9ACD32', '#FF69B4']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Bar chart without textual annotations
ax1.bar(fruit_categories, sales_growth, color=colors, edgecolor='darkgrey', linestyle='--', linewidth=1.5)
ax1.set_ylim(0, max(sales_growth) + 2)
ax1.grid(which='major', linestyle=':', linewidth=0.5)

# Pie chart without textual annotations
ax2.pie(fruit_popularity, startangle=120, colors=colors,
        wedgeprops=dict(edgecolor='gray'), shadow=False)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax2.add_artist(centre_circle)

plt.tight_layout()
plt.show()