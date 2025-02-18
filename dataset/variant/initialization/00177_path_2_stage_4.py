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

# Rearrange the colors such that they are shuffled, here we use a manual shuffle
color_list = ['deepskyblue', 'navy', 'dodgerblue', 'royalblue']
shuffled_colors = np.array(color_list)[sorted_indices]

plt.figure(figsize=(10, 6))
plt.bar(sorted_agencies, sorted_success_rates, color=shuffled_colors, alpha=0.7)

plt.xlabel('Agencies', fontsize=10)
plt.ylabel('Average Success %', fontsize=10)
plt.title("Sorted Average Space Mission Success (2010-2020)", fontsize=14, weight='bold')
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', linewidth=0.5, color='gray')
plt.tight_layout()
plt.show()