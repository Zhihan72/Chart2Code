import matplotlib.pyplot as plt

# Data
volunteer_roles = ['Directors', 'Coaches', 'Chefs', 'Artists', 'Security', 'IT Support']
volunteer_counts = [15, 25, 18, 10, 8, 14]
colors = ['#FF6347', '#FFD700', '#8A2BE2', '#4682B4', '#32CD32', '#FF69B4']

# Create pie chart
fig, ax = plt.subplots(figsize=(8, 8))

# Altered explode and shadow settings
explode = (0, 0.1, 0, 0, 0.1, 0)

wedges, texts, autotexts = ax.pie(
    volunteer_counts,
    labels=volunteer_roles,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    explode=explode,
    shadow=False
)

# Customize font properties
for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('regular')

for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_color('navy')
    autotext.set_fontweight('bold')

# Updated title style
ax.set_title(
    "Spring Fest Volunteer Roles",
    fontsize=16, fontweight='bold', pad=15
)

# Changed legend settings
ax.legend(
    wedges, volunteer_roles,
    title="Roles",
    loc="upper right",
    bbox_to_anchor=(1, 0.7)
)

# Added grid to the plot
ax.grid(visible=True)

# Display the plot
plt.show()