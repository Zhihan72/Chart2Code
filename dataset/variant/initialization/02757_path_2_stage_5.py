import matplotlib.pyplot as plt

# Shuffled budget allocations, labels, and colors
budget_allocations = [15, 30, 10, 20, 25]
colors = ['#ffd700', '#fa8072', '#32cd32', '#8a2be2', '#4682b4']
labels = ['Sales', 'Marketing', 'IT', 'Operations', 'R&D']

plt.figure(figsize=(12, 6))
wedges, texts, autotexts = plt.pie(budget_allocations, 
                                   colors=colors, 
                                   autopct='%1.1f%%',
                                   startangle=140, 
                                   explode=(0, 0.1, 0.1, 0, 0),
                                   shadow=False,
                                   wedgeprops={'edgecolor': 'black', 'linestyle': 'dotted'})

for text in texts:
    text.set_fontsize(12)

for autotext in autotexts:
    autotext.set_color('blue')
    autotext.set_fontsize(12)

plt.legend(wedges, labels, loc="upper right")
plt.axis('equal')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()