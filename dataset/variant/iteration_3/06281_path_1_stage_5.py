import matplotlib.pyplot as plt

fruit_types = ['Berries', 'Mango', 'Straw', 'Kiwi', 'Peach']
percentages = [15, 25, 30, 10, 20]
colors = ['#FFA500', '#FF6347', '#FFD700', '#9ACD32', '#4B0082']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

ax2.pie(
    percentages, labels=fruit_types, autopct='%1.1f%%', startangle=140, 
    colors=colors, explode=(0.1, 0.15, 0, 0.05, 0))

ax2.set_title('Fruit Distribution', fontsize=16, fontweight='bold', pad=20)
ax2.axis('equal')

ax1.barh(fruit_types, percentages, color=colors)
ax1.set_title('Fruit Analysis', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Preference %", fontsize=12)
ax1.set_xlim(0, 35)
ax1.set_yticks(range(len(fruit_types)))
ax1.set_yticklabels(fruit_types, fontsize=10)

plt.tight_layout()
plt.show()