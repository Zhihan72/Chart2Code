import matplotlib.pyplot as plt

labels_food = ['Frt', 'Veg', 'Grn', 'Pro', 'Dai']
production_sizes = [30, 25, 20, 15, 10]
colors_food = ['#FFCC99', '#FF9999', '#C2C2F0', '#66B3FF', '#99FF99']

colonies = ["Z-1", "X-13", "O-8", "B-3", "L-22"]
sweet_consumption = [100, 150, 90, 110, 130]

fig, ax = plt.subplots(1, 2, figsize=(14, 7))

ax[1].pie(
    production_sizes, 
    startangle=90, 
    colors=colors_food, 
    wedgeprops={'width': 0.4, 'edgecolor': 'w', 'alpha': 0.85}
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax[1].add_artist(centre_circle)
ax[1].axis('equal')

ax[0].barh(colonies, sweet_consumption, color='#FFDA79', edgecolor='black')

plt.show()