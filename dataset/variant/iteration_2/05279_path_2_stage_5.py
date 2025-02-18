import matplotlib.pyplot as plt

cities = ['Chicago', 'Los Angeles', 'New York', 'Houston', 'Phoenix', 'San Diego', 'Philadelphia', 'San Antonio', 'San Jose', 'Dallas']
pizzas_sold = [190, 180, 240, 140, 160, 130, 170, 150, 165, 190]

types = ['Cheese', 'Pepperoni', 'Veggie', 'BBQ Chicken', 'Hawaiian']
type_data = {'New York': [70, 50, 45, 35, 35]}

# Change subplot from (2, 1) to (1, 2)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

bars1 = ax1.barh(cities, pizzas_sold, color='orange', edgecolor='grey', hatch='/')
bars2 = ax2.barh(types, type_data['New York'], color='blue', edgecolor='darkred', hatch='*')

ax1.set_title('Pizza Sales in US Cities - April', fontsize=16, fontweight='semibold')
ax1.set_xlabel('Pizzas Sold', fontsize=13, labelpad=10)
ax1.set_ylabel('Americas Cities', fontsize=13, labelpad=10)

ax2.set_title('Favorite Pizza Types in NYC', fontsize=16, fontweight='semibold')
ax2.set_xlabel('Count of Pizzas', fontsize=13, labelpad=10)
ax2.set_ylabel('Pizza Types', fontsize=13, labelpad=10)

ax1.xaxis.grid(True, linestyle=':', alpha=0.5)
ax2.xaxis.grid(True, linestyle='-.', alpha=0.5)

ax1.spines['top'].set_linewidth(1.5)
ax1.spines['right'].set_visible(False)
ax2.spines['left'].set_color('green')
ax2.spines['left'].set_linewidth(1.5)
ax2.spines['bottom'].set_color('purple')
ax2.spines['bottom'].set_linewidth(1.5)

plt.tight_layout(pad=3.0)
plt.show()