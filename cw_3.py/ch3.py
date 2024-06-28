def capitalize_last_name(first_name, last_name):
    my_first_name = first_name.capitalize()
    my_last_name = last_name.upper()
    print(my_first_name,my_last_name)

name = input()

list_name = name.split()
if len(list_name) > 2 or len(list_name) < 2:
    raise Exception("ValueError out of range")
for item in list_name:
    if not item.isalpha():
        raise Exception("string contains number or symbol")

capitalize_last_name(list_name[0],list_name[1])