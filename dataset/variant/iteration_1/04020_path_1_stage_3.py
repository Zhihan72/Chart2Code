import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2023, 2029)
math_engagement = np.array([70, 72, 75, 78, 80, 82])
science_engagement = np.array([65, 67, 70, 73, 75, 78])
literature_engagement = np.array([55, 58, 60, 62, 65, 67])

fig, ax = plt.subplots(figsize=(12, 6))

# Applying a single color consistently across all data groups
consistent_color = '#1f77b4'

ax.plot(years, math_engagement, marker='v', linestyle='--', color=consistent_color, label='Math')
ax.plot(years, science_engagement, marker='x', linestyle='-', color=consistent_color, label='Science')
ax.plot(years, literature_engagement, marker='D', linestyle=':', color=consistent_color, label='Literature')

ax.set_title("Virtual Learning Engagement in Schools (2023-2028)\nMonitoring Student Engagement in Various Subjects", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Student Engagement (%)", fontsize=14)

ax.legend(title="Subjects", loc='upper left', fontsize=12, frameon=True, shadow=True)
ax.grid(True, linestyle='-', alpha=0.3)

ax.spines['top'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)

plt.tight_layout()
plt.show()