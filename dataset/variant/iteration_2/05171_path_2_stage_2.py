import matplotlib.pyplot as plt

# Updated categories and their respective proportions
activities = [
    "Leisure & Entertainment", 
    "Work & Career", 
    "Health & Fitness", 
    "Education & Learning", 
    "Socializing", 
    "Travel & Exploration", 
    "Personal Development"
]

# Updated proportions of each category
activity_proportions = [20, 15, 10, 15, 12, 10, 10]

# Updated color scheme for each activity
colors = ['#4B0082', '#FF6347', '#4682B4', '#FFD700', '#ADFF2F', '#DEB887', '#40E0D0']

# Updated explode to emphasize Leisure and Health
explode = (0.1, 0, 0.1, 0, 0, 0, 0)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the pie chart
wedges, texts, autotexts = ax.pie(
    activity_proportions, labels=activities, colors=colors, explode=explode,
    autopct='%1.1f%%', startangle=90, pctdistance=0.85, shadow=True
)

plt.setp(texts, size=10, weight='bold', color='navy')
plt.setp(autotexts, size=10, color='white', weight='bold')

# Add a central circle for a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')
ax.set_title("Favorite Activities in Zeropolis, 2123", fontsize=16, fontweight='bold', pad=40)

# Add a legend positioned outside the chart
ax.legend(wedges, activities, title="Activities", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)

plt.tight_layout()
plt.show()