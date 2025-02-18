import matplotlib.pyplot as plt
import numpy as np

# Data updates with shortened names
regions = ['N. America', 'Europe', 'Asia', 'Africa', 'S. America', 'Oceania']
educational_focuses = ['Space', 'Cybersec', 'AI & Robo', 'Quantum', 'Renewable', 'Biotech']
percentages = [15, 18, 20, 25, 10, 12]

colors = ['#FFCE56', '#9966FF', '#FF6384', '#FF9F40', '#36A2EB', '#4BC0C0']
explode = [0.1 if perc == max(percentages) else 0.05 if perc == min(percentages) else 0 for perc in percentages]

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(aspect="equal"))

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

# Annotating each wedge with abbreviated labels
for i, text in enumerate(texts):
    txt = f"{regions[i]}:\n{educational_focuses[i]}"
    text.set_text(txt)
    text.set_size(10)
    text.set_color('black')

plt.setp(autotexts, size=12, weight='bold', color='white')

# Adding center circle for the donut shape
centre_circle = plt.Circle((0,0), 0.70, fc='white')
ax.add_artist(centre_circle)

# Simplified title
ax.set_title("Global Edu Focus 2075", fontsize=16, fontweight='bold', pad=20)

# Legend settings with abbreviated names
ax.legend(wedges, educational_focuses, title="Focus Areas", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()

plt.show()