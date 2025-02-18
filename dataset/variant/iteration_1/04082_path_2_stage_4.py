import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

interest_coding = np.array([6, 7, 8, 8, 9, 9, 7, 6, 7, 8, 8, 9])
interest_cooking = np.array([5, 6, 6, 8, 9, 9, 8, 7, 6, 6, 7, 8])
interest_hiking = np.array([7, 6, 7, 9, 10, 9, 8, 7, 7, 7, 6, 7])
interest_reading = np.array([8, 8, 9, 9, 10, 10, 8, 8, 9, 10, 10, 9])

interest_data = {
    'Coding': interest_coding,
    'Cooking': interest_cooking,
    'Hiking': interest_hiking,
    'Reading': interest_reading
}

colors = {
    'Coding': 'red',
    'Cooking': 'purple',
    'Hiking': 'green',
    'Reading': 'orange'
}

fig, ax = plt.subplots(figsize=(14, 7))
for hobby, interest in interest_data.items():
    ax.plot(months, interest, marker='o', color=colors[hobby], linewidth=2, linestyle='-')

ax.set_xticks(months)
ax.set_yticks(np.arange(0, 11, 1))

plt.tight_layout()
plt.show()