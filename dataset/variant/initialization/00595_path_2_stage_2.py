import matplotlib.pyplot as plt
import numpy as np

# Skills of various characters
skills = ['Bravery', 'Focus', 'Wisdom', 'Agility', 'Ingenuity', 'Charm']
num_skills = len(skills)

# Skills scores
knight_skills = [9, 4, 3, 2, 5, 8]
archer_skills = [5, 9, 4, 8, 5, 6]
mage_skills = [2, 3, 10, 4, 7, 5]

# Define angles for plotting
angles = np.linspace(0, 2 * np.pi, num_skills, endpoint=False).tolist()
knight_skills += knight_skills[:1]
archer_skills += archer_skills[:1]
mage_skills += mage_skills[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
fig.patch.set_facecolor('#ffffff')

# Define gridlines
ax.grid(color='black', linestyle='-', linewidth=1)

# Plot each character's skills
ax.fill(angles, knight_skills, color='tab:red', alpha=0.3)
ax.plot(angles, knight_skills, color='tab:red', linewidth=1, linestyle='solid', marker='o', label='Warrior')

ax.fill(angles, archer_skills, color='tab:green', alpha=0.3)
ax.plot(angles, archer_skills, color='tab:green', linewidth=1, linestyle='solid', marker='s', label='Sharpshooter')

ax.fill(angles, mage_skills, color='tab:blue', alpha=0.3)
ax.plot(angles, mage_skills, color='tab:blue', linewidth=1, linestyle='solid', marker='^', label='Sorcerer')

# Customize axis labels and title
ax.set_yticklabels(['Weak', '', '', 'Average', '', '', 'Strong'], fontsize=10, color='black')
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, fontsize=12, color='darkgreen')

# Annotate a specific skill
ax.annotate('Peak Wisdom', xy=(angles[2], mage_skills[2]), xytext=(angles[2], mage_skills[2] + 2),
            arrowprops=dict(facecolor='teal', shrink=0.05), fontsize=11, color='teal')

# Set chart title and legend
ax.set_title('Skills of Champions in Mystica', fontsize=16, fontweight='bold', color='darkorange', pad=20)
ax.legend(loc='lower left', bbox_to_anchor=(-0.2, 0.15), frameon=True, fontsize=12)

plt.tight_layout()
plt.show()