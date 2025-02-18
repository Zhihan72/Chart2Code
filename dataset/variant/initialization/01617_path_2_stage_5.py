import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
enrollments = {
    "Anthropology": [300, 320, 340, 360, 380, 400, 450, 470, 480, 490, 500],
    "Sociology": [280, 290, 310, 330, 350, 370, 390, 420, 450, 460, 470],
    "History": [260, 270, 280, 300, 320, 340, 360, 370, 380, 400, 410],
}

fig, ax = plt.subplots(figsize=(16, 10))
x = np.arange(len(years))
total = np.array(enrollments["Anthropology"]) + np.array(enrollments["Sociology"]) + np.array(enrollments["History"])
antropology_pct = np.array(enrollments["Anthropology"]) / total * 100
sociology_pct = np.array(enrollments["Sociology"]) / total * 100
history_pct = np.array(enrollments["History"]) / total * 100

uniform_color = '#66b3ff'

ax.bar(x, antropology_pct, color=uniform_color, edgecolor='black', label='Anthropology')
ax.bar(x, -sociology_pct, color=uniform_color, edgecolor='black', label='Sociology')
ax.bar(x, -history_pct - sociology_pct, color=uniform_color, edgecolor='black', label='History')

ax.set_xticks(x)
ax.set_xticklabels(years)
ax.yaxis.grid(True, linestyle='-', which='major', color='blue', alpha=0.3)
ax.legend(loc='upper left')
plt.axhline(0, color='black', linewidth=0.8)
plt.tight_layout()
plt.show()