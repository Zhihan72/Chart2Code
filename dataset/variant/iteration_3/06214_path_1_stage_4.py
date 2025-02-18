import matplotlib.pyplot as plt
import numpy as np

# Data definitions
fruit_categories = ['Melons', 'Berries', 'Pomes', 'Citrus', 'Tropical', 'Drupes']
fruit_popularity = [5, 25, 10, 35, 20, 5]
sales_growth = [2, 4, 1, 3, 2, 5]
new_colors = ['#8B4513', '#4682B4', '#32CD32', '#FF6347', '#8A2BE2', '#FFD700']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

bars = ax1.barh(fruit_categories, sales_growth, color=new_colors, edgecolor='black')
for bar in bars:
    width = bar.get_width()
    ax1.text(width, bar.get_y() + bar.get_height() / 2, f'growth: {width}%', va='center', ha='left', fontsize=10)

ax1.set_title("Annual Fruit Sales Increase", fontsize=14, fontweight='bold')
ax1.set_xlabel("Percentage Increase", fontsize=12)
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

ax2.set_title("Fruit Sales Share at Market 2023", fontsize=14, fontweight='bold')
ax2.legend(wedges, fruit_categories, title="Types of Fruits", loc='center left', bbox_to_anchor=(1, 0.5),
           fontsize=10, title_fontsize=12)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax2.add_artist(centre_circle)

plt.tight_layout() 
plt.show()