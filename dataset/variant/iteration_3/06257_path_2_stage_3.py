import matplotlib.pyplot as plt

meal_types = ['Breakfast', 'Lunch', 'Dinner', 'Snacks', 'Hydration Fluids']
calorie_intake = [
    [230, 250, 245, 270, 260, 255, 240, 255, 250, 265, 270, 275, 280, 260, 245, 250, 230, 255, 260, 250, 265, 270, 270, 255, 250, 275, 260, 265, 250, 255, 260, 270, 270, 275, 280, 260, 255, 270, 265, 250, 255, 270, 270, 275, 250, 255, 270, 265, 275, 280, 255, 260],
    [460, 470, 450, 480, 490, 475, 465, 460, 450, 480, 490, 475, 465, 460, 450, 490, 480, 475, 460, 450, 460, 475, 480, 465, 460, 475, 480, 490, 450, 460, 475, 460, 475, 450, 480, 465, 475, 480, 460, 450, 460, 480, 470, 465, 455, 470, 450, 480, 455, 465, 470, 460],
    [520, 530, 510, 540, 550, 525, 515, 520, 510, 540, 550, 525, 515, 520, 510, 550, 540, 525, 520, 510, 520, 535, 540, 525, 520, 535, 540, 550, 510, 520, 535, 520, 535, 510, 545, 525, 540, 535, 520, 510, 520, 540, 530, 525, 515, 540, 510, 540, 515, 525, 530, 520],
    [150, 160, 155, 170, 165, 160, 155, 160, 155, 165, 170, 165, 160, 155, 150, 165, 170, 155, 150, 160, 155, 165, 170, 155, 150, 165, 160, 165, 155, 150, 165, 155, 165, 150, 170, 155, 165, 160, 155, 150, 160, 170, 165, 155, 150, 170, 155, 165, 150, 155, 160, 150],
    [30, 35, 25, 40, 45, 35, 30, 32, 28, 42, 40, 35, 32, 30, 25, 40, 45, 35, 32, 28, 32, 35, 40, 35, 30, 35, 45, 40, 32, 30, 35, 32, 35, 25, 40, 35, 38, 40, 32, 30, 35, 40, 35, 32, 30, 40, 25, 40, 35, 32, 30, 28]
]

fig, ax = plt.subplots(figsize=(14, 8))

boxplot = ax.boxplot(calorie_intake, vert=False, patch_artist=True, labels=meal_types)

colors = ['#5F9EA0', '#FFD700', '#008080', '#8A2BE2', '#FF4500']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

medianprops = dict(linestyle='--', linewidth=1.5, color='black')
ax.boxplot(calorie_intake, vert=False, patch_artist=True, labels=meal_types, 
           medianprops=medianprops)

plt.title('Mars Colony Nutrition Study: Calorie Intake by Meal Type (2050)', fontsize=15, color='teal')
plt.ylabel('Meal Categories', fontsize=12)
plt.xlabel('Caloric Values (Calories)', fontsize=12, color='maroon')

ax.xaxis.grid(False)

annotations = ["Kickstart", "Refuel", "Nourish", "Nibbles", "Hydrate"]
for i, annotation in enumerate(annotations):
    ax.text(max(calorie_intake[i]) + 10, i + 1, annotation, ha='left', va='center', fontsize=10, color='red')

for box in boxplot['boxes']:
    box.set(linewidth=0)

plt.tight_layout()
plt.show()