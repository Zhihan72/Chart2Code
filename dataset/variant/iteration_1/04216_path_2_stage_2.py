import matplotlib.pyplot as plt

# Data for the pie chart
handheld_gaming_consoles = ['Nintendo Switch', 'PlayStation Vita', 'Game Boy', 'PSP', 'Other']
market_share = [55, 15, 10, 15, 5]

# Shuffled colors for each console
colors = ['#c2c2f0', '#66b3ff', '#ffcc99', '#ff9999', '#99ff99']

# Create a pie chart
fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    market_share, 
    labels=handheld_gaming_consoles, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    pctdistance=0.85,
    explode=(0.1, 0, 0, 0.1, 0)
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

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()