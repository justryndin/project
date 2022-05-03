class MyClass:
    name = "Класс MyClass"

    def set(self, n):
        self.nickname = n

    def get(self):
        print(f"Значение поля: {self.nickname}")

    def __init__(self, n):
        self.set(n)
        print("Экзепляр класса создан!")
        self.get()


green = MyClass("Зеленый")
print("Принадлежность", green.name)
red = MyClass("Красный")
print("Принадлежность", red.name)
MyClass.name = "Здесь могла быть ваша реклама"
print("Спрашивает Красный", red.name)
print("Спрашивает Зеленый", green.name)
