import matplotlib.pyplot as plt
import numpy as np

fruit_categories = ['Citrus', 'Berries', 'Tropical', 'Pomes', 'Drupes', 'Melons']
fruit_popularity = [35, 25, 20, 10, 5, 5]
sales_growth = [3, 4, 2, 1, 5, 2]

# Shuffled colors
colors = ['#FFD700', '#00CED1', '#DDA0DD', '#C71585', '#FFA07A', '#98FB98']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

wedges, texts, autotexts = ax1.pie(fruit_popularity, labels=fruit_categories, autopct='%1.1f%%',
                                   startangle=140, colors=colors, pctdistance=0.85,
                                   wedgeprops=dict(edgecolor='white'), shadow=True)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

for text in texts:
    text.set_fontsize(10)
    text.set_fontweight('normal')

ax1.set_title("2023 Farmer's Market Fruit Sales Distribution", fontsize=14, fontweight='bold')

ax1.legend(wedges, fruit_categories, title="Fruit Categories", loc='center left', bbox_to_anchor=(1, 0.5), 
           fontsize=10, title_fontsize=12)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax1.add_artist(centre_circle)

bars = ax2.bar(fruit_categories, sales_growth, color=colors, edgecolor='black')

for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{height}%', ha='center', va='bottom', fontsize=10)

ax2.set_title("Year-over-Year Sales Growth", fontsize=14, fontweight='bold')
ax2.set_ylabel("Growth Percentage", fontsize=12)
ax2.set_ylim(0, max(sales_growth) + 2)

plt.tight_layout()
plt.show()