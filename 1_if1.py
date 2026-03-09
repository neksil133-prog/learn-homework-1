age = int(input("Введите ваш возраст: "))
def what_to_do(age):
        if age < 7:
         return "Вы будете ходить в детский сад."     
        elif age < 18:
             return "Вы будете учиться в школе."
        elif age < 24:
            return "Вы будете работать."
        else:
            return "Вам нужно работать."
result = what_to_do(age)
print(result)  


