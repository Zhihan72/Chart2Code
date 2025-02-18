import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# In 2075, educational curriculums in various global regions have evolved to include courses focusing on technological advancements.
# This pie chart explores the distribution of these educational focuses.

# Data for educational focuses in different regions
regions = ['North America', 'Europe', 'Asia', 'Africa', 'South America', 'Oceania']
educational_focuses = ['AI & Robotics', 'Renewable Energy', 'Space Exploration', 'Biotechnology', 'Cybersecurity', 'Quantum Computing']
percentages = [20, 10, 15, 12, 18, 25]

# Colors for each sector
colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40']

# Exploding the largest and smallest sectors for emphasis
explode = [0.1 if perc == max(percentages) else 0.05 if perc == min(percentages) else 0 for perc in percentages]

# Create a figure and a single subplot
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(aspect="equal"))

# Pie chart plotting
wedges, texts, autotexts = ax.pie(
    percentages,
    explode=explode,
    labels=None,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    shadow=True
)

# Annotating each wedge with the region labels
for i, text in enumerate(texts):
    txt = f"{regions[i]}:\n{educational_focuses[i]}"
    text.set_text(txt)
    text.set_size(10)
    text.set_color('black')

# Customizing the inner text percentages
plt.setp(autotexts, size=12, weight='bold', color='white')

# Adding center circle for the donut shape
centre_circle = plt.Circle((0,0), 0.70, fc='white')
ax.add_artist(centre_circle)

# Title and context settings
ax.set_title("Educational Focus Areas Across Global Regions in 2075", fontsize=16, fontweight='bold', pad=20)

# Legend settings
ax.legend(wedges, educational_focuses, title="Focus Areas", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Ensuring the layout is tight and neat
plt.tight_layout()

# Displaying the chart
plt.show()