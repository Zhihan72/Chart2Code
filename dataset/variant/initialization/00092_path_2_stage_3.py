import matplotlib.pyplot as plt

labels = ['Recycle', 'Compost', 'Energy', 'Water', 'Transport']
percentages = [30, 25, 20, 15, 10]
colors = ['#76C7C0', '#FFD700', '#FF6F61', '#6B8E23', '#4682B4']

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(
    percentages,
    colors=colors,
    startangle=90,
    labels=labels,
    autopct='%1.1f%%',
    explode=(0.05, 0.05, 0.05, 0.05, 0.05)
)

ax.axis('equal')

plt.show()