import matplotlib.pyplot as plt
import numpy as np

categories = ['Tech Gadgets', 'Apparel', 'Home Essentials', 'Outdoor Gear', 'Kids Play']
sales_q1 = np.array([150, 200, 130, 120, 90])
sales_q2 = np.array([180, 210, 140, 130, 100])

total_sales = sales_q1 + sales_q2
sorted_indices = np.argsort(-total_sales)
categories = [categories[i] for i in sorted_indices]
sales_q1 = sales_q1[sorted_indices]
sales_q2 = sales_q2[sorted_indices]

fig, ax = plt.subplots(figsize=(14, 8))
width = 0.35
x = np.arange(len(categories))

ax.bar(x - width/2, sales_q1, width, color='seagreen', edgecolor='black')
ax.bar(x + width/2, sales_q2, width, color='darkorange', edgecolor='black')

for bar in ax.patches:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 2, int(yval), ha='center', va='bottom')

ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=45, ha='right')

plt.show()