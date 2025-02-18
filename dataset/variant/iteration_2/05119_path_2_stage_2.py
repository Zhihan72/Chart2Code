import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2023, 2031)
categories = ['Artificial Intelligence', 'Robotics', 'Quantum Computing', 'Cybersecurity']

ai_exhibitors = [15, 20, 25, 30, 38, 42, 45, 48]
robotics_exhibitors = [10, 15, 22, 28, 37, 41, 44, 47]
quantum_exhibitors = [5, 8, 12, 18, 27, 32, 39, 43]
cybersecurity_exhibitors = [8, 10, 13, 17, 22, 28, 33, 36]

robotics_cumulative = np.array(ai_exhibitors) + np.array(robotics_exhibitors)
quantum_cumulative = robotics_cumulative + np.array(quantum_exhibitors)
cybersecurity_cumulative = quantum_cumulative + np.array(cybersecurity_exhibitors)

fig, ax = plt.subplots(figsize=(14, 7))

ax.bar(years, ai_exhibitors, color='skyblue', alpha=0.8)
ax.bar(years, robotics_exhibitors, bottom=ai_exhibitors, color='lightgreen', alpha=0.8)
ax.bar(years, quantum_exhibitors, bottom=robotics_cumulative, color='salmon', alpha=0.8)
ax.bar(years, cybersecurity_exhibitors, bottom=quantum_cumulative, color='gold', alpha=0.8)

ax.set_title('Exhibitor Trends in Techville’s Annual Showcase (2023-2030)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Exhibitors', fontsize=14)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.set_yticks(np.arange(0, 150, step=10))

plt.tight_layout()
plt.show()