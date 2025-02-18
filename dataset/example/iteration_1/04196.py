import matplotlib.pyplot as plt

# Title and backstory: "Favorite Fruit Preferences in a Hypothetical Classroom"
# Imagine surveying a classroom of children about their favorite fruits.

# Data for pie chart segment
fruits = ['Apple', 'Banana', 'Strawberry', 'Orange', 'Grape', 'Mango']
preferences = [25, 20, 15, 18, 10, 12]

# Colors to be used for each segment
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    preferences, 
    labels=fruits, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors, 
    pctdistance=0.85, 
    wedgeprops=dict(width=0.4),
    explode=[0, 0.1, 0, 0, 0.1, 0] # Highlight Banana and Grape
)

# Equal aspect ratio ensures the pie is drawn as a circle
ax.axis('equal')

# Customizing labels and autotexts
plt.setp(texts, size=12, weight="bold", va="center")
plt.setp(autotexts, size=12, weight="bold", color="black")

# Title & styling
plt.title("Favorite Fruit Preferences in a Hypothetical Classroom", fontsize=16, y=1.05)

# Draw an inner circle to create a donut chart
centre_circle = plt.Circle((0, 0), 0.60, fc='white')
fig.gca().add_artist(centre_circle)

# Draw an extra subplot for bar chart representation
ax1 = fig.add_axes([0.2, 0.2, 0.6, 0.3])
ax1.bar(fruits, preferences, color=colors, edgecolor='black')

# Additional labels and customization for bar chart
ax1.set_title("Fruit Preferences in Numbers", fontsize=14)
ax1.set_ylabel("Number of Children")
ax1.set_xlabel("Fruits")
ax1.grid(False)  # Turn off grid lines to avoid clutter

# Ensure pie chart is circular
ax.axis('equal')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the entire plot
plt.show()