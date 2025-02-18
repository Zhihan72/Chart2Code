import matplotlib.pyplot as plt

# Data for pie chart
fruits = ['Apple', 'Banana', 'Strawberry', 'Orange', 'Grape', 'Mango']
preferences = [25, 20, 15, 18, 10, 12]

# Manually shuffled colors
colors = ['#66b3ff', '#ffb3e6', '#c2c2f0', '#ff9999', '#ffcc99', '#99ff99']

fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    preferences,
    labels=fruits,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    pctdistance=0.85,
    wedgeprops=dict(width=0.4),
    explode=[0, 0.1, 0, 0, 0.1, 0]
)

ax.axis('equal')
plt.setp(texts, size=12, weight="bold", va="center")
plt.setp(autotexts, size=12, weight="bold", color="black")

plt.title("Fruit Preferences", fontsize=16, y=1.05)

# Create donut chart center
centre_circle = plt.Circle((0, 0), 0.60, fc='white')
fig.gca().add_artist(centre_circle)

# Subplot for bar chart
ax1 = fig.add_axes([0.2, 0.2, 0.6, 0.3])
ax1.bar(fruits, preferences, color=colors, edgecolor='black')

ax1.set_title("Preferences", fontsize=14)
ax1.set_ylabel("Count")
ax1.set_xlabel("Fruits")
ax1.grid(False)

plt.tight_layout()
plt.show()