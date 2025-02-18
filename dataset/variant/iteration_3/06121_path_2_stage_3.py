import matplotlib.pyplot as plt

snack_types = ['Cookies', 'Chocolate', 'Fruits', 'Chips', 'Candy', 'Others']
preferences = [15, 20, 15, 25, 15, 10]

colors = ['#B22222', '#8B4513', '#FF6347', '#FFD700', '#4B0082', '#4682B4']
explode = (0, 0, 0, 0.1, 0, 0)

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

plt.title('Favorite Snack Types Among Students\n2023 Survey Results', fontsize=16, fontweight='bold', pad=20)
plt.axis('equal')
plt.tight_layout()
plt.show()