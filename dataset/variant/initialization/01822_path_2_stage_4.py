import matplotlib.pyplot as plt

transaction_categories = [
    'Peer-to-Peer Transfers', 
    'Investments', 
    'Subscription Payments', 
    'Online Purchases', 
    'Bill Payments'
]

transaction_counts = [550, 300, 250, 200, 100]

# Modified colors for each transaction category
colors = ['#66B3FF', '#FFCC99', '#FF6F61', '#FF9999', '#99FF99']

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(aspect="equal"))

# Creating a donut chart by setting the width of the wedges
wedges, texts, autotexts = ax.pie(transaction_counts, labels=transaction_categories, 
                                  colors=colors, autopct='%1.1f%%', startangle=90,
                                  wedgeprops=dict(width=0.4, edgecolor='w'))

# Center text for the donut chart
ax.text(0, 0, 'Q3\nFinancials\nAnalysis', horizontalalignment='center', 
        verticalalignment='center', fontsize=14, fontweight='bold', color='gray')

ax.legend(wedges, transaction_categories, title="Categories of Transactions", loc="center left", 
          bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

plt.setp(autotexts, size=10, weight='bold', color='white')
plt.setp(texts, size=11)

plt.title("Q3 Fiscal Year Report\nCategory Breakdown", fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()