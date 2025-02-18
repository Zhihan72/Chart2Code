import matplotlib.pyplot as plt

# The content within the data groups 'budget_allocations' is randomly altered
budget_allocations = [25, 15, 30, 20, 10]

projects = ['Mars Col.', 'Ast. Min.', 'Tel. Dev.', 'Lunar Res.', 'Exo. Disc.']
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

plt.figure(figsize=(10, 8))
plt.pie(budget_allocations, 
        labels=projects, 
        colors=colors, 
        autopct='%1.1f%%',
        startangle=90)

plt.axis('equal')
plt.show()