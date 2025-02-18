import matplotlib.pyplot as plt

percentages = [25, 20, 18, 15, 12, 7]

fig, ax = plt.subplots(figsize=(10, 8))

# Standard pie chart without a hole in the center
ax.pie(percentages, startangle=140, colors=['#66B3FF']*len(percentages), explode=(0.05, 0.05, 0, 0, 0, 0))

plt.axis('equal')
plt.tight_layout()

plt.show()