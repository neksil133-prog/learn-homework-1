"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    """
    Замените pass на ваш код
    """
answer = ""
while answer != "Хорошо":
        try:
            answer = input("Как дела? ")
            if answer == "Хорошо":
                print("Я рад, что всё хорошо")
        except KeyboardInterrupt:
            print("\nПока!")
            break
    
if __name__ == "__main__":
    hello_user()
