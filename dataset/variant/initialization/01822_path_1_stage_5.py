import matplotlib.pyplot as plt

transaction_categories = [
    'Online', 
    'Bills', 
    'P2P', 
    'Subs', 
    'Invest', 
    'ATM',
    'Shopping'
]

transaction_counts = [550, 300, 250, 200, 150, 100, 180]

colors = ['#D32F2F', '#1976D2', '#388E3C', '#FBC02D', '#8E24AA', '#5D4037', '#FFA000']

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(transaction_counts, labels=transaction_categories, 
                                  colors=colors, autopct='%1.1f%%', startangle=150,  # Changed angle
                                  pctdistance=0.8,  # Altered percentage distance
                                  wedgeprops=dict(width=0.35, edgecolor='grey'))  # Altered border color

ax.text(0, 0, 'Transact\nQ3 2023', horizontalalignment='center', 
        verticalalignment='center', fontsize=12, fontweight='light', color='blue')  # Changed text style

ax.legend(wedges, transaction_categories, title="Category", loc="upper right", 
          bbox_to_anchor=(1, 0.5), fontsize=9)  # Changed legend position

plt.setp(autotexts, size=11, weight='normal', color='black')  # Changed label style
plt.setp(texts, size=10)

plt.title("Transaction Type Distribution\nQ3 2023", fontsize=14, fontweight='bold', pad=15, color='darkblue')  # Changed title style
plt.grid(True, linestyle='--', linewidth=0.7, color='grey')  # Added grid
plt.tight_layout()
plt.show()