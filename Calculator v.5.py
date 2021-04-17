#Простой калькулятор v.05
#by Petukhov Nikita 
#supported by Davydov Nikita

from enum import Enum

# Определим возможные действия в нашей проге
class Actions(Enum):
    Exit = 0 # при этом выборе выходим из программы
    SelectOperation = 1 # Выбор операции (после каждой программы возращаемся сюда)
    Calc = 2 # показываем калькулятор
    IMT = 3  # показываем вычисление ИМТ
    Sqr = 4  # показываем вычисление квадратного корня


print("Здравствуйте!")

# По-умолчанию выбираем действие - показать основное меню
action = Actions.SelectOperation

# основной цикл программы - как только выберут Exit, программа завершит цикл
while action != Actions.Exit:
    
    # Показываем основное меню
    if action == Actions.SelectOperation:
        operation = input("\nДоступные действия:\n1)Калькулятор(+,-,*,/);\n2)Определитель ИМТ;\n3)Решение квадратных уравнений;\n4)Выход;\n\nВыберите дальнейшее действие(1,2,3,4):")
        
        # выбираем тип операции - Калькулятор\ИМТ\Квадратный корень или неправильная операция
        if operation == "1":
            action = Actions.Calc
        elif operation == "2":
            action = Actions.IMT
        elif operation == "3":
            action = Actions.Sqr
        elif operation == "4":
            action = Actions.Exit
        else:
            action = Actions.SelectOperation
            print("Неправильная операция. Попробуйте снова!")
            
        # возращаемся в основной цикл while 
        continue

    elif action == Actions.Calc:
        what = input("Это Калькулятор: \nЧто будем делать?(+,-,*,/):")

        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        
        if what == "+":
            c = a + b
            print("Результат: " + str(c))
        elif what == "-":
            c = a - b
            print("Результат: " + str(c))

        elif what == "*":
            c = a * b
            print("Результат: " + str(c))

        elif what == "/":
            c = a / b
            print("Результат: " + str(c))

        else:
            print("Выбрана неверная операция!")
            
        input("Чтобы продолжить, нажмите ENTER")
        
        # возращаемся в основной цикл while и будем показывать основное меню
        action = Actions.SelectOperation
        continue

    elif action == Actions.IMT:
        w = float(input("\nВведите ваш вес(целое число в килограммах):"))
        h = float(input("Введите ваш рост(в сантиметрах):"))
        s = h /100
        imt = w / s**2
        imt = round(imt)
        
        if imt < 18:
             print("Ваш ИМТ равен: " + str(imt) + " кг/м²!" + "Вы страдаете дефицитом массы тела, поэтому Вам следует больше питаться.")
        elif imt > 30:
             print("Ваш ИМТ равен: " + str(imt) + " кг/м²!" + " У Вас есть избыточная масса тела, поэтому Вам следует обратиться к диетологу.")
        else :
             print("Ваш ИМТ равен: " + str(imt) + " кг/м²!" + " У Вас нормальное телосложение.")
        print("Результат вычисления массы тела помогает оценить степень соответствия массы человека и его роста и тем самым КОСВЕННО судить о том, является ли масса недостаточной, нормальной или избыточной.")
        
        input("Чтобы продолжить, нажмите ENTER")

        # возращаемся в основной цикл while и будем показывать основное меню
        action = Actions.SelectOperation
        continue
    
    elif action == Actions.Sqr:
        print("\nКвадратное уравнение вида: ax²+bx+c=0") 
        vA = float(input("Введите a:"))
        vB = float(input("Введите b:"))
        vC = float(input("Введите c:"))
        discr = ((vB)**2)- 4 * (vA) * (vC)

        if discr < 0:
            print("Уравнение " + str(vA) + "x²+" + "(" + str(vB) + ")" + "x+" + "(" + str(vC) + ")" + " = 0" + " не имеет действительных корней, т.к. дискриминант меньше нуля.")

        elif discr == 0:
            vX0 = -((vB) / 2*(vA))
            print("Уравнение " + str(vA) + "x²+" + "(" + str(vB) + ")" + "x+" + "(" + str(vC) + ")" + " = 0" + " имеет один корень, т.к. дискриминант равен нулю.")
            print("Результат: x=" + str(vX0))

        elif discr > 0:
            from math import sqrt
            ndis = sqrt(discr)
            vX1=(-(vB) + (ndis)) / (2 * (vA))
            vX2=(-(vB) - (ndis)) / (2 * (vA))
            print("Уравнение " + str(vA) + "x²+" + "(" + str(vB)+ ")" + "x+" + "(" + str(vC) + ")" + " = 0" + " имеет два корня, т.к. дискриминант больше нуля.")
            print("Результат: x1=" + str(vX1) + "; x2=" + str(vX2))

        input("Чтобы продолжить, нажмите ENTER")

        # возращаемся в основной цикл while и будем показывать основное меню
        action = Actions.SelectOperation
        continue
    
input("Нажмите ENTER, чтобы выйти")
