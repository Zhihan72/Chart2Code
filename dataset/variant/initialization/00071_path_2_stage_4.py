import matplotlib.pyplot as plt

# Data Preparation
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Science Fiction', 'Romance', 'Historical Fiction', 'Fantasy']
overall_preference = [30, 20, 15, 10, 10, 10, 5]

# Predefined colors for each genre
genre_colors = ['#4682B4', '#8B008B', '#FF1493', '#32CD32', '#FF8C00', '#FFD700', '#FF6347']

# Plotting the base pie chart without stylistic elements
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(overall_preference, labels=genres, colors=genre_colors, startangle=140, autopct='%1.1f%%')

# Show the plot
plt.show()