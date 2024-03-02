import matplotlib.pyplot as plt

boys = 15
girls = 17

fig = plt.figure()

plt.text(1.2, 1, f"Всего детей: {boys+girls}", fontsize=10, ha="left")

labels = ["Boys", "Girls"]
sizes = [boys, girls]
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.show()
