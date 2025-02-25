import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2023, 2031)
ai_exhibitors = [15, 20, 25, 30, 38, 42, 45, 48]
robotics_exhibitors = [10, 15, 22, 28, 37, 41, 44, 47]
quantum_exhibitors = [5, 8, 12, 18, 27, 32, 39, 43]
cybersecurity_exhibitors = [8, 10, 13, 17, 22, 28, 33, 36]

robotics_cumulative = np.array(ai_exhibitors) + np.array(robotics_exhibitors)
quantum_cumulative = robotics_cumulative + np.array(quantum_exhibitors)
cybersecurity_cumulative = quantum_cumulative + np.array(cybersecurity_exhibitors)

fig, ax = plt.subplots(figsize=(14, 7))

# Changed all colors to 'skyblue'
ax.bar(years, ai_exhibitors, label='AI Innovations', color='skyblue', alpha=0.8)
ax.bar(years, robotics_exhibitors, bottom=ai_exhibitors, label='Robo Advancements', color='skyblue', alpha=0.8)
ax.bar(years, quantum_exhibitors, bottom=robotics_cumulative, label='Quantum Progress', color='skyblue', alpha=0.8)
ax.bar(years, cybersecurity_exhibitors, bottom=quantum_cumulative, label='Security Protocols', color='skyblue', alpha=0.8)

ax.set_title('Tech Trends Forecast (2023-2030)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=14)
ax.set_ylabel('Participant Volume', fontsize=14)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.set_yticks(np.arange(0, 150, step=10))

plt.tight_layout()
plt.legend()
plt.show()