import matplotlib.pyplot as plt

# Data for the pie chart
flavors = ['Chocolate', 'Vanilla', 'Strawberry', 'Mint Chocolate', 'Cookie Dough']
popularity = [25, 20, 15, 10, 10]  # Proportions sum to 80%

# New set of colors for each flavor
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFB6C1']

# Explode the 'Chocolate' and 'Vanilla' slices for emphasis
explode = (0.1, 0.1, 0, 0, 0)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Plot pie chart
wedges, texts, autotexts = ax.pie(
    popularity, 
    labels=flavors, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors, 
    explode=explode,
    shadow=True,
    textprops=dict(color="black"),
    wedgeprops=dict(edgecolor='w', linewidth=1.5)
)

# Customizing text inside the wedges
plt.setp(autotexts, size=10, weight="bold")

# Title and legend setup
ax.set_title(
    "Ice Cream Flavor Preferences among Teenagers in Sweetvale", 
    fontsize=16, fontweight='bold', pad=20
)
ax.legend(
    wedges, flavors, title="Flavors", loc="center left", 
    bbox_to_anchor=(1, 0, 0.5, 1)
)

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()