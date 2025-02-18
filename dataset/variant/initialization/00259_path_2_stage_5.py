import matplotlib.pyplot as plt
import numpy as np

years_experience = np.array([1, 3, 5, 7, 10, 12, 15, 18, 20, 25, 30, 35, 40])
ai_adoption_rate = np.array([70, 65, 60, 55, 50, 52, 48, 45, 42, 40, 38, 35, 30])
number_of_tools = np.array([5, 4, 4, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1]) * 10

fig, ax = plt.subplots(figsize=(7, 8))

ax.scatter(years_experience, ai_adoption_rate, s=number_of_tools,
           c='mediumslateblue', alpha=0.8, edgecolors='orange', linewidth=1.5)

# Altered text elements by rearranging
ax.set_title("Experience vs. Rate:\nHealthcare AI Adoption", fontsize=14, fontweight='normal')
ax.set_xlabel("Adoption Rate (%)", fontsize=13, style='italic')
ax.set_ylabel("Years in Field", fontsize=13, style='italic')
ax.set_xticks(years_experience[::2])

ax.grid(True, linestyle='-.', which='both', axis='y', color='gray', alpha=0.3, linewidth=0.7)

for i, (x, y) in enumerate(zip(years_experience, ai_adoption_rate)):
    ax.annotate(f'{number_of_tools[i]//10}',
                (x, y), textcoords="offset points", xytext=(0, -12), ha='center', fontsize=8, color='darkred')

ax.legend(['Tools Size Bubble'], loc='lower left', fontsize=10, frameon=True, facecolor='whitesmoke', edgecolor='darkblue')

plt.tight_layout()
plt.show()