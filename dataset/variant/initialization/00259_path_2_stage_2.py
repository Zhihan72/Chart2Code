import matplotlib.pyplot as plt
import numpy as np

years_experience = np.array([1, 3, 5, 7, 10, 12, 15, 18, 20, 25, 30, 35, 40])
ai_adoption_rate = np.array([70, 65, 60, 55, 50, 52, 48, 45, 42, 40, 38, 35, 30])
number_of_tools = np.array([5, 4, 4, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1]) * 10
ai_influence_index = np.array([5, 15, 28, 40, 60, 75, 90, 110, 130, 160, 200, 240, 280])

fig, axs = plt.subplots(1, 2, figsize=(14, 8))

scatter = axs[0].scatter(years_experience, ai_adoption_rate, s=number_of_tools,
                          c='mediumslateblue', alpha=0.8, edgecolors='orange', linewidth=1.5)
axs[0].set_title("AI Adoption in Healthcare:\nExperience vs. Adoption Rate", fontsize=14, fontweight='normal')
axs[0].set_xlabel("Years of Experience", fontsize=13, style='italic')
axs[0].set_ylabel("AI Adoption Rate (%)", fontsize=13, style='italic')
axs[0].set_xticks(years_experience[::2])

axs[0].grid(True, linestyle='-.', which='both', axis='y', color='gray', alpha=0.3, linewidth=0.7)

for i, (x, y) in enumerate(zip(years_experience, ai_adoption_rate)):
    axs[0].annotate(f'{number_of_tools[i]//10}',
                    (x, y), textcoords="offset points", xytext=(0, -12), ha='center', fontsize=8, color='darkred')

axs[0].legend(['Bubble size ~ AI Tools'], loc='lower left', fontsize=10, frameon=True, facecolor='whitesmoke', edgecolor='darkblue')

axs[1].plot(years_experience, ai_influence_index, color='seagreen', marker='s', linestyle='--', linewidth=1.5)
axs[1].set_title("Cumulative AI Influence Index\nOver Time", fontsize=14, fontweight='normal')
axs[1].set_xlabel("Years of Experience", fontsize=13, style='italic')
axs[1].set_ylabel("AI Influence Index", fontsize=13, style='italic')
axs[1].set_xticks(years_experience[1::3])

axs[1].grid(True, linestyle=':', which='major', color='gray', alpha=0.4)

axs[1].fill_between(years_experience, ai_influence_index, color='seagreen', alpha=0.15, edgecolor='none')

plt.tight_layout()
plt.show()