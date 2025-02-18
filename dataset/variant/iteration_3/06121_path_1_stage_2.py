import matplotlib.pyplot as plt

# Define the data
snack_types = ['Chips', 'Chocolate', 'Fruits', 'Cookies', 'Candy', 'Others']
preferences = [25, 20, 15, 15, 15, 10]

# Define colors for each segment of the pie chart
colors = ['#FF4500', '#FF8C00', '#FFD700', '#ADFF2F', '#32CD32', '#00CED1']

# Create the donut chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    preferences, 
    labels=snack_types, 
    autopct='%1.0f%%', 
    startangle=45,  
    colors=colors, 
    wedgeprops=dict(width=0.3, edgecolor='navy', linewidth=2, linestyle='--'),  # Added width for donut
    textprops=dict(color="black", fontsize=10, weight="semibold")
)

# Set the title
plt.title('Favorite Snack Types Among Students\nSurvey 2023', fontsize=18, fontstyle='italic', pad=30)

# Add a legend
plt.legend(wedges, snack_types, title="Snacks", loc="upper right", fontsize=10)

# Ensure the pie chart maintains its aspect ratio
plt.axis('equal') 

# Automatically adjust layout to ensure sufficient padding is maintained
plt.tight_layout()

# Display the plot
plt.show()