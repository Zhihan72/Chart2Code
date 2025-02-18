import matplotlib.pyplot as plt
import numpy as np

# Data
fruit_types = ['Blueberries', 'Mangoes', 'Strawberries', 'Kiwi', 'Peaches']
percentages = [20, 30, 25, 15, 10]
colors = ['#4B0082', '#FFA500', '#FF6347', '#9ACD32', '#FFD700']

# Subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Pie Chart
explode = (0.1, 0.15, 0, 0.05, 0)  
wedges, texts, autotexts = ax1.pie(
    percentages, labels=fruit_types, autopct='%1.1f%%', startangle=140, 
    colors=colors, explode=explode, shadow=True, textprops=dict(color="w"))

plt.setp(texts, size=12, weight="bold")
plt.setp(autotexts, size=12, weight="bold")
ax1.set_title('Fruit Distribution', fontsize=16, fontweight='bold', pad=20)

ax1.axis('equal')
ax1.legend(wedges, fruit_types, title="Fruits", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)

# Horizontal Bar Chart
bars = ax2.barh(fruit_types, percentages, color=colors, edgecolor='black')
ax2.set_title('Fruit Analysis', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel("Preference (%)", fontsize=12)
ax2.set_xlim(0, 35)
ax2.set_yticks(range(len(fruit_types)))
ax2.set_yticklabels(fruit_types, fontsize=10)
ax2.xaxis.grid(True, linestyle='--', alpha=0.7)

# Bar labels
for bar, percentage in zip(bars, percentages):
    ax2.text(bar.get_width() - 2.5, bar.get_y() + bar.get_height() / 2, f'{percentage}%', 
             va='center', ha='left', color='black', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()