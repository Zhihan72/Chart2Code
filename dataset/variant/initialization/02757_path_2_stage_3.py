import matplotlib.pyplot as plt

budget_allocations = [30, 25, 20, 15, 10]

colors = ['#fa8072', '#4682b4', '#8a2be2', '#ffd700', '#32cd32']

plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(budget_allocations, 
                                   colors=colors, 
                                   autopct='%1.1f%%',
                                   startangle=90, 
                                   explode=(0.05, 0, 0, 0, 0),
                                   shadow=True)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)

plt.axis('equal')
plt.tight_layout()
plt.show()