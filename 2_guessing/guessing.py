a = input('Введите нижнюю границу для региона: ')
b = input('Введите верхнюю границу для региона: ')
if a < b:
    
    number = int(input(f'Выбери одно число от {a} до {b} ' ))
        
    while True:
        midnumber = int(((b - a)/2)+ a)
        guess = input(f'Твоё число [>], [<] или [=]  {midnumber} ')
            
        if guess == ">":
            a = midnumber
            continue
            
        elif guess == "<":
            b = midnumber
            continue    

        elif guess == "=":
            print(f'Твое число это {midnumber}')
            break
        elif guess == "exit":
            break
else:
    print('Неправильный формат ввода')
   
