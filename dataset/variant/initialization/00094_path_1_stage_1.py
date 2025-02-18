import matplotlib.pyplot as plt

# Data for the fleet composition
ship_types = ['Exploration', 'Defense', 'Cargo', 'Scientific', 'Diplomatic']
percentages = [25, 35, 15, 10, 15]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Base pie chart
wedges, texts, autotexts = ax.pie(percentages, autopct='%1.1f%%', startangle=140, colors=colors, labels=ship_types)

# Set the title of the chart
ax.set_title("Galactic Federation Fleet Composition\nShip Types and Capabilities", fontsize=14, fontweight='bold')

# Improve aesthetics of the texts
plt.setp(autotexts, size=10, weight="bold", color="black")
plt.setp(texts, size=9)

# Custom legend
ax.legend(wedges, ship_types, title="Ship Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust layout to fit everything without overlap
plt.tight_layout()

# Display the plot
plt.show()