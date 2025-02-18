import matplotlib.pyplot as plt
import squarify

expenses = [1200, 300, 500, 150, 100, 50]

total_expenses = sum(expenses)
sizes = [expense / total_expenses * 100 for expense in expenses]

# New set of colors for each category
colors = ['#3498db', '#e74c3c', '#2ecc71', '#9b59b6', '#f1c40f', '#34495e']

plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, 
              color=colors, alpha=0.8, edgecolor="white", linewidth=2)

plt.axis('off')
plt.tight_layout()
plt.show()