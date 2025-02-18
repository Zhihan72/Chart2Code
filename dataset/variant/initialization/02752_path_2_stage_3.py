import matplotlib.pyplot as plt

user_percentages = [22, 18, 25, 15, 10, 10]

# New set of colors
colors = ['#FF5733', '#33FFBD', '#335BFF', '#F5FF33', '#9333FF', '#FF3380']

plt.figure(figsize=(10, 7))
plt.pie(
    user_percentages,
    colors=colors,
    startangle=140,
    autopct='%1.1f%%'
)

plt.axis('equal')
plt.tight_layout()
plt.show()