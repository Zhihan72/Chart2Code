import matplotlib.pyplot as plt

activities = [
    "Holo-gaming", 
    "Virtual Tourism", 
    "Zero-G Sports", 
    "Nebula Painting", 
    "Stargazing"
]
popularity_percentages = [25, 15, 18, 10, 12]

# Colors for each activity
colors = ['#ff9999', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Exploring the distribution of leisure activities
fig, ax1 = plt.subplots(figsize=(10, 7))

# Update explode to match the new activity list
explode = [0.1, 0, 0, 0, 0]

ax1.pie(popularity_percentages, labels=activities, autopct='%1.1f%%', startangle=140, colors=colors,
        explode=explode, shadow=True, wedgeprops=dict(edgecolor='black'))

ax1.set_title("Recreational Preferences in the Galactic Federation", fontsize=16, fontweight='bold', pad=20)

# Create a legend
plt.legend(activities, title="Leisure Activities", loc="upper right", bbox_to_anchor=(1.2, 1), frameon=False)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()