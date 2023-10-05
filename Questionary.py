
"""This class is used to recopile the information of the user and build his profile"""

class Questionary:
    chr = []
    hobb = []

    
    def ask_hobbies():
        hobbies = []
        print("Qué prefieres?")
        answer=input("1. Montaña  o  2. Playa \n ")
        if answer == "1":
            hobbies.append("Montaña")
        elif answer == "2":
            hobbies.append("Playa")
        else:
            print("Opción no válida")
        answer=input("1. Mensaje de texto  o  2. Llamada \n ")
        if answer == "1":
            hobbies.append("Mensaje de texto")
        elif answer == "2":
            hobbies.append("Llamada")
        else:
            print("Opción no válida")
        answer=input("1. Ir de fiesta  o  2. Quedarme en casa \n ")
        if answer == "1":
            hobbies.append("Ir de fiesta")
        elif answer == "2":
            hobbies.append("Quedarme en casa")
        else:
            print("Opción no válida")
        answer=input("1. Social  o  2. Solitario \n ")
        if answer == "1":
            hobbies.append("Social")
        elif answer == "2":
            hobbies.append("Solitario")
        else:
            print("Opción no válida")
        answer=input("1. Planes espontáneos  o  2. Planes bien planeados \n ")
        if answer == "1":
            hobbies.append("Planes espontáneos")
        elif answer == "2":
            hobbies.append("Planes bien planeados")
        else:
            print("Opción no válida")
        answer=input("1. Dulce  o  2. Salado \n ")
        if answer == "1":
            hobbies.append("Dulce")
        elif answer == "2":
            hobbies.append("Salado")
        else:
            print("Opción no válida")
        answer=input("1. Clima caliente  o  2. Clima frío \n")
        if answer == "1":
            hobbies.append("Clima caliente")
        elif answer == "2":
            hobbies.append("Clima frío")
        else:
            print("Opción no válida")
        answer=input("1. Facebook  o  2. Instagram  \n")
        if answer == "1":
            hobbies.append("Facebook")
        elif answer == "2":
            hobbies.append("Instagram")
        else:
            print("Opción no válida")
        return hobbies

    def ask_characteristics():
        characteristics=[]
        print("Como te identificas?")
        answer=input("1.Alegre  o  2. Serio \n ")
        if answer == "1":
            characteristics.append("Alegre")
        elif answer == "2":
            characteristics.append("Serio")
        else:
            print("Opción no válida")
        answer=input("1.Formal o 2. Casual \n")
        if answer == "1":
            characteristics.append("Formal")
        elif answer == "2":
            characteristics.append("Casual")
        else:
            print("Opción no válida")
        answer=input("1. Racional  o  2. Emocional  \n")
        if answer == "1":
            characteristics.append("Racional")
        elif answer == "2":
            characteristics.append("Emocional")
        else:
            print("Opción no válida")
        answer=input("1. Introvertido  o  2. Extrovertido \n ")
        if answer == "1":
            characteristics.append("Introvertido")
        elif answer == "2":
            characteristics.append("Extrovertido")
        else:
            print("Opción no válida")
        answer=input("1. Reservado  o  2. Abierto  \n")   
        if answer == "1":
            characteristics.append("Reservado")
        elif answer == "2":
            characteristics.append("Abierto")
        else:
            print("Opción no válida")
        answer=input("1. Social o 2. Individual \n")
        if answer == "1":
            characteristics.append("Social")
        elif answer == "2":
            characteristics.append("Individual")
        else:
            print("Opción no válida")
        answer=input("1. Detallista  o  2. Distraido  \n ")
        if answer == "1":
            characteristics.append("Detallista")
        elif answer == "2":
            characteristics.append("Distraido")
        else:
            print("Opción no válida")
        answer=input("1. Independiente  o  2. Dependiente \n ")
        if answer == "1":
            characteristics.append("Independiente")
        elif answer == "2":
            characteristics.append("Dependiente")
        else:
            print("Opción no válida")
        answer=input("1. Afectuoso  o  2. Frio \n ")
        if answer == "1":
            characteristics.append("Afectuoso")
        elif answer == "2":
            characteristics.append("Frio")
        else:
            print("Opción no válida")
        answer=input("1. Generoso  o  2. Ambicioso \n ")
        if answer == "1":
            characteristics.append("Generoso")
        elif answer == "2":
            characteristics.append("Ambicioso")
        else:
            print("Opción no válida")
        answer=input("1. Tradicional o 2. Liberal \n")
        if answer == "1":
            characteristics.append("Tradicional")
        elif answer == "2":
            characteristics.append("Liberal")
        else:
            print("Opción no válida")
        return characteristics


    def ask_questions():
        chr=ask_characteristics()
        hobb=ask_hobbies()
        return chr, hobb

