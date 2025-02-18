import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

apples = np.array([25, 24, 23, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 12, 12, 12, 13, 14, 15])
bananas = np.array([20, 21, 22, 23, 24, 24, 25, 25, 25, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14])
oranges = np.array([15, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 10])
grapes = np.array([10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 25, 25, 24, 23, 22])
pears = np.array([5, 5, 5, 5, 6, 6, 7, 7, 8, 9, 9, 9, 10, 10, 10, 10, 10, 10, 11, 11, 11])
pineapples = np.array([5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10])
strawberries = 100 - (apples + bananas + oranges + grapes + pears + pineapples)

fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(years, apples, bananas, oranges, grapes, pears, pineapples, strawberries, 
             labels=['Apples', 'Bananas', 'Oranges', 'Grapes', 'Pears', 'Pineapples', 'Strawberries'], 
             colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#ffe135','#ffed4f', '#c2c2f0'], alpha=0.8)

ax.set_title('Fruit Consumption Trends in Small Town (2000-2020)', fontsize=14, loc='center')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage of Total Fruit Consumption', fontsize=12)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Fruits')
ax.set_xlim(years.min(), years.max())
ax.set_ylim(0, 100)
ax.grid(True, linestyle='--', alpha=0.5)

ax.annotate('Steady Increase in Grape Consumption', xy=(2015, 21), xytext=(2010, 30),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.tight_layout()
plt.show()