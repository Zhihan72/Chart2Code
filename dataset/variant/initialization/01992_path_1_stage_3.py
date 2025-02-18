import matplotlib.pyplot as plt

continents = ['Afr', 'Ant', 'Asia', 'Eur', 'N. Am.', 'S. Am.', 'Oce']
initiatives_percentage = [15, 10, 25, 20, 18, 8, 4]
new_colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#33FFF3', '#A833FF', '#FFF333']

plt.figure(figsize=(12, 8))

explode = (0, 0, 0.1, 0, 0, 0, 0)
wedges, texts, autotexts = plt.pie(initiatives_percentage, labels=continents, autopct='%1.1f%%', startangle=120, colors=new_colors, shadow=True, explode=explode)

for w in wedges:
    w.set_linewidth(2)
    w.set_edgecolor('white')

plt.gca().add_artist(plt.Circle((0, 0), 0.70, color='white'))

plt.title('Global Exploration Initiatives\n by Cont.', fontsize=16, fontweight='bold', pad=20)
plt.legend(title="Cont.", loc='center left', bbox_to_anchor=(1.1, 0.5), fontsize=12)

plt.tight_layout()
plt.show()