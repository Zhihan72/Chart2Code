import matplotlib.pyplot as plt

# Updated data segment labels for the pie chart
fruits = ['Red Apple', 'Yellow Banana', 'Berry', 'Citrus', 'Vine Fruit']
preferences = [25, 20, 15, 18, 10]

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    preferences,
    labels=fruits,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    pctdistance=0.85,
    wedgeprops=dict(width=0.4),
    explode=[0, 0.1, 0, 0, 0.1]
)

ax.axis('equal')
plt.setp(texts, size=12, weight="bold", va="center")
plt.setp(autotexts, size=12, weight="bold", color="black")

plt.title("Kids' Beloved Fruits: Imaginary Class", fontsize=16, y=1.05)

centre_circle = plt.Circle((0, 0), 0.60, fc='white')
fig.gca().add_artist(centre_circle)

ax1 = fig.add_axes([0.2, 0.2, 0.6, 0.3])
ax1.bar(fruits, preferences, color=colors, edgecolor='black')

ax1.set_title("Fruit Count Surprise", fontsize=14)
ax1.set_ylabel("Child Count")
ax1.set_xlabel("Fruit Types")
ax1.grid(False)

ax.axis('equal')
plt.tight_layout()
plt.show()