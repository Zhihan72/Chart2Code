import matplotlib.pyplot as plt

# Define the data
snack_types = ['Chips', 'Chocolate', 'Fruits', 'Cookies', 'Candy', 'Others']
preferences = [25, 20, 15, 15, 15, 10]

# Define colors for each segment of the donut chart
colors = ['#FFD700', '#8B4513', '#FF6347', '#B22222', '#4B0082', '#4682B4']

# Define the explode parameter to highlight the 'Chips' slice
explode = (0.1, 0, 0, 0, 0, 0)

# Create the donut chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    preferences, 
    labels=snack_types, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors, 
    explode=explode, 
    shadow=True,
    textprops=dict(color="white", fontsize=12, weight="bold"),
    wedgeprops=dict(edgecolor='black', linewidth=1, width=0.3)
)

# Set the title
plt.title('Favorite Snack Types Among Students\n2023 Survey Results', fontsize=16, fontweight='bold', pad=20)

# Add a legend to provide insights
plt.legend(wedges, snack_types, title="Snack Types", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=12)

# Ensure the donut chart is a circle
plt.axis('equal')

# Automatically adjust layout for padding
plt.tight_layout()

# Display the plot
plt.show()