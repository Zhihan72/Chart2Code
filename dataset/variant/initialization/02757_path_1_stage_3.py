import matplotlib.pyplot as plt

projects = ['Mars Col.', 'Ast. Min.', 'Tel. Dev.', 'Lunar Res.', 'Exo. Disc.']
budget_allocations = [30, 25, 20, 15, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

plt.figure(figsize=(10, 8))
plt.pie(budget_allocations, 
        labels=projects, 
        colors=colors, 
        autopct='%1.1f%%',
        startangle=90)

plt.axis('equal')  
plt.show()