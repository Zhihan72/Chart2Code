import matplotlib.pyplot as plt

transaction_categories = [
    'Peer-to-Peer Transfers', 
    'Investments', 
    'Subscription Payments', 
    'Online Purchases', 
    'Bill Payments'
]

transaction_counts = [550, 300, 250, 200, 100]

colors = ['#66B3FF', '#FFCC99', '#FF6F61', '#FF9999', '#99FF99']

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(aspect="equal"))

# Modified line styles and marker properties
wedges, texts, autotexts = ax.pie(transaction_counts, labels=transaction_categories, 
                                  colors=colors, autopct='%1.1f%%', startangle=45,  # Changed startangle
                                  wedgeprops=dict(width=0.3, edgecolor='k', linestyle='--'))  # Changed line style

# Center text adjusted with new color
ax.text(0, 0, 'Q3\nAnalysis', horizontalalignment='center', 
        verticalalignment='center', fontsize=14, fontweight='bold', color='darkblue')

# Adjusted legend properties and placement
ax.legend(wedges, transaction_categories, title="Transaction Categories", loc="upper right", 
          bbox_to_anchor=(1, 1), fontsize=9)  # Changed position

plt.setp(autotexts, size=9, weight='bold', color='yellow')  # Changed text color
plt.setp(texts, size=10)

plt.title("Fiscal Report: Q3\nBreakdown by Category", fontsize=15, fontweight='bold', pad=15)  # Adjusted title font size

# Added grid for visual enhancement
plt.grid(True)

plt.tight_layout()
plt.show()