import matplotlib.pyplot as plt
import numpy as np

# Transaction categories and their respective count of transactions
transaction_categories = [
    'Peer-to-Peer Transfers', 
    'Investments', 
    'Subscription Payments', 
    'Online Purchases', 
    'Bill Payments'
]

# Artificial data representing the number of transactions for each category
transaction_counts = [550, 300, 250, 200, 100]

# Define colors for each transaction category
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF6F61']

# Create the ring chart
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(aspect="equal"))

# Plot the pie chart with an inner radius for a ring effect
wedges, texts, autotexts = ax.pie(transaction_counts, labels=transaction_categories, 
                                  colors=colors, autopct='%1.1f%%', startangle=90,
                                  pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w'))

# Add a central title inside the ring
ax.text(0, 0, 'Q3\nFinancials\nAnalysis', horizontalalignment='center', 
        verticalalignment='center', fontsize=14, fontweight='bold', color='gray')

# Customize legend and position it outside the chart
ax.legend(wedges, transaction_categories, title="Categories of Transactions", loc="center left", 
          bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Enhance the label text properties
plt.setp(autotexts, size=10, weight='bold', color='white')
plt.setp(texts, size=11)

# Title of the chart
plt.title("Q3 Fiscal Year Report\nCategory Breakdown", fontsize=16, fontweight='bold', pad=20)

# Ensure layout is tight
plt.tight_layout()

# Show the chart
plt.show()