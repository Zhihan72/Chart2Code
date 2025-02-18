import matplotlib.pyplot as plt

budget_allocations = [30, 25, 20, 15, 10]
colors = ['#fa8072', '#4682b4', '#8a2be2', '#ffd700', '#32cd32']

plt.figure(figsize=(12, 6))
wedges, texts, autotexts = plt.pie(budget_allocations, 
                                   colors=colors, 
                                   autopct='%1.1f%%',
                                   startangle=140, 
                                   explode=(0, 0, 0.1, 0, 0.1),
                                   shadow=False,
                                   wedgeprops={'edgecolor': 'black', 'linestyle': 'dotted'})

for text in texts:
    text.set_fontsize(12)

for autotext in autotexts:
    autotext.set_color('blue')
    autotext.set_fontsize(12)

plt.legend(wedges, ['Marketing', 'R&D', 'Operations', 'Sales', 'IT'], loc="upper right")
plt.axis('equal')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()