import matplotlib.pyplot as plt

budget_allocations = [25, 15, 30, 20, 10]
projects = ['Mars Col.', 'Ast. Min.', 'Tel. Dev.', 'Lunar Res.', 'Exo. Disc.']
single_color = '#66b3ff'  # Chose one color from the original list

plt.figure(figsize=(10, 8))
plt.pie(budget_allocations, 
        labels=projects, 
        colors=[single_color] * len(budget_allocations),  # Use the single color for all slices
        autopct='%1.1f%%',
        startangle=90)

plt.axis('equal')
plt.show()