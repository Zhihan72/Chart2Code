import matplotlib.pyplot as plt

productivity_data = {
    'Lunes': [4, 5, 6, 5, 7, 8, 5, 6, 4, 6],
    'Martes': [6, 7, 5, 6, 8, 9, 7, 6, 8, 9],
    'Miércoles': [7, 8, 6, 7, 9, 9, 7, 8, 6, 7],
    'Jueves': [5, 6, 5, 6, 7, 7, 8, 6, 5, 6],
    'Viernes': [4, 5, 4, 5, 6, 6, 5, 4, 5, 6],
    'Sábado': [2, 3, 2, 4, 3, 4, 3, 2, 3, 4],
    'Domingo': [1, 2, 1, 3, 2, 2, 3, 1, 2, 1],
    'Super Lunes': [8, 9, 8, 9, 10, 10, 9, 8, 9, 10]  # New data series
}

box_plot_data = list(productivity_data.values())
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightpink', 'lightgray', 
          'lightgoldenrodyellow', 'lightsteelblue']  # Added new color for 'Super Lunes'

fig, ax = plt.subplots(figsize=(14, 10))

bplots = ax.boxplot(box_plot_data, vert=False, labels=productivity_data.keys(),
                    patch_artist=True, notch=True, medianprops=dict(color='black'))

for patch, color in zip(bplots['boxes'], colors):
    patch.set_facecolor(color)

ax.set_xlabel('Puntuación de Productividad (1-10)', fontsize=14)
ax.set_ylabel('Día de la Semana', fontsize=14)

plt.tight_layout()
plt.show()