import numpy as np
import matplotlib.pyplot as plt

# Define plantation area data (in hectares) for different fruits in "Tropical Bay"
mango = np.array([5, 7, 8, 10, 14, 18, 22, 30, 40, 52, 65, 80, 98, 115, 135, 150, 170, 195, 220, 245, 270])
pineapple = np.array([4, 5, 6, 7, 9, 10, 12, 15, 18, 22, 27, 32, 40, 45, 50, 55, 62, 70, 78, 85, 92])
banana = np.array([6, 8, 10, 14, 18, 22, 28, 35, 42, 50, 60, 70, 85, 95, 110, 125, 140, 160, 182, 200, 225])
coconut = np.array([2, 3, 4, 5, 6, 7, 9, 11, 14, 17, 21, 25, 30, 35, 42, 50, 58, 68, 78, 88, 100])
papaya = np.array([1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 22, 25, 30, 35, 40, 45, 50, 55, 60, 66])
# Additional made-up data for new fruits
durian = np.array([3, 4, 5, 6, 7, 8, 10, 13, 16, 20, 25, 30, 35, 42, 50, 60, 72, 85, 100, 115, 130])
lychee = np.array([2, 3, 4, 6, 8, 10, 13, 17, 22, 28, 35, 45, 55, 67, 80, 95, 110, 130, 150, 172, 195])

# Stack the data for boxplot
plantation_data = [mango, pineapple, banana, coconut, papaya, durian, lychee]

# Create the horizontal box plot
fig, ax = plt.subplots(figsize=(12, 10))

fruit_labels = ['Mango', 'Pineapple', 'Banana', 'Coconut', 'Papaya', 'Durian', 'Lychee']

ax.boxplot(plantation_data, vert=False, patch_artist=True, labels=fruit_labels,
           boxprops=dict(facecolor='lightblue', color='blue'),
           whiskerprops=dict(color='black'),
           capprops=dict(color='black'),
           medianprops=dict(color='red'))

ax.set_title("Distribution of Plantation Areas (2000-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Total Plantation Area (Hectares)', fontsize=12)
ax.grid(linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()