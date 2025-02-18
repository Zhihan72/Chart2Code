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

# New set of colors for the pie chart
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#FF69B4', '#8A2BE2', '#00CED1']

line_styles = ['-', '--', '-.', ':']
marker_styles = ['o', 's', 'D', '*', 'p', 'X', '^', 'v']

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    percentages, 
    labels=specializations, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors,
    wedgeprops=dict(linestyle=line_styles[1])
)

plt.setp(autotexts, size=10, weight="bold", color="darkblue")
plt.setp(texts, size=12)

plt.title(
    'CS/IT Grads Specialization (2023)',
    fontsize=16, fontweight='bold', color="maroon"
)

ax.axis('equal')
ax.grid(axis='y', linestyle=line_styles[2], linewidth=0.5)  

plt.tight_layout()

plt.show()