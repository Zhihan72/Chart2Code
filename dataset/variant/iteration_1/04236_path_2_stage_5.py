import matplotlib.pyplot as plt

# Data
educational_focuses = ['Space', 'Cybersec', 'AI & Robo', 'Quantum', 'Renewable', 'Biotech']
percentages = [15, 18, 20, 25, 10, 12]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A4', '#33FFD6', '#FFD633']
explode = [0.1 if perc == max(percentages) else 0.05 if perc == min(percentages) else 0 for perc in percentages]

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(aspect="equal"))

# Plot a pie chart with distinct colors for each section
wedges, texts, autotexts = ax.pie(
    percentages,
    explode=explode,
    labels=None,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    shadow=False
)

# Set size and color for the percentage labels
plt.setp(autotexts, size=10, weight='normal', color='black')

# Title with altered font style
ax.set_title("Global Edu Focus 2075", fontsize=18, fontweight='light', pad=10)

# Legend settings with focus areas
ax.legend(wedges, educational_focuses, title="Focus Areas", loc="upper right", bbox_to_anchor=(-0.1, 1))

plt.grid(True, linestyle='--', linewidth=0.5)
plt.tight_layout()

plt.show()