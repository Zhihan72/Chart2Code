import matplotlib.pyplot as plt

# Data Preparation
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Science Fiction', 'Romance', 'Historical Fiction', 'Fantasy']
overall_preference = [30, 20, 15, 10, 10, 10, 5]

# Predefined colors for each genre
genre_colors = ['#4682B4', '#8B008B', '#FF1493', '#32CD32', '#FF8C00', '#FFD700', '#FF6347']

# Plotting the base pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(overall_preference, labels=genres, colors=genre_colors,
                                  startangle=140, autopct='%1.1f%%')

# Customizing text properties
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')

# Title
plt.title("General Reading Preferences by Genre with Additional Data", fontsize=14, weight='bold')

# Show the plot
plt.show()