import matplotlib.pyplot as plt

# Data Preparation after removal of 'Science Fiction'
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Romance', 'Thriller', 'Fantasy']
overall_preference = [20, 15, 15, 10, 15, 15]

age_distribution = {
    'Fiction': [10, 20, 30, 30, 10],
    'Non-Fiction': [5, 15, 20, 35, 25],
    'Mystery': [3, 12, 25, 40, 20],
    'Romance': [5, 15, 25, 35, 20],
    'Thriller': [10, 20, 30, 30, 10],
    'Fantasy': [20, 15, 25, 25, 15],
}

# Colors for genres and age groups
genre_colors = ['#8B008B', '#FF8C00', '#4682B4', '#FF1493', '#B22222', '#20B2AA']
age_colors = ['#F4A460', '#00FA9A', '#6495ED', '#FFD700', '#D2691E']

# Plotting the multi-ring donut chart
fig, ax = plt.subplots(figsize=(12, 10))
ax.pie(
    overall_preference, 
    colors=genre_colors, 
    startangle=140, 
    wedgeprops=dict(width=0.3), 
    autopct='%1.1f%%', 
    pctdistance=0.85
)

# Draw the outer rings representing the age distribution
for i, genre in enumerate(genres):
    ax.pie(
        age_distribution[genre], 
        radius=0.7, 
        colors=age_colors, 
        startangle=140, 
        wedgeprops=dict(width=0.3)
    )

# Adding a circle in the middle to create a donut shape
centre_circle = plt.Circle((0, 0), 0.35, fc='white')
fig.gca().add_artist(centre_circle)

# Customizing text properties
for autotext in ax.texts:
    autotext.set_color('white')
    autotext.set_weight('bold')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()