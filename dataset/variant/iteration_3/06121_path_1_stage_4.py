import matplotlib.pyplot as plt

snack_types = ['Chips', 'Chocolate', 'Fruits', 'Cookies', 'Candy', 'Others']
preferences = [20, 15, 25, 15, 10, 15]

# Updated colors to offer a new set
new_colors = ['#8A2BE2', '#5F9EA0', '#7FFF00', '#FF7F50', '#6495ED', '#DC143C']

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    preferences, 
    labels=snack_types, 
    autopct='%1.0f%%', 
    startangle=45,  
    colors=new_colors, 
    wedgeprops=dict(width=0.3, edgecolor='navy', linewidth=2, linestyle='--'),
    textprops=dict(color="black", fontsize=10, weight="semibold")
)

plt.title('Favorite Snack Types Among Students\nSurvey 2023', fontsize=18, fontstyle='italic', pad=30)
plt.legend(wedges, snack_types, title="Snacks", loc="upper right", fontsize=10)
plt.axis('equal')
plt.tight_layout()
plt.show()