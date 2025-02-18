import matplotlib.pyplot as plt

tech_advancement = {
    'AI and Robotics': 41,
    'Sustainable Energy': 36,
    'Biotechnology': 31,
}

labels = list(tech_advancement.keys())
sizes = list(tech_advancement.values())
colors = ['#FF4500', '#2E8B57', '#6A5ACD']

fig, ax = plt.subplots(figsize=(9, 9))
ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)

ax.set_title('Distribution of Technological Advancements in 3050', fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()