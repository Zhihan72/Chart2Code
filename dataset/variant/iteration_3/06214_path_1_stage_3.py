import matplotlib.pyplot as plt
import numpy as np

# Data definitions
fruit_categories = ['Citrus', 'Berries', 'Tropical', 'Pomes', 'Drupes', 'Melons']
fruit_popularity = [35, 25, 20, 10, 5, 5]
sales_growth = [3, 4, 2, 1, 5, 2]
new_colors = ['#FF6347', '#4682B4', '#8A2BE2', '#32CD32', '#FFD700', '#8B4513']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

bars = ax1.barh(fruit_categories, sales_growth, color=new_colors, edgecolor='black')
for bar in bars:
    width = bar.get_width()
    ax1.text(width, bar.get_y() + bar.get_height() / 2, f'{width}%', va='center', ha='left', fontsize=10)

ax1.set_title("Year-over-Year Sales Growth", fontsize=14, fontweight='bold')
ax1.set_xlabel("Growth Percentage", fontsize=12)
ax1.set_xlim(0, max(sales_growth) + 2)

wedges, texts, autotexts = ax2.pie(fruit_popularity, labels=fruit_categories, autopct='%1.1f%%',
                                    startangle=140, colors=new_colors, pctdistance=0.85,
                                    wedgeprops=dict(edgecolor='white'), shadow=True)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

for text in texts:
    text.set_fontsize(10)
    text.set_fontweight('normal')

ax2.set_title("2023 Farmer's Market Fruit Sales Distribution", fontsize=14, fontweight='bold')
ax2.legend(wedges, fruit_categories, title="Fruit Categories", loc='center left', bbox_to_anchor=(1, 0.5),
           fontsize=10, title_fontsize=12)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax2.add_artist(centre_circle)

plt.tight_layout() 
plt.show()