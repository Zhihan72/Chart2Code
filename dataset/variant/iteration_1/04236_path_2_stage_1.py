import matplotlib.pyplot as plt
import numpy as np

# Data for educational focuses in different regions
regions = ['North America', 'Europe', 'Asia', 'Africa', 'South America', 'Oceania']
educational_focuses = ['Space Exploration', 'Cybersecurity', 'AI & Robotics', 'Quantum Computing', 'Renewable Energy', 'Biotechnology']  # Changed order
percentages = [15, 18, 20, 25, 10, 12]  # Altered percentages to match shuffled educational focuses

# Colors for each sector
colors = ['#FFCE56', '#9966FF', '#FF6384', '#FF9F40', '#36A2EB', '#4BC0C0']

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