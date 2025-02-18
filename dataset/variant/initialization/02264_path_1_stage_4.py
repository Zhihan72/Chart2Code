import matplotlib.pyplot as plt
import numpy as np

specializations = [
    'Data Sci', 
    'Cybersec', 
    'AI & ML', 
    'Soft Eng', 
    'Network', 
    'Web Dev',
    'Blockchain',
    'Quantum'
]
percentages = [22, 18, 14, 16, 10, 8, 7, 5]

colors = plt.cm.Paired(np.linspace(0, 1, len(specializations)))

line_styles = ['-', '--', '-.', ':']  # Adding a variety of line styles
marker_styles = ['o', 's', 'D', '*', 'p', 'X', '^', 'v']  # Adding a variety of marker styles

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    percentages, 
    labels=specializations, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors,
    wedgeprops=dict(linestyle=line_styles[1])  # Using a different line style
)

plt.setp(autotexts, size=10, weight="bold", color="darkblue")
plt.setp(texts, size=12)

plt.title(
    'CS/IT Grads Specialization (2023)',
    fontsize=16, fontweight='bold', color="maroon"
)

ax.axis('equal')

# Removing the legend for stylistic change
# ax.legend(wedges, specializations, title="Specializations", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

ax.grid(axis='y', linestyle=line_styles[2], linewidth=0.5)  # Adding grid with a new line style

plt.tight_layout()

plt.show()