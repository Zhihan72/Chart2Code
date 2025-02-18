import matplotlib.pyplot as plt

# Data: Distribution of Volunteers for a Community Event
volunteer_roles = ['Organizers', 'Mentors', 'Caterers', 'Performers', 'Security', 'Technical Support']
volunteer_counts = [15, 25, 18, 10, 8, 14]

# Colors for each segment in the pie chart
colors = ['#FF6347', '#FFD700', '#8A2BE2', '#4682B4', '#32CD32', '#FF69B4']

# Creating the pie chart
fig, ax = plt.subplots(figsize=(10, 7))

# Explode first and fourth segments
explode = (0.1, 0, 0, 0.1, 0, 0)

# Plot pie chart
wedges, texts, autotexts = ax.pie(
    volunteer_counts,
    labels=volunteer_roles,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    explode=explode,
    shadow=True
)

# Customize font properties for better visibility
for text in texts:
    text.set_fontsize(10)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# Setting the title of the chart
ax.set_title(
    "Volunteer Role Distribution for Annual Community Event",
    fontsize=14, fontweight='bold', pad=20
)

# Add a legend outside the pie chart for clarity
ax.legend(
    wedges, volunteer_roles,
    title="Volunteer Roles",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)

# Ensure the layout fits well on display
plt.tight_layout()

# Display the plot
plt.show()