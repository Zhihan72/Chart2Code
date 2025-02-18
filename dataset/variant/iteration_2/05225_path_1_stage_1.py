import matplotlib.pyplot as plt

# Data for the pie chart
ride_names = ['Dragon Coaster', 'Pirate Ship', 'Haunted Mansion', 'Safari Adventure', 'Water Rapids']
visitor_percentage = [25, 20, 15, 30, 10]
colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231']

# Setup the figure
fig, ax = plt.subplots(figsize=(10, 7))

# Create the pie chart
wedges, texts, autotexts = ax.pie(
    visitor_percentage,
    labels=ride_names,
    autopct='%1.0f%%',
    startangle=90,
    colors=colors,
    wedgeprops=dict(edgecolor='gray', linestyle='--'),
    explode=(0, 0.2, 0, 0.2, 0),
    shadow=False
)

# Improve text/annotation appearance
plt.setp(autotexts, size=10, weight="normal", color="black")
plt.setp(texts, size=11)

# Set main title
plt.title('AdventureLand Ride Popularity', fontsize=15, fontweight='normal', color='darkgreen', pad=20)

# Add a legend
ax.legend(
    wedges, 
    ride_names, 
    title="Ride Names", 
    loc="upper right", 
    bbox_to_anchor=(1, 1),
    fontsize=12,
    title_fontsize=13
)

# Aspect ratio for pie chart
ax.set_aspect('equal')

# Display the chart
plt.show()