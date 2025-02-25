import matplotlib.pyplot as plt

# Data
fruits = ["Apple", "Banana", "Orange", "Blueberry", "Strawberry", "Grapes", "Kiwi", "Watermelon",
          "Pineapple", "Mango", "Peach", "Papaya"]
vitamin_content = [6, 10, 70, 9, 32, 10, 92, 8, 45, 36, 10, 60]
avg_rating = [7.5, 8.0, 9.0, 8.5, 9.5, 7.0, 8.5, 7.0, 8.8, 9.2, 7.8, 8.9]

fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting a horizontal bar chart
bars = ax1.barh(fruits, vitamin_content, color="sandybrown", edgecolor='black', linewidth=0.8)

ax1.grid(True, linestyle='--', alpha=0.7)

# Plotting the line chart for average ratings with a new color
ax2 = ax1.twiny()
ax2.plot(avg_rating, fruits, color="crimson", marker='o', linestyle='-', linewidth=2.5, markersize=10)

ax2.tick_params(axis='x', labelcolor='crimson')

plt.tight_layout()
plt.show()