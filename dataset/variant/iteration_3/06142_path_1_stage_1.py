import matplotlib.pyplot as plt

# Define the data
transport_modes = ["Bicycles", "Cars", "Walking", "Motorcycles", "Public Transport", "Others"]
percentages = [25, 20, 30, 10, 10, 5]

# Colors for the transport modes
colors = ['#ffcc99', '#66b3ff', '#99ff99', '#ff9999', '#c2c2f0', '#ffb3e6']

# Create pie chart
fig, ax = plt.subplots(figsize=(10, 7))

# Creating the pie chart
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=transport_modes,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors
)

# Ensure each label and percentage is properly displayed
for text in texts:
    text.set_size(10)

for autotext in autotexts:
    autotext.set_size(10)
    autotext.set_color('darkgrey')

# Add title
plt.title("Transportation Modes in the Village\nDistribution of Daily Commuting Options", fontsize=16, weight='bold', pad=20)

# Adding the legend with a title
ax.legend(wedges, transport_modes, title="Transport Modes", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the pie chart
plt.show()