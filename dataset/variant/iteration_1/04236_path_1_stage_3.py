import matplotlib.pyplot as plt
import numpy as np

regions = ['Oceania', 'S. America', 'Asia', 'Africa', 'Europe', 'N. America']
focuses = ['Quantum', 'Cybersec', 'AI', 'Renewable', 'Space', 'Biotech']
percentages = [25, 18, 20, 10, 15, 12]

colors = ['#3498DB', '#1ABC9C', '#9B59B6', '#E74C3C', '#F1C40F', '#2ECC71']
explode = [0.1 if perc == max(percentages) else 0.05 if perc == min(percentages) else 0 for perc in percentages]

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(
    percentages,
    explode=explode,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    shadow=True
)

for i, text in enumerate(texts):
    txt = f"{regions[i]}:\n{focuses[i]}"
    text.set_text(txt)
    text.set_size(10)
    text.set_color('black')

plt.setp(autotexts, size=12, weight='bold', color='white')

centre_circle = plt.Circle((0,0), 0.70, fc='white')
ax.add_artist(centre_circle)

ax.set_title("Ed. Focus Areas in 2075", fontsize=16, fontweight='bold', pad=20)

ax.legend(wedges, focuses, title="Focuses", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.show()