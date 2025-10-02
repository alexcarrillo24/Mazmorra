# Tiene que haber un desafio aritmetico
# Tiene que haber varios objetos que se tienen que coger y mas adelante mirar si el usuario lo tiene o no lo tiene 
from random import randint
numeroaleatorio = randint(1,50)
respuesta = numeroaleatorio * 10

titulo = "Mazmorra del Callao"
print(f"{"-" * len(titulo)}")
print(titulo)
print(f"{"-" * len(titulo)}")

print("""
Fuiste traicionado por uno de tus compinches,\n
te capturaron y te llevaron a Sarita,\n
debes escapar con algunos reclusos para poder vengarte de ese csmr.\n
    """)

opcion = input("""A - Intentas hablar con un guardia para sobornarlo\n
B - Decides organizar una fuga con los reclusos\n
               """)

if opcion == "A":
    print("Escogiste sobornar al guardia")

    opcion2 = input("""A - Le ofreces cariñosas los fines de semana\n
B - Le ofreces dinero luego de escapar\n
                    """)
    
    if opcion2 == "A":
        print("Coordinas con gente de afuera para mandarla su primera cariñosa")
    elif opcion2 == "B":
        print("Pides a un familiar que le de un pago anticipado")
    else:
        print("No seas paloma elige bien")
               
elif opcion == "B":
     
    print("Reunes a todos para el motin pero mantienes un grupo reducido quienes se fugaran contigo")
    opcion3 = input("""Para poder asegurar tu escape debes traicionar a todos, lo haras? (SI/NO)""")
    if opcion3 == "SI":
        print("Te atrapan por cagon")
    else:
        print("Continuas con ellos y aseguras tu escape")
        print("Vez a uno de los reclusos con un arma escondida")
        esTerna = input("""A - Lo acusas con los demas reclusos\n
B - No se lo dices a nadie, pero no le quitas la vista\n""")
        if esTerna == "A":
            print("Lo mataron por gil")
            print("Bombardean Sarita")
        elif esTerna == "B":
            print("Lo invitas a una celda para proponerle un plan")
            mentira = input("""A - Lo matas a escondidas\n
B - Le propones un plan\n""")
            arma = False
            if mentira == "A":
                print("Mataste al soplon")
                coger = input("""A - Coges el arma\n
B - Dejas el arma\n""")
                if coger == "A":
                    arma = True
                    print("Cogiste el arma")
                else:
                    print("Decidiste ser bebita")

                print("En el bolsillo de la camisa del terna viste una tarjeta con un codigo")
                codigo = input("""A - Tomas la tarjeta\n
B - No lo tomas\n""")
                if codigo == "A":
                    print("Tomaste la tarjeta y ves un problema aritmetico")
                    problemaAritmetico = int(input(f"Cuanto es {numeroaleatorio} * 10\n"))
                    if problemaAritmetico == respuesta:
                        print("Acertaste se abrio la puerta, vete ctm")    
                        escape = True
                        print("Encontraste un guardia en la puerta, debes atacarlo para huir")
                        if escape == True and arma == True:
                            print("Menos mal tomaste el arma, mataste al guardia y escapaste")
                        elif escape == True and arma == False:
                            print("Por no coger el arma, te mataron")
                    else:
                        print("MORISTE POR BRUTO")
                else:
                    print("No tomaste la tarjeta y moriste GIL")
                
            elif mentira == "B":
                print("El terna te descubrio y pium te mato")
        else:
            print("El terna te mato")


else: 
    print("Fijate las opciones oe firulais")


