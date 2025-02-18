import matplotlib.pyplot as plt

# Define the data
transport_modes = ["Bicycles", "Cars", "Walking", "Motorcycles", "Public Transport", "Others"]
percentages = [25, 20, 30, 10, 10, 5]

# Single color for all transport modes
single_color = ['#66b3ff']

# Create pie chart
fig, ax = plt.subplots(figsize=(10, 7))

# Creating the pie chart with a single color
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=transport_modes,
    autopct='%1.1f%%',
    startangle=90,
    colors=single_color * len(transport_modes)
)

# Ensure each label and percentage is properly displayed
for text in texts:
    text.set_size(10)

for autotext in autotexts:
    autotext.set_size(10)
    autotext.set_color('darkgrey')

# Display the pie chart
plt.show()