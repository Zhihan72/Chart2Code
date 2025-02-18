import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 8)

software_dev = np.array([84, 88, 85, 80, 83, 84, 90])
marketing = np.array([66, 60, 62, 62, 61, 65, 60])
sales = np.array([55, 53, 50, 54, 58, 56, 55])
hr = np.array([31, 33, 32, 30, 34, 32, 30])
customer_support = np.array([75, 73, 70, 74, 76, 77, 72])

data = np.vstack([software_dev, marketing, sales, hr, customer_support])

fig, ax = plt.subplots(figsize=(14, 7))

ax.stackplot(days, data, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'], alpha=0.8)
ax.set_xticks(days)

plt.tight_layout()
plt.show()