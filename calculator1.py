def plus(a, b):
    return a + b

def minus(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b, result):
    try:
        result_function = a / b
    except:
        print('Ошибка')
        return result
    return result_function

def pow(a,b):
    return a**b

infinity = 0
result = 0
trust_operation = False
while infinity != 1:
    print('Калькулятор')
    while True:
        try:
            first_number = float(input('Введите первое число: '))
            trust_operation = True
        except:
            print('Ошибка')
        if trust_operation == True:
            break
    trust_operation = False
    while True:
        try:
            second_number = float(input('Введите второе число: '))
            trust_operation = True
        except:
            print('Ошибка')
        if trust_operation == True:
            break
    while True:
        choosen_operation = input('Выберите операцию (+,-,/,*,^): ')
        match choosen_operation:
            case '+':
                result = plus(first_number, second_number)
                break
            case '-':
                result = minus(first_number, second_number)
                break
            case '*':
                result = multi(first_number, second_number)
                break
            case '/':
                result = div(first_number, second_number, result)
                break
            case '^':
                result = pow(first_number, second_number)
                break
            case _:
                print('Ошибка, такой операции нету!')
    print(f"Ответ: {result}")
    count_operation = float(input('Введите количество операций: '))
    count_operation += 1
    i = 2
    while i <= count_operation:
        second_number = float(input('Введите второе число: '))
        while True:
            choosen_operation = input('Выберите операцию (+,-,/,*,^): ')
            match choosen_operation:
                case '+':
                    result = plus(result, second_number)
                    break
                case '-':
                    result = minus(result, second_number)
                    break
                case '*':
                    result = multi(result, second_number)
                    break
                case '/':
                    result = div(result, second_number, result)
                    break
                case '^':
                    result = pow(result, second_number)
                    break
                case _:
                    print('Ошибка, такой операции нету!')
        print(f'Ответ {i} операции: {result}')
        i += 1
    infinity = int(input('Введите любое число, чтобы продолжить или 1, чтобы завершить программу: '))