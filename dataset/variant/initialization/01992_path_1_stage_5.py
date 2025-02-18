import matplotlib.pyplot as plt

# Updated list of continents to include fictional groups
continents = ['Afr', 'Ant', 'Asia', 'Eur', 'N. Am.', 'S. Am.', 'Oce', 'Atlantis', 'Lemuria']
# Updated percentage to include the new groups
initiatives_percentage = [15, 10, 25, 20, 18, 8, 4, 5, 3]
# Extended color scheme to cover the additional slices
new_colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#33FFF3', '#A833FF', '#FFF333', '#8A33FF', '#33FFA5']

plt.figure(figsize=(12, 8))
explode = (0, 0, 0.1, 0, 0, 0, 0, 0, 0)
wedges, texts, autotexts = plt.pie(
    initiatives_percentage, 
    labels=continents, 
    autopct='%1.1f%%', 
    startangle=120, 
    colors=new_colors, 
    explode=explode
)

for w in wedges:
    w.set_linewidth(2)
    w.set_edgecolor('white')

plt.gca().add_artist(plt.Circle((0, 0), 0.70, color='white'))

plt.title('Global Exploration Initiatives\n by Cont.', fontsize=16, fontweight='bold', pad=20)

plt.show()