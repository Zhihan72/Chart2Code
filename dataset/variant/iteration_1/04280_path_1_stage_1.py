import matplotlib.pyplot as plt

# Data: Randomly altered to reflect new distribution labels
volunteer_roles = ['Directors', 'Coaches', 'Chefs', 'Artists', 'Security', 'IT Support']
volunteer_counts = [15, 25, 18, 10, 8, 14]

# Colors remain the same
colors = ['#FF6347', '#FFD700', '#8A2BE2', '#4682B4', '#32CD32', '#FF69B4']

# Create pie chart
fig, ax = plt.subplots(figsize=(10, 7))

# Explode section updated
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

# Setting the title of the chart changed
ax.set_title(
    "Volunteer Role Allocation for Spring Festival",
    fontsize=14, fontweight='bold', pad=20
)

# Updated legend
ax.legend(
    wedges, volunteer_roles,
    title="Event Roles",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)

# Ensure the layout fits well on display
plt.tight_layout()

# Display the plot
plt.show()