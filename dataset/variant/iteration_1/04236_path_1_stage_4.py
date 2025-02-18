import matplotlib.pyplot as plt

regions = ['Oceania', 'S. America', 'Asia', 'Africa', 'Europe', 'N. America']
focuses = ['Quantum', 'Cybersec', 'AI', 'Renewable', 'Space', 'Biotech']
percentages = [25, 18, 20, 10, 15, 12]

colors = ['#3498DB', '#1ABC9C', '#9B59B6', '#E74C3C', '#F1C40F', '#2ECC71']

fig, ax = plt.subplots(figsize=(10, 8))

wedges, texts, autotexts = ax.pie(
    percentages,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    shadow=True
)

for i, text in enumerate(texts):
    text.set_text(f"{regions[i]}:\n{focuses[i]}")
    text.set_size(10)
    text.set_color('black')

plt.setp(autotexts, size=12, weight='bold', color='white')

ax.set_title("Ed. Focus Areas in 2075", fontsize=16, fontweight='bold', pad=20)

ax.legend(wedges, focuses, title="Focuses", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.show()