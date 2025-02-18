import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
wheat_yield = np.array([2.8, 3.3, 2.9, 3.1, 3.5, 3.7, 3.6, 4.0, 3.8, 4.1, 4.4])
corn_yield = np.array([5.3, 5.1, 6.0, 5.4, 5.6, 5.9, 6.1, 6.4, 5.8, 6.2, 6.7])
soybean_yield = np.array([1.1, 1.5, 1.6, 1.4, 1.8, 1.7, 2.1, 2.3, 2.0, 2.4, 2.6])

fig, ax = plt.subplots(figsize=(12, 8))

# Apply a consistent color 'blue' across all data groups
uniform_color = 'blue'

ax.plot(years, wheat_yield, color=uniform_color, marker='o', linewidth=2, linestyle='-')
ax.plot(years, corn_yield, color=uniform_color, marker='s', linewidth=2, linestyle='-.')
ax.plot(years, soybean_yield, color=uniform_color, marker='^', linewidth=2, linestyle='--')

ax.set_title('Crop Growth Trends: 2010s', fontsize=16, fontweight='bold', loc='center', pad=20)
ax.set_xlabel('Calendar Year', fontsize=12)
ax.set_ylabel('Production Volume (tons)', fontsize=12)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

ax.annotate('Eco-Friendly Approaches Adopted', xy=(2015, 3.5), xytext=(2013, 4.0),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, backgroundcolor='white')
ax.annotate('Year of Scarcity', xy=(2012, 6.0), xytext=(2009, 5.5),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, backgroundcolor='white')
ax.annotate('Debut of New Soybean Type', xy=(2017, 2.3), xytext=(2015, 2.2),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, backgroundcolor='white')

plt.tight_layout()
plt.show()