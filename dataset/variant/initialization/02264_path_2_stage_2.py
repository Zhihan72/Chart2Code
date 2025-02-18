import matplotlib.pyplot as plt

specializations = [
    'Data Science', 
    'Cybersecurity', 
    'AI & ML', 
    'Software Engineering', 
    'Networking', 
    'Web Development'
]
percentages = [25, 20, 15, 18, 12, 10]

single_color = ['#66c2a5' for _ in range(len(specializations))]
explode = (0.1, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    percentages, 
    labels=specializations, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=single_color,
    explode=explode
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