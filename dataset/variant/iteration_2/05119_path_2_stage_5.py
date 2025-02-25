import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2023, 2031)
ai_exhibitors = [15, 20, 25, 30, 38, 42, 45, 48]
robotics_exhibitors = [10, 15, 22, 28, 37, 41, 44, 47]
quantum_exhibitors = [-5, -8, -12, -18, -27, -32, -39, -43]
cybersecurity_exhibitors = [-8, -10, -13, -17, -22, -28, -33, -36]

fig, ax = plt.subplots(figsize=(14, 7))

ax.bar(years, ai_exhibitors, label='AI Innovations', color='skyblue', alpha=0.8)
ax.bar(years, robotics_exhibitors, bottom=ai_exhibitors, label='Robo Advancements', color='lightgreen', alpha=0.8)
ax.bar(years, quantum_exhibitors, label='Quantum Progress', color='salmon', alpha=0.8)
ax.bar(years, cybersecurity_exhibitors, bottom=quantum_exhibitors, label='Security Protocols', color='orange', alpha=0.8)

ax.set_title('Tech Trends Forecast (2023-2030)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=14)
ax.set_ylabel('Participant Volume', fontsize=14)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.set_yticks(np.arange(-100, 100, step=10))

plt.tight_layout()
plt.legend(loc='upper left')
plt.axhline(0, color='black', linewidth=0.8)  # Central axis line
plt.show()