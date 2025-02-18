import matplotlib.pyplot as plt
import numpy as np

specializations = [
    'Data Science', 
    'Cybersecurity', 
    'AI & ML', 
    'Software Engineering', 
    'Networking', 
    'Web Development',
    'Blockchain',
    'Quantum Computing'
]
percentages = [22, 18, 14, 16, 10, 8, 7, 5]

colors = plt.cm.Set3(np.linspace(0, 1, len(specializations)))
explode = (0, 0, 0, 0, 0, 0, 0, 0)  # No segment is exploded

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
    'Distribution of Specializations Among \n'
    'Computer Science and Information Technology Graduates (2023)',
    fontsize=14, fontweight='bold'
)

ax.axis('equal')

ax.legend(wedges, specializations, title="Specializations", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()

plt.show()