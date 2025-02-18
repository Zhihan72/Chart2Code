import matplotlib.pyplot as plt

# Define the genres and user distribution data
genres = ['Jazz', 'Country', 'Pop', 'Electronic', 'Hip-Hop', 'Reggae', 'Classical', 'Rock']
user_distribution = [30, 20, 15, 12, 8, 7, 5, 3]

# Define colors for each genre
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#e6e600', '#ff6666']

# Explode the 'Pop' genre slice for emphasis
explode = (0, 0, 0.1, 0, 0, 0, 0, 0)

# Create the donut chart
plt.figure(figsize=(10, 8))
plt.pie(user_distribution, explode=explode, labels=genres, autopct='%1.1f%%',
        colors=colors, startangle=140, shadow=True, wedgeprops=dict(edgecolor='w', width=0.3))

# Title
plt.title("Exploration of Melodic Preferences:\n2023 Music Analysis", fontsize=16, fontweight='bold', pad=20)

# Position the legend
plt.legend(genres, loc='center left', bbox_to_anchor=(1, 0.5), title="Trend Categories", title_fontsize='13')

# Ensure pie chart is circular
plt.axis('equal')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()