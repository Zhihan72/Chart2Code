import matplotlib.pyplot as plt

transaction_categories = [
    'Online', 
    'Bills', 
    'P2P', 
    'Subs', 
    'Invest', 
    'ATM'
]

transaction_counts = [550, 300, 250, 200, 150, 100]

# New set of colors for each transaction category
colors = ['#D32F2F', '#1976D2', '#388E3C', '#FBC02D', '#8E24AA', '#5D4037']

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(transaction_counts, labels=transaction_categories, 
                                  colors=colors, autopct='%1.1f%%', startangle=90,
                                  pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w'))

ax.text(0, 0, 'Transact\nQ3', horizontalalignment='center', 
        verticalalignment='center', fontsize=14, fontweight='bold', color='gray')

ax.legend(wedges, transaction_categories, title="Types", loc="center left", 
          bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

plt.setp(autotexts, size=10, weight='bold', color='white')
plt.setp(texts, size=11)

plt.title("Transaction Distribution\nQ3", fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()