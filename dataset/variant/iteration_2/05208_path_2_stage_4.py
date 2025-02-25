import matplotlib.pyplot as plt

percentages = [30, 25, 15, 10, 5]
colors = ['#f3e5ab', '#7b3f00', '#ff69b4', '#d2b48c', '#93c572']
explode = (0.05, 0.1, 0, 0, 0.1)

fig, ax = plt.subplots(figsize=(10, 8))

# Draw a donut pie chart by adjusting wedgeprops
wedges, _ = ax.pie(
    percentages, 
    startangle=90,
    colors=colors,
    explode=explode,
    wedgeprops=dict(width=0.3, edgecolor='w', lw=2)  # Adjusting width for the donut shape
)

ax.axis('equal')

plt.tight_layout()
plt.show()