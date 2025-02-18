import matplotlib.pyplot as plt

# Multiple datasets to be stacked in the histogram
energy_consumption_2022 = [
    150, 155, 160, 162, 165, 170, 175, 180, 185, 188, 190, 195, 198, 200, 205,
    210, 215, 220, 223, 225, 230, 235, 238, 240, 245, 250, 255, 258, 260, 265,
    270, 275, 278, 280, 285, 290, 295, 300, 310, 320, 330, 340, 350, 360, 370,
    380, 390, 400, 410, 420, 425, 430, 435, 440, 445, 450, 460, 470, 480, 490
]

energy_consumption_2023 = [
    160, 165, 170, 172, 175, 180, 185, 190, 192, 195, 198, 200, 205, 210, 215,
    220, 225, 230, 235, 238, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285,
    290, 295, 300, 305, 310, 315, 320, 330, 340, 350, 360, 370, 380, 390, 400,
    410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 505, 510, 520, 530, 540
]

plt.figure(figsize=(12, 8))

# Creating the stacked histogram
plt.hist([energy_consumption_2022, energy_consumption_2023], bins=14, stacked=True, color=['cadetblue', 'lightcoral'], edgecolor='black', alpha=0.8, label=['2022', '2023'])

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.legend(fontsize=10)
plt.tight_layout()

plt.show()