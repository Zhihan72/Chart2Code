import matplotlib.pyplot as plt
import numpy as np

years_experience = np.array([1, 3, 5, 7, 10, 12, 15, 18, 20, 25, 30, 35, 40])
ai_adoption_rate = np.array([70, 65, 60, 55, 50, 52, 48, 45, 42, 40, 38, 35, 30])
data_science_adoption_rate = np.array([60, 58, 57, 53, 50, 49, 48, 46, 44, 43, 42, 41, 40])
number_of_tools = np.array([5, 4, 4, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1]) * 10

ai_influence_index = np.array([5, 15, 28, 40, 60, 75, 90, 110, 130, 160, 200, 240, 280])
data_science_influence_index = np.array([10, 18, 30, 45, 65, 80, 95, 115, 135, 165, 205, 245, 285])

fig, axs = plt.subplots(2, 1, figsize=(10, 12))

axs[0].scatter(years_experience, ai_adoption_rate, s=number_of_tools, c='teal', alpha=0.7, edgecolors='w', linewidth=2)
axs[0].scatter(years_experience, data_science_adoption_rate, s=number_of_tools, c='orange', alpha=0.7, edgecolors='w', linewidth=2)
axs[0].set_xlabel("Years", fontsize=12)
axs[0].set_ylabel("Adoption Rate (%)", fontsize=12)
axs[0].set_xticks(years_experience)
axs[0].tick_params(axis='x', rotation=45)
axs[0].set_yticks(np.arange(25, 80, 5))

for i, (x, y) in enumerate(zip(years_experience, ai_adoption_rate)):
    axs[0].annotate(f'{number_of_tools[i]//10}', (x, y), textcoords="offset points", xytext=(0, -10), ha='center', fontsize=9)

for i, (x, y) in enumerate(zip(years_experience, data_science_adoption_rate)):
    axs[0].annotate(f'{number_of_tools[i]//10}', (x, y), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, color='orange')

axs[1].plot(years_experience, ai_influence_index, color='purple', marker='o', linestyle='-')
axs[1].plot(years_experience, data_science_influence_index, color='green', marker='s', linestyle='--')
axs[1].set_xlabel("Years", fontsize=12)
axs[1].set_ylabel("Influence Index", fontsize=12)
axs[1].set_xticks(years_experience)
axs[1].tick_params(axis='x', rotation=45)
axs[1].fill_between(years_experience, ai_influence_index, color='purple', alpha=0.1)
axs[1].fill_between(years_experience, data_science_influence_index, color='green', alpha=0.1)

plt.tight_layout()
plt.show()