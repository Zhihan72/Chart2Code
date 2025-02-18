import matplotlib.pyplot as plt
import numpy as np

departments = np.array(['Sales', 'R&D', 'Customer Support'])

sales_total = np.mean([90, 89, 91, 88, 92, 85, 94, 85, 96, 93, 90, 95])
rnd_total = np.mean([86, 89, 88, 87, 82, 80, 85, 78, 90, 83, 81, 86])
cust_support_total = np.mean([75, 81, 70, 79, 82, 85, 78, 84, 80, 77, 83, 73])

performance_scores = np.array([sales_total, rnd_total, cust_support_total])

sales_avg_error = np.mean([4, 2, 3, 1, 2, 2, 3, 3, 1, 2, 3, 2])
rnd_avg_error = np.mean([3, 1, 4, 2, 3, 3, 2, 3, 1, 2, 2, 2])
cust_support_avg_error = np.mean([3, 2, 4, 2, 3, 1, 5, 2, 2, 3, 2, 4])

performance_errors = np.array([sales_avg_error, rnd_avg_error, cust_support_avg_error])

plt.figure(figsize=(10, 6))
plt.barh(departments, performance_scores, xerr=performance_errors, 
         color=['darkorange', 'royalblue', 'mediumseagreen'], edgecolor='gray', alpha=0.8, capsize=5)

plt.xticks([])
plt.yticks([])
plt.box(False)

plt.tight_layout()
plt.show()