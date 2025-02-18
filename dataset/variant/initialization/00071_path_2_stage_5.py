import matplotlib.pyplot as plt

# Data Preparation
overall_preference = [30, 20, 15, 10, 10, 10, 5]

# Predefined colors for each genre
genre_colors = ['#4682B4', '#8B008B', '#FF1493', '#32CD32', '#FF8C00', '#FFD700', '#FF6347']

# Plotting the pie chart without textual elements
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(overall_preference, colors=genre_colors, startangle=140)

# Show the plot
plt.show()