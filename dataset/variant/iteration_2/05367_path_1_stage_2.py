import matplotlib.pyplot as plt
import squarify

expenses = [1200, 300, 500, 150, 200, 100, 50, 100] 
total_expenses = sum(expenses)
sizes = [expense / total_expenses * 100 for expense in expenses]

# Manually shuffled colors
colors = ['#66b3ff', '#99ff99', '#ffb3e6', '#c2f0c2', '#ffcc99', '#c2c2f0', '#ff9999', '#ff6666']

plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, color=colors, alpha=0.8, edgecolor="white", linewidth=2)
plt.axis('off')
plt.show()