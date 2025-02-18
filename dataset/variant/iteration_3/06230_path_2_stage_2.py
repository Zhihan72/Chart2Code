import matplotlib.pyplot as plt

flavors = ['Apple', 'Banana', 'Strawberry', 'Pineapple', 'Orange', 'Grapes']
preferences = [300, 200, 150, 100, 150, 100]

colors = ['#FF9999', '#FFD700', '#FF69B4', '#FFDAB9', '#FFA500', '#9ACD32']

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    preferences, labels=flavors, colors=colors, autopct='%1.1f%%', 
    startangle=90, textprops={'fontsize': 10, 'color': 'purple'}
)

ax.set_title('Fruit Flavors Survey\nAmong Locals', fontsize=16, fontweight='bold', pad=15)

ax.legend(wedges, flavors, title="Flavors", loc="upper right", bbox_to_anchor=(0.9, 0.9))

plt.tight_layout()
plt.show()