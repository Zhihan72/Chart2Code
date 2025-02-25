import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Dec', 'Jul', 'Sep', 'Oct', 'Mar', 'Feb'])
endurance_scores = [60, 65, 55, 80, 50, 70]
strength_scores = [65, 50, 75, 40, 55, 60]
flexibility_scores = [55, 45, 65, 40, 30, 50]

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(months, endurance_scores, marker='x', markersize=7, linewidth=1, 
         linestyle='-', color='skyblue', label='Stamina')

ax1.plot(months, strength_scores, marker='s', markersize=6, linewidth=2, 
         linestyle='-', color='orangered', label='Force')

ax1.plot(months, flexibility_scores, marker='D', markersize=6, linewidth=1, 
         linestyle=':', color='limegreen', label='Elasticity')

ax1.set_title("Six-Month Assessment of Capabilities", fontsize=18, fontweight='normal', pad=20)
ax1.set_xlabel("Time Period", fontsize=14, labelpad=15)
ax1.set_ylabel("Evaluation Scores", fontsize=14, labelpad=15)

ax1.legend(title="Examination Categories", title_fontsize='13', fontsize='12', loc='lower right')
ax1.grid(True, linestyle='-', linewidth=0.8, alpha=0.5)

ax1.xaxis.set_ticks(np.arange(len(months)))
ax1.xaxis.set_ticklabels(months, rotation=45, ha='right', fontsize=12)
ax1.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

plt.tight_layout()
plt.show()