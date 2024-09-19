# como primero crear la matriz para la cara x,y - y,z y hacer el juego en si
# en conjunto con las opciones de cara n*n y quemar opciones y tematicas de juego
def introduction():
    """FIRST MENU THAT SHOWS UP IN THE CONSOLE IF IT IS NECESARY, WITH THE OPTIONS:
        "INICIAR' : SENDS YOU TO THE SECOND MENU
        'SALIR' : EXITS THE PROGRAM
    """
    print("BIENVENIDO A CRUCIGRAMA 3D")
    print("1 > INICIAR")
    print("2 > SALIR")

    while True:
        try:
            choice = int(input("Por favor introduzca su elección: "))
            if choice == 1:
                show_options()
                break  
            elif choice == 2:
                print("Saliendo...")
                exit() 
            else:
                print("INTRODUZCA OPCION VALIDA")
                introduction()
        except ValueError:
            print("Por favor, introduzca una opcion válida '1,2'.")


def show_options():
    print("ESCOGE LA OPCION QUE DESEAS ELEGIR:\n"
      "1 > CRONOGRAMAS PREDETERMINADOS\n"
      "2 > CREAR TU PROPIO CRONOGRAMA 3D\n"
      "3 > VOLVER A PANTALLA PRINCIPAL")
    while True:
        choice = int(input("Introduzca la accion que desea realizar: "))
        while True: 
            try: 
                if choice == 1 :
                    cronogramas_quemados()
                    break
                elif choice == 2 :
                    crear_cronograma()
                    break
                elif choice == 3:
                    introduction()
                    break
                else: 
                    print("INTRODUZCA OPCION VALIDA")
                    show_options()
                    break
            except ValueError:
                print("Por favor, introduzca una opcion válida '1,2,3'.")
introduction()

