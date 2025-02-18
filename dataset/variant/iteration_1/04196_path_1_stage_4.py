import matplotlib.pyplot as plt

fruits = ['Red Apple', 'Yellow Banana', 'Berry', 'Citrus', 'Vine Fruit']
preferences = [25, 20, 15, 18, 10]

colors = ['#ff6666', '#ffcc66', '#66ff66', '#ff66b3', '#66ccff']

fig, ax = plt.subplots(figsize=(10, 10))
ax.barh(fruits, preferences, color=colors, edgecolor='black')

ax.set_title("Kids' Beloved Fruits: Imaginary Class", fontsize=16, y=1.05)
ax.set_xlabel("Child Count")
ax.set_ylabel("Fruit Types")

plt.tight_layout()
plt.show()