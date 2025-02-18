import matplotlib.pyplot as plt
import numpy as np

meal_types = ['Lunch', 'Hydration Fluids', 'Dinner', 'Snacks', 'Breakfast']

calorie_intake = [
    [460, 470, 450, 480, 490, 475, 465, 460, 450, 480, 490, 475, 465, 460, 450, 490, 480, 475, 460, 450, 460, 475, 480, 465, 460, 475, 480, 490, 450, 460, 475, 460, 475, 450, 480, 465, 475, 480, 460, 450, 460, 480, 470, 465, 455, 470, 450, 480, 455, 465, 470, 460],
    [30, 35, 25, 40, 45, 35, 30, 32, 28, 42, 40, 35, 32, 30, 25, 40, 45, 35, 32, 28, 32, 35, 40, 35, 30, 35, 45, 40, 32, 30, 35, 32, 35, 25, 40, 35, 38, 40, 32, 30, 35, 40, 35, 32, 30, 40, 25, 40, 35, 32, 30, 28],
    [520, 530, 510, 540, 550, 525, 515, 520, 510, 540, 550, 525, 515, 520, 510, 550, 540, 525, 520, 510, 520, 535, 540, 525, 520, 535, 540, 550, 510, 520, 535, 520, 535, 510, 545, 525, 540, 535, 520, 510, 520, 540, 530, 525, 515, 540, 510, 540, 515, 525, 530, 520],
    [150, 160, 155, 170, 165, 160, 155, 160, 155, 165, 170, 165, 160, 155, 150, 165, 170, 155, 150, 160, 155, 165, 170, 155, 150, 165, 160, 165, 155, 150, 165, 155, 165, 150, 170, 155, 165, 160, 155, 150, 160, 170, 165, 155, 150, 170, 155, 165, 150, 155, 160, 150],
    [230, 250, 245, 270, 260, 255, 240, 255, 250, 265, 270, 275, 280, 260, 245, 250, 230, 255, 260, 250, 265, 270, 270, 255, 250, 275, 260, 265, 250, 255, 260, 270, 270, 275, 280, 260, 255, 270, 265, 250, 255, 270, 270, 275, 250, 255, 270, 265, 275, 280, 255, 260]
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