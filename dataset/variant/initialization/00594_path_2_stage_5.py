import matplotlib.pyplot as plt
import numpy as np

num_skills = 6

knight_skills = [3, 9, 8, 5, 4, 2] 
archer_skills = [6, 4, 5, 5, 8, 9]
mage_skills = [7, 5, 2, 3, 4, 10]

angles = np.linspace(0, 2 * np.pi, num_skills, endpoint=False).tolist()

knight_skills += knight_skills[:1]
archer_skills += archer_skills[:1]
mage_skills += mage_skills[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Fill and plot for knight
ax.fill(angles, knight_skills, color='tab:blue', alpha=0.25)
ax.plot(angles, knight_skills, color='tab:blue', linewidth=1.5)

# Fill and plot for archer
ax.fill(angles, archer_skills, color='tab:red', alpha=0.25)
ax.plot(angles, archer_skills, color='tab:red', linewidth=1.5)

# Fill and plot for mage
ax.fill(angles, mage_skills, color='tab:green', alpha=0.25)
ax.plot(angles, mage_skills, color='tab:green', linewidth=1.5)

ax.set_yticklabels([])
ax.set_xticks([])

plt.show()