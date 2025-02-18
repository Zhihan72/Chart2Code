import matplotlib.pyplot as plt

departments = ['R&D', 'Marketing', 'Sales', 'IT']
expenditure = [45, 20, 15, 7]  # in millions
colors = ['#FF9999', '#66B2FF', '#99FF99', '#CC99FF']
explode = (0.1, 0, 0, 0)

fig, ax1 = plt.subplots(figsize=(8, 8))

wedges, texts, autotexts = ax1.pie(
    expenditure, explode=explode, labels=departments, colors=colors, autopct='%1.1f%%',
    startangle=140, shadow=True, wedgeprops=dict(edgecolor='black', linewidth=1.5), radius=1.2)

# Add a circle at the center to transform the pie chart into a donut chart
centre_circle = plt.Circle((0,0),0.8,fc='white')
fig.gca().add_artist(centre_circle)

plt.setp(autotexts, size=10, weight="bold", color="black")

ax1.set_title('2023 Operating Expenditure by Department (in Millions)', fontsize=14, fontweight='bold', pad=20)
ax1.legend(title='Departments', loc='upper right', bbox_to_anchor=(1.3, 0.8), shadow=True, fontsize=10)

plt.tight_layout()

plt.show()