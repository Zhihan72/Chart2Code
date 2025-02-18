import matplotlib.pyplot as plt

# Data
fruits = ["Apple", "Banana", "Orange", "Blueberry", "Strawberry", "Grapes", "Kiwi", "Watermelon",
          "Pineapple", "Mango", "Peach", "Papaya"]
vitamin_content = [6, 10, 70, 9, 32, 10, 92, 8, 45, 36, 10, 60]  # Vitamin C content (in mg per 100g)
avg_rating = [7.5, 8.0, 9.0, 8.5, 9.5, 7.0, 8.5, 7.0, 8.8, 9.2, 7.8, 8.9]  # Average rating (out of 10)

fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting the bars for vitamin content
bars = ax1.bar(fruits, vitamin_content, color="limegreen", edgecolor='black', linewidth=0.8)

ax1.grid(True, linestyle='--', alpha=0.7)

# Plotting the line chart for average ratings
ax2 = ax1.twinx()
ax2.plot(fruits, avg_rating, color="blue", marker='o', linestyle='-', linewidth=2.5, markersize=10)

ax2.tick_params(axis='y', labelcolor='blue')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()