import matplotlib.pyplot as plt

# Data for alien cuisines preferences
cuisines = ['Zorg Tacos', 'Nebula Noodles', 'Cosmic Pizza', 'Stellar Sushi', 'Galactic Burgers', 'Meteoric Stew']
percentages = [25, 18, 20, 10, 12, 8]

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(10, 10))
ax.pie(
    percentages,
    startangle=90,
    labels=cuisines,
    autopct='%1.1f%%',
    explode=[0.05]*len(cuisines)
)

plt.show()