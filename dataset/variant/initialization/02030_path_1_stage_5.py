import matplotlib.pyplot as plt

beverages = ['Organic Tea', 'Herbal Infusion', 'Kombucha', 'Coconut Water', 'Aloe Vera Juice']
production_volumes = [55, 42, 63, 80, 37]

fig, ax = plt.subplots(figsize=(10, 6))
# Use a single consistent color for all bars
ax.bar(beverages, production_volumes, color='#8FD14F', alpha=0.85, edgecolor='black')
ax.set_xticklabels([])
ax.set_yticklabels([])
plt.tight_layout()
plt.show()