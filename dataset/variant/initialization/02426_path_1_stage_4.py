import matplotlib.pyplot as plt

tropical_growth = [60, 65, 58, 62, 68, 61, 63, 64, 66, 60, 67, 65]
temperate_growth = [35, 40, 38, 42, 37, 39, 41, 36, 34, 43, 38, 39]
desert_growth = [10, 12, 11, 9, 13, 14, 8, 11, 12, 15, 10, 9]

growth_data = [tropical_growth, temperate_growth, desert_growth]

climate_zones = ['Arid', 'Humid Tropics', 'Mild']

plt.figure(figsize=(10, 6))
box = plt.boxplot(
    growth_data, patch_artist=True, labels=climate_zones, 
    notch=True, medianprops={'color': 'red'}, vert=True
)

single_color = '#2E8B57'
for patch in box['boxes']:
    patch.set_facecolor(single_color)

plt.xlabel('Environmental Types', fontsize=12)
plt.ylabel('Rate of Growth (yearly cm)', fontsize=12)

plt.tight_layout()
plt.show()