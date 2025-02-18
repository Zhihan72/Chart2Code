import matplotlib.pyplot as plt

# Data for horizontal bar chart
fruits = ['Apple', 'Banana', 'Strawberry', 'Orange', 'Grape', 'Mango']
preferences = [25, 20, 15, 18, 10, 12]

# Manually shuffled colors
colors = ['#66b3ff', '#ffb3e6', '#c2c2f0', '#ff9999', '#ffcc99', '#99ff99']

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(fruits, preferences, color=colors)

# Customize plot
ax.set_xlabel("Count")
ax.set_ylabel("Fruits")
ax.invert_yaxis()

plt.tight_layout()
plt.show()