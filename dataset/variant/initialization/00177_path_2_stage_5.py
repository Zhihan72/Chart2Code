import numpy as np
import matplotlib.pyplot as plt

agencies = ['NASA', 'ESA', 'Roscosmos', 'ISRO']

success_rates = np.array([
    [85, 90, 95],  # NASA
    [75, 85, 88],  # ESA
    [80, 83, 89],  # Roscosmos
    [70, 78, 85]   # ISRO
])

average_success_rates = np.mean(success_rates, axis=1)
sorted_indices = np.argsort(average_success_rates)[::-1]

sorted_agencies = np.array(agencies)[sorted_indices]
sorted_success_rates = average_success_rates[sorted_indices]

color_list = ['royalblue', 'deepskyblue', 'navy', 'dodgerblue']
line_styles = ['-', '--', '-.', ':']
shuffled_colors = np.array(color_list)[sorted_indices]
marker_types = ['o', 's', '^', 'D']

plt.figure(figsize=(10, 6))
for i, agency in enumerate(sorted_agencies):
    plt.bar(agency, sorted_success_rates[i], color=shuffled_colors[i], alpha=0.7, 
            edgecolor='black', linestyle=line_styles[i % len(line_styles)], 
            hatch=marker_types[i % len(marker_types)])

plt.xlabel('Agencies', fontsize=10, weight='light')
plt.ylabel('Avg Success %', fontsize=10, style='italic')
plt.title("Sorted Avg Space Mission Success (2010-2020)", fontsize=14,
          weight='bold', style='italic')

plt.ylim(0, 100)
plt.grid(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_color('blue')
plt.gca().spines['bottom'].set_linewidth(2.0)

plt.tight_layout()
plt.show()