import matplotlib.pyplot as plt

# Data
popularity = [45, 30, 5, 7, 6, 4, 3]
colors = ['#66b3ff', '#ff9999', '#ffb3e6', '#c2c2f0', '#99ff99', '#ff6666', '#ffcc99']
explode = (0.05, 0.05, 0, 0, 0, 0, 0)

# Plotting
fig, ax = plt.subplots(figsize=(10, 10))
ax.pie(popularity, explode=explode, colors=colors, startangle=140)

# Show plot
plt.show()