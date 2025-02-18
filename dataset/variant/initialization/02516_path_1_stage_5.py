import matplotlib.pyplot as plt
import numpy as np

proficiency_healthcare = [6, 5, 8, 7, 9, 7]
proficiency_finance = [8, 9, 7, 7, 6, 8]
proficiency_technology = [8, 6, 7, 9, 9, 8]

proficiency_projection_2030 = {
    'Healthcare': [8, 9, 8, 7, 6, 9],
    'Finance': [7, 8, 9, 9, 8, 9],
    'Technology': [9, 7, 9, 9, 8, 9]
}

num_vars = len(proficiency_healthcare)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

proficiency_healthcare += proficiency_healthcare[:1]
proficiency_finance += proficiency_finance[:1]
proficiency_technology += proficiency_technology[:1]
angles += angles[:1]

single_color = '#1f77b4'

fig, axs = plt.subplots(1, 2, figsize=(16, 8))

ax = axs[0]
ax.plot(angles, proficiency_healthcare, linewidth=2, linestyle='solid', color=single_color)
ax.fill(angles, proficiency_healthcare, alpha=0.25, color=single_color)
ax.plot(angles, proficiency_finance, linewidth=2, linestyle='solid', color=single_color)
ax.fill(angles, proficiency_finance, alpha=0.25, color=single_color)
ax.plot(angles, proficiency_technology, linewidth=2, linestyle='solid', color=single_color)
ax.fill(angles, proficiency_technology, alpha=0.25, color=single_color)
ax.set_yticklabels([])
ax.set_xticks([])
ax.set_yticks([])

ax2 = axs[1]
height = 0.2  
y = np.arange(num_vars)

ax2.barh(y - height, proficiency_projection_2030['Healthcare'], height, color=single_color)
ax2.barh(y, proficiency_projection_2030['Finance'], height, color=single_color)
ax2.barh(y + height, proficiency_projection_2030['Technology'], height, color=single_color)

ax2.set_yticks([])
ax2.set_xticks([])

plt.tight_layout()
plt.show()