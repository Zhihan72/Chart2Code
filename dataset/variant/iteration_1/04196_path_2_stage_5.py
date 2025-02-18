import matplotlib.pyplot as plt

# Data for horizontal bar chart
fruits = ['Apple', 'Banana', 'Orange', 'Grape', 'Mango']
preferences = [25, 20, 18, 10, 12]

# Manually adjusted colors
colors = ['#66b3ff', '#ffb3e6', '#ff9999', '#ffcc99', '#99ff99']

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(fruits, preferences, color=colors)

# Customize plot
ax.set_xlabel("Count")
ax.set_ylabel("Fruits")
ax.invert_yaxis()

plt.tight_layout()
plt.show()