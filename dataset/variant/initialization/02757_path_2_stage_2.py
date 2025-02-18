import matplotlib.pyplot as plt

projects = ['Mars Colonization', 'Asteroid Mining', 'Space Telescope Development', 
            'Lunar Research', 'Exoplanet Discovery']
budget_allocations = [30, 25, 20, 15, 10]

# New set of colors for the chart
colors = ['#fa8072', '#4682b4', '#8a2be2', '#ffd700', '#32cd32']

plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(budget_allocations, 
                                   labels=projects, 
                                   colors=colors, 
                                   autopct='%1.1f%%',
                                   startangle=90, 
                                   explode=(0.05, 0, 0, 0, 0),
                                   shadow=True)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)

plt.axis('equal')  
plt.title('IRA 2023 Budget Allocations\nStrategic Projects in Space Exploration', 
          fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()