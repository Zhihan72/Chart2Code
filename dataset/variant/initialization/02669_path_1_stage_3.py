import matplotlib.pyplot as plt

# Removed the second group of data
energy_consumption = [
    150, 155, 160, 162, 165, 170, 175, 180, 185, 188, 190, 195, 198, 200, 205,
    210, 215, 220, 223, 225, 230, 235, 238, 240, 245, 250, 255, 258, 260, 265,
    270, 275, 278, 280, 285, 290, 295, 300, 310, 320, 330, 340, 350, 360, 370,
    380, 390, 400, 410, 420, 425, 430, 435, 440, 445, 450, 460, 470, 480, 490
]

plt.figure(figsize=(12, 8))
plt.hist(energy_consumption, bins=14, color='cadetblue', edgecolor='black', alpha=0.8)

plt.xlabel('Energy Consumption (GWh)', fontsize=12)
plt.ylabel('Number of Neighborhoods', fontsize=12)

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.tight_layout()

plt.show()