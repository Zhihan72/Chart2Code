import matplotlib.pyplot as plt

growth_data = [
    [60, 65, 58, 62, 68, 61, 63, 64, 66, 60, 67, 65], 
    [35, 40, 38, 42, 37, 39, 41, 36, 34, 43, 38, 39], 
    [10, 12, 11, 9, 13, 14, 8, 11, 12, 15, 10, 9],    
    [5, 4, 6, 3, 4, 5, 5, 6, 3, 4, 4, 5]              
]

plt.figure(figsize=(10, 6))
box = plt.boxplot(growth_data, patch_artist=True, notch=True, medianprops={'color': 'red'})

colors = ['skyblue', 'lightgreen', 'lightcoral', 'plum']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()