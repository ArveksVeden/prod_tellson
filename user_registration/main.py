def validate(name, surname, phone):
    # Проверяем имя и фамилию
    if not (1 <= len(name) <= 25 and name[0].isupper() and name[1:].islower()):
        return "no"
    if not (1 <= len(surname) <= 25 and surname[0].isupper() and surname[1:].islower()):
        return "no"
    
    # Проверяем номер телефона
    if not (phone.startswith("+7") and len(phone) == 12 and phone[1:].isdigit()):
        return "no"
    
    return "yes"
 
test_count = int(input())
for i in range(test_count):
    name = input()
    surname = input()
    phone = input()
    print(validate(name, surname, phone))
