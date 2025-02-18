import matplotlib.pyplot as plt

departments = ['Software Dev', 'Product Management', 'Marketing', 'Sales', 'HR']
num_employees = [50, 30, 20, 40, 25]
colors = ['lightblue', 'peachpuff', 'lightgreen', 'lightsalmon', 'thistle']

# Combine data pairs of (num_employees, department, color) for sorting
sorted_data = sorted(zip(num_employees, departments, colors), key=lambda x: x[0])

# Unpack the sorted data
sorted_num_employees, sorted_departments, sorted_colors = zip(*sorted_data)

# Create a sorted bar chart
plt.figure(figsize=(10, 5))
plt.bar(sorted_departments, sorted_num_employees, color=sorted_colors)
plt.xlabel('Departments')
plt.ylabel('Number of Employees')
plt.title('Sorted Bar Chart of Number of Employees by Department')
plt.tight_layout()
plt.show()