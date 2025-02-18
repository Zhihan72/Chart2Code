import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])

endurance_scores = [50, 60, 55, 70, 65, 80]
strength_scores = [40, 50, 60, 55, 65, 75]
flexibility_scores = [30, 40, 50, 45, 55, 65]
speed_scores = [45, 55, 65, 60, 70, 85]       # New data series
balance_scores = [35, 45, 55, 50, 60, 70]     # New data series

x = np.arange(len(months))

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(months, endurance_scores, marker='x', markersize=8, linewidth=2.5, 
         linestyle='-', color='teal', label='Stamina')

ax1.plot(months, strength_scores, marker='^', markersize=8, linewidth=2.5, 
         linestyle=':', color='orange', label='Power')

ax1.plot(months, flexibility_scores, marker='v', markersize=8, linewidth=2.5, 
         linestyle='--', color='purple', label='Agility')

ax1.plot(months, speed_scores, marker='o', markersize=8, linewidth=2.5, 
         linestyle='-.', color='red', label='Speed')  # New plot for Speed

ax1.plot(months, balance_scores, marker='s', markersize=8, linewidth=2.5, 
         linestyle='-', color='blue', label='Balance') # New plot for Balance

ax1.set_title("Six-Month Fitness Journey", fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel("Training Months", fontsize=14, labelpad=15)
ax1.set_ylabel("Scores on Average", fontsize=14, labelpad=15)

ax1.legend(title="Test Areas", title_fontsize='13', fontsize='12', loc='lower right')

ax1.grid(True, linestyle=':', linewidth=1, alpha=0.3)

# Annotations for the existing data
max_endurance = max(endurance_scores)
max_idx = endurance_scores.index(max_endurance)
ax1.annotate(f'Max: {max_endurance}', xy=(x[max_idx], max_endurance), xytext=(x[max_idx], max_endurance+10),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, color='teal')

max_strength = max(strength_scores)
max_idx = strength_scores.index(max_strength)
ax1.annotate(f'Max: {max_strength}', xy=(x[max_idx], max_strength), xytext=(x[max_idx], max_strength+10),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, color='orange')

max_flexibility = max(flexibility_scores)
max_idx = flexibility_scores.index(max_flexibility)
ax1.annotate(f'Max: {max_flexibility}', xy=(x[max_idx], max_flexibility), xytext=(x[max_idx], max_flexibility+10),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, color='purple')

# Annotations for the new data
max_speed = max(speed_scores)
max_idx = speed_scores.index(max_speed)
ax1.annotate(f'Max: {max_speed}', xy=(x[max_idx], max_speed), xytext=(x[max_idx], max_speed+10),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, color='red')

max_balance = max(balance_scores)
max_idx = balance_scores.index(max_balance)
ax1.annotate(f'Max: {max_balance}', xy=(x[max_idx], max_balance), xytext=(x[max_idx], max_balance+10),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, color='blue')

plt.tight_layout()

plt.show()