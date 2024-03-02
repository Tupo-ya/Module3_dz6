import matplotlib.pyplot as plt

grades = [2, 3, 3, 2, 5, 5, 3, 4, 5, 4]
plt.hist(grades)

plt.xlabel("Оценки")
plt.ylabel("% учеников")
plt.title("Распределение оценок учеников")

plt.show()
