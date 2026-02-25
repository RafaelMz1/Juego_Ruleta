import random,time
print("Bienvenido al juego de la ruleta")
while True:
    lista1= ["Manzana", "Pera", "Uva", "Mango", "Piña"]
    lista2= ["Manzana", "Pera", "Uva", "Mango", "Piña"]
    lista3= ["Manzana", "Pera", "Uva", "Mango", "Piña"]

    random_list1 = random.choice(lista1)
    random_list2 = random.choice(lista2)
    random_list3 = random.choice(lista3)
    inicio = time.time()
    print(random_list1,random_list2,random_list3)
    if random_list1 == random_list2 == random_list3:
        print("\nGANASTE\n")
        final = time.time()
        diferencia = final-inicio
        print(f"te demoraste {diferencia} segundos")
        print("\nQuieres jugar de nuevo?")
        opcion = input(':').lower()
        if opcion == "si":
            print()
        else:
            print("esta bien")
            break
        if diferencia > 60:
            print(f"te demoraste {diferencia/60} minutos")

    else:
        print("\nPERDISTE\n")
        time.sleep(1)

