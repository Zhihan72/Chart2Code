import matplotlib.pyplot as plt

percentages = [30, 25, 15, 5]
colors = ['#f3e5ab', '#7b3f00', '#ff69b4', '#93c572']
explode = (0.1, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(
    percentages,
    startangle=140,
    colors=colors,
    explode=explode,
    shadow=True,
    wedgeprops=dict(width=0.3)
)

ax.axis('equal')
plt.show()