import matplotlib.pyplot as plt

# Percentages of alien cuisines preferences
percentages = [25, 18, 20, 10, 12, 8]

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(10, 10))
ax.pie(
    percentages,
    startangle=90,
    explode=[0.05]*len(percentages)
)

plt.show()