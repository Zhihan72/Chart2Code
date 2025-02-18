import matplotlib.pyplot as plt
import numpy as np

focus_areas = ['IoT', 'Cybersecurity', 'Blockchain', 'Artificial Intelligence', 'Fintech', 'HealthTech', 'EdTech']
percentages = [7, 3, 12, 25, 20, 18, 15]  # Rearranged percentage distribution

colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#C71585', '#7B68EE']

fig, ax = plt.subplots(figsize=(10, 8))
explode = (0, 0, 0, 0.05, 0.05, 0, 0)
wedges, texts, autotexts = ax.pie(percentages, labels=focus_areas, autopct='%1.1f%%',
                                  startangle=140, colors=colors, pctdistance=0.85,
                                  wedgeprops=dict(width=0.3, edgecolor='w'), explode=explode, shadow=True)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)
plt.axis('equal')  
ax.set_title("Technology Startups by Focus Area in 2023", fontsize=16, fontweight='bold', pad=20)
ax.legend(wedges, focus_areas, title="Focus Areas", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

for autotext in autotexts:
    autotext.set_color('darkblue')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

plt.tight_layout()
plt.show()