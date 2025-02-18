import matplotlib.pyplot as plt

# Updated data for public interest in space missions (in percentage)
categories = [
    'Planetary Exploration', 
    'Space Telescopes', 
    'Human Spaceflight', 
    'Astronomical Research', 
    'Space Mining',
    'Mars Colonization',
    'Space Tourism'
]
interest = [25, 20, 18, 12, 8, 10, 7]

# Define colors for each category
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff6666', '#c2c2f0', '#ffb3e6']

# Create the pie chart
fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))

# Plot the pie chart
wedges, texts, autotexts = ax.pie(
    interest, 
    labels=categories, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    pctdistance=0.85, 
    wedgeprops=dict(edgecolor='white', linewidth=1.5),
    explode=(0.1, 0, 0, 0, 0, 0.1, 0),  # Slightly explode the 'Planetary Exploration' and 'Mars Colonization'
    shadow=True
)

# Customize the autotexts (percentages) on pie wedges
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# Adjust labels for better readability
for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('normal')

# Add a title
ax.set_title(
    "Public Interest in Different Aspects of Space Missions (2023):\n"
    "A Survey by Space Exploration Agency",
    fontsize=16, fontweight='bold', pad=20
)

# Add a legend
ax.legend(
    wedges, categories, 
    title="Interest Areas", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=10, title_fontsize='12'
)

# Draw a circle at the center to transform the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

# Automatically adjust layout to prevent overlap and clipping
plt.tight_layout()

plt.show()