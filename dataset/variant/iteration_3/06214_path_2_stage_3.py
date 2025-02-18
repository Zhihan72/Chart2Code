import matplotlib.pyplot as plt
import numpy as np

fruit_categories = ['Citrus', 'Berries', 'Tropical', 'Pomes', 'Drupes', 'Melons']
fruit_popularity = [35, 25, 20, 10, 5, 5]
sales_growth = [3, 4, 2, 1, 5, 2]

# Updated colors
colors = ['#8A2BE2', '#5F9EA0', '#DAA520', '#CD5C5C', '#48D1CC', '#9ACD32']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

bars = ax1.bar(fruit_categories, sales_growth, color=colors, edgecolor='darkgrey', linestyle='--', linewidth=1.5)

for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{height}%', ha='center', va='bottom', fontsize=10)

ax1.set_title("Year-over-Year Sales Growth", fontsize=14, fontweight='bold')
ax1.set_ylabel("Growth Percentage", fontsize=12)
ax1.set_ylim(0, max(sales_growth) + 2)

ax1.grid(which='major', linestyle=':', linewidth=0.5)

wedges, texts, autotexts = ax2.pie(fruit_popularity, labels=fruit_categories, autopct='%1.1f%%',
                                   startangle=120, colors=colors,
                                   wedgeprops=dict(edgecolor='gray'), shadow=False)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(9)
    autotext.set_fontweight('normal')

for text in texts:
    text.set_fontsize(9)
    text.set_fontweight('normal')

ax2.set_title("2023 Farmer's Market Fruit Sales Distribution", fontsize=14, fontweight='bold')

ax2.legend(wedges, fruit_categories, title="Categories", loc='upper right', fontsize=9, title_fontsize=11)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax2.add_artist(centre_circle)

plt.tight_layout()
plt.show()