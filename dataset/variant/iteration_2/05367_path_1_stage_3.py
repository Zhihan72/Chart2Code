import matplotlib.pyplot as plt
import squarify

# Manually altered expenses
expenses = [300, 100, 200, 1200, 100, 500, 50, 150]
total_expenses = sum(expenses)
sizes = [expense / total_expenses * 100 for expense in expenses]

# Correspondingly shuffled colors manually
colors = ['#99ff99', '#c2c2f0', '#ffcc99', '#66b3ff', '#ff6666', '#ffb3e6', '#ff9999', '#c2f0c2']

plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, color=colors, alpha=0.8, edgecolor="white", linewidth=2)
plt.axis('off')
plt.show()