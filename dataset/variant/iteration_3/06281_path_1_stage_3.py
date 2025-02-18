import matplotlib.pyplot as plt

# Same fruit types, shuffled percentages
fruit_types = ['Blueberries', 'Mangoes', 'Strawberries', 'Kiwi', 'Peaches']
percentages = [15, 25, 30, 10, 20]  # Manually adjusted values for randomness
colors = ['#FFA500', '#FF6347', '#FFD700', '#9ACD32', '#4B0082']  # Same colors

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

explode = (0.1, 0.15, 0, 0.05, 0)  # Same explode effect
ax1.pie(
    percentages, labels=fruit_types, autopct='%1.1f%%', startangle=140, 
    colors=colors, explode=explode)

ax1.set_title('Distribution of Favorite Fruits\namong Elves in Fruit Paradise', 
              fontsize=16, fontweight='bold', pad=20)
ax1.axis('equal')

ax2.barh(fruit_types, percentages, color=colors)
ax2.set_title('Favorite Fruits Detailed Analysis', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel("Percentage of Preference", fontsize=12)
ax2.set_xlim(0, 35)
ax2.set_yticks(range(len(fruit_types)))
ax2.set_yticklabels(fruit_types, fontsize=10)

plt.tight_layout()
plt.show()