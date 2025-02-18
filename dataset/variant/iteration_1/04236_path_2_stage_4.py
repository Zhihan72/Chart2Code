import matplotlib.pyplot as plt

# Data
educational_focuses = ['Space', 'Cybersec', 'AI & Robo', 'Quantum', 'Renewable', 'Biotech']
percentages = [15, 18, 20, 25, 10, 12]
single_color = ['#FFCE56'] * len(percentages)
explode = [0.1 if perc == max(percentages) else 0.05 if perc == min(percentages) else 0 for perc in percentages]

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(aspect="equal"))

# Plot a pie chart with a single color for all sections
wedges, texts, autotexts = ax.pie(
    percentages,
    explode=explode,
    labels=None,
    colors=single_color,
    autopct='%1.1f%%',
    startangle=140,
    shadow=True
)

# Set size and color for the percentage labels
plt.setp(autotexts, size=12, weight='bold', color='white')

# Title
ax.set_title("Global Edu Focus 2075", fontsize=16, fontweight='bold', pad=20)

# Legend settings with focus areas
ax.legend(wedges, educational_focuses, title="Focus Areas", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()

plt.show()