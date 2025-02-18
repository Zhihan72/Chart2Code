import matplotlib.pyplot as plt
import numpy as np

meal_types = ['Lunch', 'Hydration Fluids', 'Dinner', 'Snacks', 'Breakfast']

calorie_intake = [
    [465, 470, 490, 450, 480, 455, 465, 475, 450, 480, 490, 475, 460, 460, 450, 475, 480, 465, 460, 450, 475, 480, 460, 490, 465, 475, 480, 460, 450, 475, 460, 475, 450, 460, 470, 480, 475, 460, 480, 450, 460, 470, 490, 465, 455, 470, 450, 480, 455, 465, 480, 475],
    [32, 28, 25, 40, 35, 45, 30, 32, 28, 42, 35, 40, 32, 30, 25, 45, 40, 35, 32, 30, 32, 35, 40, 30, 45, 35, 40, 40, 35, 30, 35, 32, 35, 25, 32, 40, 38, 35, 32, 30, 40, 40, 35, 32, 30, 28, 40, 35, 32, 35, 30, 40],
    [520, 530, 515, 540, 525, 510, 550, 520, 510, 550, 540, 525, 515, 520, 510, 525, 540, 520, 510, 535, 520, 535, 540, 525, 520, 510, 540, 550, 510, 535, 520, 535, 540, 510, 545, 525, 540, 535, 520, 510, 530, 540, 530, 515, 515, 540, 520, 540, 515, 525, 530, 520],
    [160, 155, 150, 170, 165, 160, 155, 160, 150, 165, 170, 165, 160, 155, 150, 165, 170, 155, 150, 160, 155, 165, 170, 155, 150, 165, 160, 165, 155, 150, 165, 155, 165, 150, 170, 155, 165, 160, 155, 150, 160, 170, 165, 155, 150, 170, 155, 165, 150, 155, 160, 150],
    [250, 260, 245, 230, 260, 255, 270, 255, 250, 265, 275, 270, 280, 245, 250, 230, 255, 260, 250, 265, 270, 270, 255, 250, 255, 275, 260, 265, 250, 255, 260, 270, 270, 275, 280, 260, 255, 250, 265, 275, 255, 270, 270, 275, 250, 255, 270, 265, 275, 280, 255, 260]
]

fig, ax = plt.subplots(figsize=(14, 8))

boxplot = ax.boxplot(calorie_intake, vert=True, patch_artist=True, labels=meal_types, notch=True)

colors = ['#66B3FF', '#FFD700', '#99FF99', '#FFCC99', '#FF9999']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

medianprops = dict(linestyle='-', linewidth=2.5, color='darkred')
ax.boxplot(calorie_intake, vert=True, patch_artist=True, labels=meal_types, notch=True, 
           medianprops=medianprops)

plt.title('Astronaut Diet Observations: Weekly Meal Data', fontsize=16, fontweight='bold', color='darkslategray')
plt.xlabel('Types of Meals', fontsize=13, fontweight='bold')
plt.ylabel('Calories Consumed', fontsize=13, fontweight='bold')

ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

annotations = ["Midday Power", "Thirst Quench", 
               "Dinner Delight", "Snack Hits", 
               "Morning Boost"]
for i, annotation in enumerate(annotations):
    ax.text(i + 1, max(calorie_intake[i]) + 10, annotation, ha='center', va='bottom', 
            fontsize=10, color='navy')

plt.tight_layout()
plt.show()