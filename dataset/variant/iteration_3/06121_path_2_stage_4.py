import matplotlib.pyplot as plt

# Modified data to reflect random changes in textual elements
snack_types = ['Fruits', 'Candy', 'Chips', 'Others', 'Cookies', 'Chocolate']
preferences = [15, 15, 25, 10, 15, 20]

colors = ['#B22222', '#8B4513', '#FF6347', '#FFD700', '#4B0082', '#4682B4']
explode = (0, 0, 0.1, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    preferences,
    labels=snack_types,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    explode=explode,
    textprops=dict(color="white", fontsize=12, weight="bold"),
    wedgeprops=dict(edgecolor='black', linewidth=1, width=0.3)
)

# Altered title to reflect a different context
plt.title('Snacks Preference Among Youngsters\nRecent Analysis', fontsize=16, fontweight='bold', pad=20)
plt.axis('equal')
plt.tight_layout()
plt.show()