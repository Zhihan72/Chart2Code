import matplotlib.pyplot as plt
import numpy as np

# Data definitions
fruit_categories = ['Melons', 'Berries', 'Pomes', 'Citrus', 'Tropical', 'Drupes']
fruit_popularity = [5, 25, 10, 35, 20, 5]
sales_growth = [2, 4, 1, 3, 2, 5]
new_colors = ['#8B4513', '#4682B4', '#32CD32', '#FF6347', '#8A2BE2', '#FFD700']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

bars = ax1.barh(fruit_categories, sales_growth, color=new_colors, edgecolor='black', linestyle='dashed', hatch='/')
for bar in bars:
    width = bar.get_width()
    ax1.text(width, bar.get_y() + bar.get_height() / 2, f'growth: {width}%', va='center', ha='left', fontsize=10)

ax1.set_title("Annual Fruit Sales Increase", fontsize=14, fontweight='bold', style='italic')
ax1.set_xlabel("Percentage Increase", fontsize=12, style='oblique')
ax1.grid(True, linestyle='--', linewidth=0.5)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

wedges, texts, autotexts = ax2.pie(fruit_popularity, labels=fruit_categories, autopct='%1.1f%%',
                                    startangle=140, colors=new_colors, pctdistance=0.85,
                                    wedgeprops=dict(edgecolor='gray', linestyle='-'), shadow=False)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(12)
    autotext.set_fontweight('normal')

for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('light')

ax2.set_title("Fruit Sales Share at Market 2023", fontsize=14, fontweight='bold', style='italic')
ax2.legend(wedges, fruit_categories, title="Types of Fruits", loc='lower right', bbox_to_anchor=(1, 0),
           fontsize=9, title_fontsize=11, frameon=False)

centre_circle = plt.Circle((0, 0), 0.70, fc='lightgray')
ax2.add_artist(centre_circle)

plt.tight_layout() 
plt.show()