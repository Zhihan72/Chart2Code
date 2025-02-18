import matplotlib.pyplot as plt

# Data for the pie chart
handheld_gaming_consoles = ['Nintendo Switch', 'PlayStation Vita', 'Game Boy', 'PSP', 'Other']
market_share = [55, 15, 10, 15, 5]

# Define colors for each console
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create a pie chart
fig, ax = plt.subplots(figsize=(10, 10))

# Create wedges, labels, and percentages
wedges, texts, autotexts = ax.pie(
    market_share, 
    labels=handheld_gaming_consoles, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    pctdistance=0.85,
    explode=(0.1, 0, 0, 0.1, 0)  # Slightly explode Nintendo Switch and PSP for emphasis
)

# Add a circular center to create the "sector" pie chart look
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Ensure the pie is drawn as a circle
ax.axis('equal')

# Set the title
plt.title("Handheld Gaming Consoles Market Share Overview\nAn Insight into Market Distribution", fontsize=16, fontweight='bold', pad=20)

# Customize the texts and autotexts
plt.setp(texts, size=12, weight='bold', color='black')
plt.setp(autotexts, size=10, weight='bold', color='darkslategray')

# Add a legend outside of the pie chart
ax.legend(wedges, handheld_gaming_consoles, title="Consoles", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()