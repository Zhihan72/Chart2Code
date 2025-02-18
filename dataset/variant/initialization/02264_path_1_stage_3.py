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

colors = plt.cm.Set3(np.linspace(0, 1, len(specializations)))

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    percentages, 
    labels=specializations, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors
)

plt.setp(autotexts, size=10, weight="bold", color="black")
plt.setp(texts, size=12)

plt.title(
    'CS/IT Grads Specialization (2023)',
    fontsize=14, fontweight='bold'
)

ax.axis('equal')

ax.legend(wedges, specializations, title="Specializations", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()

plt.show()