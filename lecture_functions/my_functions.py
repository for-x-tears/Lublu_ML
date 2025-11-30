# task 1

# создать файл my_functions.py с функциями greet и change_name

# change_name - принимает строку, а возвращает измененное имя, где каждая вторая буква - большая

# greet - принимает строку, ничего не возвращает, а просто принтит "Hello имя" с помощью украшений из rich print


def change_name(text):
    half_text = text[0::2]
    result = half_text.upper()
    
    
    return result

print(change_name("Ваня"))