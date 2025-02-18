import matplotlib.pyplot as plt

sectors = [
    'Biotech Future', 
    'A. Electronics', 
    'Green Energy Prod.', 
    'Precision Tools'
]
gdp_contribution = [40, 20, 10, 10]

colors = ['#FF9999', '#66B3FF', '#FFCC99', '#E0E0E0']

fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    gdp_contribution,
    labels=sectors,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'linewidth': 0, 'width': 0.3},  # Set the width here for a donut version
    pctdistance=0.85
)

# Create a white circle in the center to transform pie chart into a donut (ring) chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

# Adjust the size of the annotations inside the pie chart
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Add central text for visual appeal
ax.text(0, 0, 'Tech Growth\nSnapshot', fontsize=14, fontweight='bold', ha='center', va='center')

plt.tight_layout()
plt.show()