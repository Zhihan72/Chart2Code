import matplotlib.pyplot as plt

# Data
popularity = [45, 30, 5, 7]
colors = ['#66b3ff', '#ff9999', '#ffb3e6', '#c2c2f0']
explode = (0.05, 0.05, 0, 0)

# Plotting
fig, ax = plt.subplots(figsize=(10, 10))
ax.pie(popularity, explode=explode, colors=colors, startangle=140, wedgeprops=dict(width=0.3))

# Show plot
plt.show()