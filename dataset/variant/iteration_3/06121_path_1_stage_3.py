import matplotlib.pyplot as plt

snack_types = ['Chips', 'Chocolate', 'Fruits', 'Cookies', 'Candy', 'Others']
# Original preferences were [25, 20, 15, 15, 15, 10]
preferences = [20, 15, 25, 15, 10, 15]

colors = ['#FF4500', '#FF8C00', '#FFD700', '#ADFF2F', '#32CD32', '#00CED1']

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    preferences, 
    labels=snack_types, 
    autopct='%1.0f%%', 
    startangle=45,  
    colors=colors, 
    wedgeprops=dict(width=0.3, edgecolor='navy', linewidth=2, linestyle='--'),
    textprops=dict(color="black", fontsize=10, weight="semibold")
)

plt.title('Favorite Snack Types Among Students\nSurvey 2023', fontsize=18, fontstyle='italic', pad=30)
plt.legend(wedges, snack_types, title="Snacks", loc="upper right", fontsize=10)
plt.axis('equal')
plt.tight_layout()
plt.show()