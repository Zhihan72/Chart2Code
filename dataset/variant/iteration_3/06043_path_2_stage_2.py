import matplotlib.pyplot as plt
import numpy as np

departments = ['Software Development', 'Marketing', 'Sales', 'Human Resources', 'Customer Support']
days = np.arange(1, 8)

software_dev = np.array([80, 85, 83, 90, 88, 85, 84])
marketing = np.array([60, 62, 61, 65, 66, 62, 60])
sales = np.array([50, 55, 53, 58, 56, 54, 55])
hr = np.array([30, 32, 31, 34, 33, 32, 30])
customer_support = np.array([70, 72, 75, 77, 76, 74, 73])

data = np.vstack([software_dev, marketing, sales, hr, customer_support])

fig, ax = plt.subplots(figsize=(14, 7))

ax.stackplot(days, data, colors=['#4e79a7', '#f28e2b', '#76b7b2', '#59a14f', '#edc948'], alpha=0.8)
ax.set_xticks(days)
ax.grid(True, linestyle='--', linewidth=0.5)

plt.tight_layout()

plt.show()