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

# Single color used for all segments
single_color = ['#4682B4']

# Plotting the multi-ring donut chart
fig, ax = plt.subplots(figsize=(12, 10))
ax.pie(
    overall_preference, 
    colors=single_color * len(genres),  # Apply single color to all
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
        colors=single_color * len(age_distribution[genre]),  # Apply single color to all
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