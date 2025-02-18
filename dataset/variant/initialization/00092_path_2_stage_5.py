import matplotlib.pyplot as plt

labels = ['Recycle', 'Compost', 'Energy', 'Water', 'Transport', 'Renewables', 'Waste']
percentages = [25, 20, 15, 10, 5, 15, 10]
# New set of colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFC733', '#A133FF', '#33FFC7']

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(
    percentages,
    colors=colors,
    startangle=90,
    labels=labels,
    autopct='%1.1f%%',
    explode=(0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05)
)

ax.axis('equal')

plt.show()