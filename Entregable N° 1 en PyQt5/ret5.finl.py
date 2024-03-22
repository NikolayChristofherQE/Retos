import re, uuid, os

def validate_string(value, min, max):
    length = len(value)

    if (min <= length <= max):
        return True
    else:
        return False


def validate_number(number):
    patron = r'^\d{10}$'

    if re.match(patron, number):
        return True
    else:
        return False

users_registered = {}
# users_registered = {
#    "1":{
#       "id":"1",
#       "name":"Carlos",
#       "last_name":"Medina",
#       "telephone_number":"9234567890",
#       "email":"correo@correo.com"
#    },
#    "2":{
#       "id":"2",
#       "name":"Luis",
#       "last_name":"Linares",
#       "telephone_number":"9876543210",
#       "email":"correo@correo.com"
#    }
# }

def new_user():
    print()
    num_users = int(input(" Ingresa la cantidad de nuevos usuarios que desea registrar: "))
    print()

    for index in range(1, num_users + 1):
        print(f" Registro del usuario {index}:", "\n")

        # Generar uuid
        id = str(uuid.uuid4())[:8]
        
        user = set_user()
        user["id"] = id

        users_registered[id] = user
        print()
        print(f" >> Info: Usuario creado correctamente con identificador: {id}", "\n")


def set_user():
    # Validación del nombre
    while True:
        name = input(" Ingresa tus nombres (entre 5 y 50 caracteres): ")
        if validate_string(name, 5, 50):
            break
        print(" >> Error: La longitud del nombre debe estar entre 5 y 50 caracteres.")

    # Validación del apellido
    while True:
        last_name = input(" Ingresa tus apellidos (entre 5 y 50 caracteres): ")
        if validate_string(last_name, 5, 50):
            break
        print(" >> Error: La longitud de los apellidos debe estar entre 5 y 50 caracteres.")

    # Validación del número de teléfono
    while True:
        telephone_number = input(" Ingresa tu número de teléfono (10 dígitos): ")
        if validate_number(telephone_number):
            break
        print(" >> Error: El número de teléfono debe tener 10 dígitos.")

    # Validación del correo electrónico
    while True:
        email = input(" Ingresa tu correo electrónico (entre 5 y 50 caracteres: ")
        if validate_string(email, 5, 50):
            break
        print(" >> Error: La longitud del correo electrónico debe estar entre 5 y 50 caracteres.")

    # Generar el diccionario user
    user = {
        "name" : name,
        "last_name" : last_name,
        "telephone_number" : telephone_number,
        "email" : email
    }
    return user


def show_user(id):
    user = users_registered.get(id)

    if user:
        print()
        print(f' |{"ID".ljust(8)}|{"Nombres".ljust(21)}|{"Apellidos".ljust(21)}|{"Número de teléfono".ljust(20)}|{"Correo electrónico".ljust(30)}|')
        print(" |--------|---------------------|---------------------|--------------------|------------------------------|")
        print(f" |{id.ljust(8)}|{user['name'].ljust(21)}|{user['last_name'].ljust(21)}|{user['telephone_number'].ljust(20)}|{user['email'].ljust(30)}|")
        print()
    else:
        print()
        print(" >> Info: Usuario no encontrado!!", "\n")


def edit_user(id):
    user = users_registered.get(id)

    if user:
        show_user(id)
        
        print(" Ingrese los nuevos datos: ", "\n")

        user_edit = set_user()
        user_edit["id"] = id
        users_registered[id] = user_edit
        print()
        print(f" >> Info: Usuario modificado correctamente con identificador: {id}", "\n")

    else:
        print()
        print(" >> Info: Usuario no encontrado!!", "\n")


def delete_user(id):
    user = users_registered.get(id)

    if user:
        del users_registered[id]
        print()
        print(f" >> Info: Usuario eliminado correctamente con identificador: {id}", "\n")
    else:
        print()
        print(" >> Info: Usuario no encontrado!!", "\n")


def list_users():
    if not users_registered:
        print()
        print(" >> Info: Aún no se han registrado usuarios.", "\n")
    else:
        print()
        print(f' |{"ID".ljust(8)}|{"Nombres".ljust(21)}|{"Apellidos".ljust(21)}|{"Número de teléfono".ljust(20)}|{"Correo electrónico".ljust(30)}|')
        print(" |--------|---------------------|---------------------|--------------------|------------------------------|")
        for key, user in users_registered.items():
            print(f" |{key.ljust(8)}|{user['name'].ljust(21)}|{user['last_name'].ljust(21)}|{user['telephone_number'].ljust(20)}|{user['email'].ljust(30)}|")
        print()


while True:
    print("Elegir la opción a, b, c, d, e o f según corresponda:", "\n")
    
    print(" a) Registrar nuevo usuario")
    print(" b) Mostrar información de un usuario")
    print(" c) Editar información de un usuario")
    print(" d) Eliminar información de un usuario")
    print(" e) Listar los usuarios registrados")
    print(" f) Salir del programa", "\n")
    
    option = input("Ingrese la opción de su preferencia: ").lower()

    match option:
        case "a":
            new_user()
        case "b":
            print()
            id = input(' Ingrese el identificador del usuario: ')
            show_user(id)
        case "c":
            print()
            id = input(" Ingrese el identificador del usuario: ")
            edit_user(id)
        case "d":
            print()
            id = input(" Ingrese el identificador del usuario: ")
            delete_user(id)
        case "e":
            list_users()
        case "f":
            print("Gracias por su participación!")
            os.system('cls')
            break
        case _:
            print('Opción no válida, vuelva a elegir')